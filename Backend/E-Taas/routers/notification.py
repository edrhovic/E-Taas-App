from fastapi import APIRouter, Depends, status, Request, WebSocket, WebSocketDisconnect, Query
from dependencies.auth import decode_token
from core.config import settings
from dependencies.websocket import notification_manager
from asyncio import create_task

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):

    try:
        payload = decode_token(token, settings.SECRET_KEY, [settings.ALGORITHM])
        user_id = payload["user_id"]
    except Exception:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        await notification_manager.connect(websocket, user_id)
        heartbeat_task = create_task(notification_manager.heartbeat(websocket))

        while True:
            try:
                data = await websocket.receive_text()
                await notification_manager.send_message(data, user_id)
            except WebSocketDisconnect:
                break
            except Exception as e:
                break

    finally:
        heartbeat_task.cancel()
        await notification_manager.disconnect(websocket, user_id)