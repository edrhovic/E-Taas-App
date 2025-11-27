from fastapi import HTTPException, status
from sqlalchemy import select
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models.notification import Notification
import logging
from dependencies.websocket import connection_manager
from utils.logger import logger


async def create_new_notification(db: AsyncSession, user_id: int, message: str) -> Notification:
    """Create a new notification for a user."""
    try:
        notification = Notification(user_id=user_id, message=message)
        db.add(notification)
        await db.commit()
        await db.refresh(notification)

        await connection_manager.send_message(message, user_id)

        logger.info(f"Notification created for user {user_id}: {message}")
        return notification
    
    except HTTPException:
        raise
    
    except Exception as e:
        await db.rollback()
        logger.exception(f"Error creating notification for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
async def get_notifications_for_user(db: AsyncSession, user_id: int) -> List[Notification]:
    try:
        result = await db.execute(select(Notification).where(Notification.user_id == user_id).order_by(Notification.created_at.desc()))
        notifications = result.scalars().all()
        logger.info(f"Retrieved {len(notifications)} notifications for user {user_id}")

        if not notifications:
            return []
        
        return notifications
    
    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Error retrieving notifications for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
async def mark_notification_as_read(db: AsyncSession, notification_id: int, user_id: int) -> Notification:
    try:
        result = await db.execute(select(Notification).where(Notification.id == notification_id, Notification.user_id == user_id))
        notification = result.scalar_one_or_none()

        if not notification:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Notification not found."
            )

        notification.is_read = True
        await db.commit()
        await db.refresh(notification)

        logger.info(f"Marked notification {notification_id} as read for user {user_id}")
        return notification

    except HTTPException:
        raise

    except Exception as e:
        await db.rollback()
        logger.error(f"Error marking notification {notification_id} as read for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
async def mark_all_notifications_as_read(db: AsyncSession, user_id: int) -> int:
    try:
        result = await db.execute(select(Notification).where(Notification.user_id == user_id, Notification.is_read == False))
        notifications = result.scalars().all()

        if not notifications:
            return 0

        for notification in notifications:
            notification.is_read = True

        await db.commit()
        logger.info(f"Marked all notifications as read for user {user_id}")
        return len(notifications)

    except HTTPException:
        raise

    except Exception as e:
        await db.rollback()
        logger.error(f"Error marking all notifications as read for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        ) from e
    
