
export const connectToWebSocket = () => {
  const ws = new WebSocket("ws://127.0.0.1:8000/v1/api/conversations/ws/conversations");

  ws.onopen = () => console.log("✔ Connected to WS");
  ws.onmessage = (event) => console.log("📩 Received:", event.data);
  ws.onclose = () => console.log("❌ WS Closed");
  ws.onerror = (err) => console.error("⚠ WS Error:", err);

  return ws;
};
