const socket = new WebSocket("ws://k08m287b-8000.euw.devtunnels.ms/");
socket.addEventListener("open", () => {
    console.log("Success");
    socket.send("Hello Server");
});