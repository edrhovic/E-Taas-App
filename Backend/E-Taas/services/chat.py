from fastapi import HTTPException, status, UploadFile
from dependencies.websocket import connection_manager
from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.conversation import Conversation, MessageImage, Message
from utils.logger import logger
from utils.cloudinary import upload_image_to_cloudinary
from schemas.chat import MessageCreate

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
    
async def create_a_conversation(db: AsyncSession, user_id: int, seller_id: int) -> Conversation:
    try:
        existing_result = await db.execute(
            select(Conversation).where(
                Conversation.user_id == user_id,
                Conversation.seller_id == seller_id
            )
        )
        existing_conversation = existing_result.scalar_one_or_none()
        if existing_conversation:
            logger.info(f"Conversation already exists between user {user_id} and seller {seller_id}")
            return existing_conversation

        new_conversation = Conversation(
            user_id=user_id,
            seller_id=seller_id
        )
        db.add(new_conversation)
        await db.commit()
        await db.refresh(new_conversation)

        logger.info(f"Created new conversation {new_conversation.id} between user {user_id} and seller {seller_id}")
        return new_conversation
    
    except HTTPException:
        raise
    
    except Exception as e:
        await db.rollback()
        logger.error(f"Error creating conversation between user {user_id} and seller {seller_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create conversation."
        ) from e
    
async def send_new_message(db: AsyncSession, message_data: MessageCreate, current_user_id: int, images: Optional[List[UploadFile]] = None, conversation_id: int = None) -> Message:
    try:

        if message_data.sender_type not in ["user", "seller"]:
            raise HTTPException(status_code=400, detail="Invalid sender type.")
        
        if message_data.sender_type == "user":
            user_id = current_user_id
            seller_id = message_data.receiver_id
        else:
            user_id = message_data.receiver_id
            seller_id = current_user_id

        if not conversation_id:
            conversation = await create_a_conversation(db, user_id, seller_id)
        else:
            result = await db.execute(
                select(Conversation).where(Conversation.id == conversation_id)
            )
            conversation = result.scalar_one_or_none()
            if not conversation:
                conversation = await create_a_conversation(db, user_id, seller_id)

        new_message = Message(
            conversation_id=conversation.id,
            sender_id=current_user_id,
            sender_type=message_data.sender_type,
            message=message_data.message
        )

        db.add(new_message)
        await db.commit()
        await db.refresh(new_message)
        logger.info(f"Created new message {new_message.id} in conversation {conversation.id}")

        if images:
            for image in images:
                image_url = await upload_image_to_cloudinary([image], folder="chat_messages_images")
                message_image = MessageImage(
                    message_id=new_message.id,
                    image_url=image_url[0]["secure_url"]
                )
                db.add(message_image)
            await db.commit()
            logger.info(f"Added {len(images)} images to message {new_message.id}")

        return new_message
    
    except HTTPException:
        raise

    except Exception as e:
        await db.rollback()
        logger.error(f"Error sending message in conversation {conversation_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send message."
        ) from e