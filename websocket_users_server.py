import asyncio
import websockets
from websockets import ServerConnection

async def my_echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"

        for _ in range(5):
            await websocket.send(response)

async def my_main():
    server = await websockets.serve(my_echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(my_main())