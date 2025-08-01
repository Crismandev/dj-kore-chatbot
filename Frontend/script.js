// Referencias a los elementos del HTML
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// URL de la API Django local
const API_URL = 'http://127.0.0.1:8000/api/chat/';

// Función para agregar un mensaje a la ventana del chat
function addMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${sender}-message`);
    
    // Procesar markdown básico para respuestas de IA
    if (sender === 'ai') {
        message = processMarkdown(message);
    }
    
    messageElement.innerHTML = `<p>${message}</p>`;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Función simple para procesar markdown
function processMarkdown(text) {
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/\n/g, '<br>');
}

// Función para enviar el mensaje a la IA
async function sendMessageToAI() {
    const message = userInput.value.trim();
    if (message === '') return;

    // Muestra el mensaje del usuario
    addMessage(message, 'user');
    userInput.value = '';
    
    // Deshabilitar input mientras procesa
    userInput.disabled = true;
    sendBtn.disabled = true;

    try {
        // Mostrar indicador de escritura
        const thinkingId = Date.now();
        addMessage('🎧 DJ Kore está pensando...', 'ai');
        const thinkingElement = chatMessages.lastElementChild;

        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Remover indicador de escritura
        thinkingElement.remove();
        
        // Mostrar respuesta
        const aiResponse = data.respuesta || 'Lo siento, no pude procesar esa respuesta.';
        addMessage(aiResponse, 'ai');
        
    } catch (error) {
        console.error('Error:', error);
        // Remover indicador de escritura si existe
        const thinkingElement = chatMessages.querySelector('.ai-message:last-child');
        if (thinkingElement && thinkingElement.textContent.includes('pensando')) {
            thinkingElement.remove();
        }
        addMessage('❌ Error: No se pudo conectar con DJ Kore. Verifica que el servidor esté ejecutándose.', 'ai');
    } finally {
        // Rehabilitar input
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

// Event Listeners
sendBtn.addEventListener('click', sendMessageToAI);
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessageToAI();
    }
});

// Enfocar input al cargar
window.addEventListener('load', () => {
    userInput.focus();
});
