import asyncio
import os
import threading
import websockets
import importlib.util


from kivy.uix.widget import Widget
from typing import Callable, Optional


from kivy.properties import ObjectProperty

from kivy.event import EventDispatcher
from kivy.clock import mainthread

_PREVIEW_PATH = os.path.join(os.path.dirname(__file__), 'preview.py')


class WidgetServer:
    def __init__(self, host: str, port: int, on_preview_written: Callable[[object | None], None]):
        self.host = host
        self.port = port
        self.is_running = False
        self._on_preview_written = on_preview_written
        self._loop = None
        self._thread = None
        self._ws_server = None

    def start(self):
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.is_running = False
        if self._loop:
            self._loop.call_soon_threadsafe(self._loop.stop)
        if self._thread:
            self._thread.join(timeout=5)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _run_loop(self):
        asyncio.set_event_loop(self._loop)
        self._loop.run_until_complete(self._serve())

    async def _serve(self):
        self.is_running = True
        async with websockets.serve(self._handle_client, self.host, self.port) as server:
            self._ws_server = server
            await asyncio.Future()  # run until the loop is stopped

    async def _handle_client(self, websocket):
        async for message in websocket:
            await websocket.send('ok')
            self._on_preview_written(message)



class NetworkListener(EventDispatcher):
    def __init__(self, ip: str, port: int, **kwargs):
        super().__init__(**kwargs)
        self.server = WidgetServer(ip, port, self.receive_new_widget)
        self.register_event_type('on_new_widget')


    @mainthread
    def receive_new_widget(self, new_module_code: str):

        try :
            g = {
                '__name__': 'figma_kivy_previewer._preview',
                '__package__': 'figma_kivy_previewer',
            }
            exec(new_module_code, g)
            new_widget = g['preview'] if 'preview' in g else None
            if new_widget is None:
                print("No 'preview' widget found in the received module.")
                return

            self.dispatch('on_new_widget', new_widget)
        except Exception as e:
            print(f"Error loading new widget: {e}")


    def start(self):
        self.server.start()

    def stop(self):
        self.server.stop()

    def on_new_widget(self, new_widget):
        pass

