#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def connection_handler(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"connection_handler {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(connection_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()