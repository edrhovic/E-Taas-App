from fastapi import HTTPException, status, UploadFile
from dependencies.websocket import connection_manager
from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.conversation import Conversation, MessageImage, Message
from utils.logger import logger
from utils.cloudinary import upload_image_to_cloudinary

async def get_conversations_for_user(db: AsyncSession, user_id: int) -> List[Conversation]:
    try:
        result = await db.execute(select(Conversation).where(Conversation.user_id == user_id))
        conversations = result.scalars().all()
        logger.info(f"Fetched {len(conversations)} conversations for user {user_id}")
        if not conversations:
            return []
        return conversations
    
    except HTTPException:
        raise
    
    except Exception as e:
        logger.error(f"Error fetching conversations for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch conversations for the user."
        ) from e
    
async def get_messages_for_conversation(db: AsyncSession, conversation_id: int) -> List[Message]:
    try:
        result = await db.execute(
            select(Message)
            .options(selectinload(Message.images))
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.timestamp.asc())
        )
        messages = result.scalars().all()
        logger.info(f"Fetched {len(messages)} messages for conversation {conversation_id}")
        if not messages:
            return []
        return messages
    
    except HTTPException:
        raise
    
    except Exception as e:
        logger.error(f"Error fetching messages for conversation {conversation_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch messages for the conversation."
        ) from e
    
