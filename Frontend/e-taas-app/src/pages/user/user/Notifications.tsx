import React, { useEffect, useRef, useState } from "react";
import { connectToWebSocket } from "../../../services/user/UserNotification";

interface NotificationMessage {
  id: number;
}

const Notifications: React.FC = () => {
  const ws = useRef<WebSocket | null>(null);
  const [notifications, setNotifications] = useState<NotificationMessage[]>([]);

  useEffect(() => {
    // Create WebSocket
    ws.current = connectToWebSocket();

    // Handle incoming messages
    const handleMessage = (event: MessageEvent) => {
      const msg = event.data;
      if (msg === "ping") return; // ignore heartbeat

      try {
        const data: NotificationMessage = JSON.parse(msg);
        setNotifications(prev => [data, ...prev]);
      } catch (err) {
        console.error("Failed to parse message", err);
      }
    };

    ws.current.addEventListener("message", handleMessage);
    return () => {
      // Cleanup on unmount
      if (ws.current) {
        ws.current.removeEventListener("message", handleMessage);
        ws.current.close();
      }
    }
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
