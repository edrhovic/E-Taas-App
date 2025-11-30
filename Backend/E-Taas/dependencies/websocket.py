
from typing import List, Dict
from fastapi import WebSocket
import asyncio

class NotificationConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)

    async def send_message(self, message: str, user_id: int):
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_text(message)
                except Exception:
                    self.disconnect(connection, user_id)

    async def heartbeat(self, websocket: WebSocket, interval: int = 30):
        while True:
            try:
                await websocket.send_text("ping")
                await asyncio.sleep(interval)
            except Exception:
                break
    
    def disconnect(self, websocket: WebSocket, user_id: int):
        if user_id in self.active_connections:
            self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

class ChatConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, participant_type: str, participant_id: int):
        await websocket.accept()
        key = f"{participant_type}:{participant_id}"
        self.active_connections.setdefault(key, []).append(websocket)

    async def disconnect(self, websocket: WebSocket, participant_type: str, participant_id: int):
        key = f"{participant_type}:{participant_id}"
        if key in self.active_connections:
            if websocket in self.active_connections[key]:
                self.active_connections[key].remove(websocket)
            if not self.active_connections[key]:
                del self.active_connections[key]

    async def send_message(self, message: str, recipient_type: str, recipient_id: int):
        key = f"{recipient_type}:{recipient_id}"
        for ws in self.active_connections.get(key, []):
            await ws.send_json({"message": message})

    async def heartbeat(self, websocket: WebSocket, interval: int = 30):
            while True:
                try:
                    await websocket.send_text("ping")
                    await asyncio.sleep(interval)
                except Exception:
                    break
notification_manager = NotificationConnectionManager()
chat_manager = ChatConnectionManager()