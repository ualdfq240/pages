const API_URL = 'http://pages-production-b821.up.railway.app:8080/';


function agregarAlChat(texto, clase) {
  const chat = document.getElementById("chat-box");
  const p = document.createElement("p");
  p.textContent = texto;
  p.style.fontWeight = clase === "bot" ? "bold" : "normal";
  chat.appendChild(p);
  chat.scrollTop = chat.scrollHeight;
}

function enviarMensaje() {
  const input = document.getElementById("mensaje");
  const mensaje = input.value.trim();
  if (!mensaje) return;

  agregarAlChat("Tú: " + mensaje, "user");

  fetch(API_URL, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({mensaje})
  })
  .then(res => res.json())
  .then(data => {
    agregarAlChat("Bot: " + data.respuesta, "bot");
  });

  input.value = "";
}

