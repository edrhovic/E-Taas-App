import React, { useEffect, useRef, useState } from "react";
import { connectToWebSocket } from "../../../services/user/UserNotification";

interface NotificationMessage {
  id: number;
  title: string;
  body: string;
  timestamp: string;
}

const Notifications: React.FC = () => {
  const ws = useRef<WebSocket | null>(null);
  const [notifications, setNotifications] = useState<NotificationMessage[]>([]);

  useEffect(() => {
    ws.current = connectToWebSocket();

    ws.current.onmessage = (event: MessageEvent) => {
      try {
        const data: NotificationMessage = JSON.parse(event.data);
        setNotifications(prev => [data, ...prev]);
      } catch (err) {
        console.error("Failed to parse message", err);
      }
    };

    return () => {
      ws.current?.close();
    };
  }, []);

  return (
    <div>
      <h2>Notifications</h2>
      <ul>
        {notifications.map(n => (
          <li key={n.id}>
            <strong>{n.title}</strong>: {n.body} <em>({n.timestamp})</em>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
