from fastapi import APIRouter, HTTPException, Query, WebSocket, WebSocketDisconnect, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import create_task
from core.security import decode_token
from core.config import settings
from dependencies.websocket import chat_manager
from utils.logger import logger



router = APIRouter()

@router.websocket("/ws/conversations")
async def chat_websocket_endpoint(
    request: Request,
    websocket: WebSocket
):
    try:
        await websocket.accept()
        logger.info("WebSocket connection accepted.")
        token = request.cookies.get("access_token")
        logger.info("Access token retrieved from cookies.")
        payload = decode_token(token, settings.SECRET_KEY, [settings.ALGORITHM])
        logger.info("Token decoded successfully.")
        user_id = payload["user_id"]
        logger.info(f"User ID extracted from token: {user_id}")
    except Exception:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        await chat_manager.connect(websocket, user_id)
        print(f"User {user_id} connected to chat manager.")
        heartbeat_task = create_task(chat_manager.heartbeat(websocket))
        logger.info(f"Heartbeat task started for user {user_id}.")

        while True:
            try:
                data = await websocket.receive_text()
                await chat_manager.send_message(data, user_id)
            except WebSocketDisconnect:
                break
            except Exception as e:
                break

    finally:
        heartbeat_task.cancel()
        await chat_manager.disconnect(websocket, user_id)