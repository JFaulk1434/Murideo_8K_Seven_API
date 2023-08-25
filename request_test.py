"""Testing proof of concept"""

import asyncio
import websockets


async def handle_message(websocket):
    async for message in websocket:
        print("Received:", message)
        parts = message.split("||")
        if len(parts) == 3:
            # Handle 3-part messages
            command, value1, value2 = parts
            print(f"Command: {command}, Value 1: {value1}, Value 2: {value2}")


async def send_single_command(websocket, id, value):
    command = f"\r\nSENDSINGLE||{id},{value}\r\n"
    print(f"Sending command: {command.strip()}")
    await websocket.send(command)


async def main():
    uri = "ws://10.0.30.43/ws/uart"
    async with websockets.connect(uri) as websocket:
        # Mimic the WebUI command
        await websocket.send("\r\nSENDSINGLE||97,111\r\n")

        # Start listening to incoming messages
        await handle_message(websocket)


asyncio.get_event_loop().run_until_complete(main())
