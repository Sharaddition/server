import asyncio
import websockets

async def server(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

async def start_server():
    async with websockets.serve(server, "0.0.0.0", 8989):
        print('Server: ON')
        await asyncio.Future()  # Run forever

asyncio.run(start_server())
