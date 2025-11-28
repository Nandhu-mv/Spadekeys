import asyncio
import websockets
from pynput.keyboard import Controller, Key

keyboard = Controller()

async def handle_connection(websocket):
    async for message in websocket:
        print(f"Received: {message}")
        if message.startswith("KEY_"):
            key = message.replace("KEY_", "")
            if len(key) == 1:
                keyboard.press(key)
                keyboard.release(key)
            elif key == "ENTER":
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            elif key == "SPACE":
                keyboard.press(Key.space)
                keyboard.release(Key.space)

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 8765):
        print("Server running on ws://0.0.0.0:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
