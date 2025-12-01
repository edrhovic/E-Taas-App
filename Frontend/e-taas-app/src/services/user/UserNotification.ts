
export const connectToWebSocket = () => {
  const ws = new WebSocket("ws://localhost:8000/v1/api/notifications/ws");

  ws.onopen = () => console.log("✔ Connected to WS");
  ws.onmessage = (event) => console.log("📩 Received:", event.data);
  ws.onclose = () => console.log("❌ WS Closed");
  ws.onerror = (err) => console.error("⚠ WS Error:", err);

  return ws;
};
