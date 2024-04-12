import asyncio
import websockets

print("\033[92m OPEN:       Server")

raw_audio = None
state = 'Free'
async def receive_data(websocket):
  buffer = b''
  global state
  global raw_audio
  while True:
    try:
      async for message in websocket:
        data = message
        if data == "EOF":
            print("End of audio stream")
        elif isinstance(data, str):
            # Handle JSON or text data
            print(f"Received text data: {data}")
        else:
            # Chunk audio data
            buffer += data
            while len(buffer) >= CHUNK_SIZE:
                chunk = buffer[:CHUNK_SIZE]
                buffer = buffer[CHUNK_SIZE:]
                
    except websockets.ConnectionClosed:
      print("WebSocket connection closed.")


async def start_server(port):
    async with websockets.serve(receive_data, "localhost", port):
        print("\033[92m OPEN:       Websocket \033[0m")
        await asyncio.Future()  # Run the server indefinitely

async def send_test_message():
    uri = "ws://localhost:6969"  # Change to your Docker container's IP if not running locally

    async with websockets.connect(uri) as websocket:
        # Send a test message
        message = "Hello, WebSocket!"
        await websocket.send(message)
        print(f"Sent: {message}")

async def main():
    # Choose a port number for your WebSocket server
    port = 6969

    # Create and start the server coroutine
    server_task = asyncio.create_task(start_server(port))
    send_task = asyncio.create_task(send_test_message())

    # Run the event loop in the main thread
    await asyncio.gather(server_task, send_task)  # Wait for both server and printing to finish
    print("Server stopped.")

if __name__ == "__main__":
    asyncio.run(main())
