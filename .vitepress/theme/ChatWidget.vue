<template>
  <div class="chat-widget" :class="{ open: isOpen }">
    <!-- Кнопка открытия чата -->
    <button v-if="!isOpen" class="chat-button" @click="isOpen = true">
      💬 Задать вопрос
    </button>

    <!-- Окно чата -->
    <div v-else class="chat-window">
      <div class="chat-header">
        <span>Авто-ассистент</span>
        <button class="close-btn" @click="isOpen = false">✕</button>
      </div>
      
      <div class="chat-messages" ref="messagesContainer">
        <div v-if="messages.length === 0" class="welcome-message">
          Задайте вопрос по автомобилям, и я найду ответ в базе знаний!
        </div>
        
        <div v-for="(msg, idx) in messages" :key="idx" :class="['message', msg.role]">
          <div class="message-content">{{ msg.content }}</div>
          <div v-if="msg.sources && msg.sources.length" class="sources">
            📚 {{ msg.sources.join(', ') }}
          </div>
        </div>
        
        <div v-if="isLoading" class="message assistant">
          <div class="typing-indicator">
            <span></span><span></span><span></span>
          </div>
        </div>
      </div>

      <form class="chat-input" @submit.prevent="sendMessage">
        <input 
          v-model="inputText" 
          type="text" 
          placeholder="Например: Какие машины до 100 тысяч?"
          :disabled="isLoading"
        />
        <button type="submit" :disabled="isLoading || !inputText.trim()">➤</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const isOpen = ref(false)
const inputText = ref('')
const messages = ref([])
const isLoading = ref(false)
const messagesContainer = ref(null)

const API_URL = 'http://127.0.0.1:8000'

async function sendMessage() {
  const question = inputText.value.trim()
  if (!question) return

  // Добавляем сообщение пользователя
  messages.value.push({ role: 'user', content: question })
  inputText.value = ''
  
  isLoading.value = true
  await scrollToBottom()

  try {
    const response = await fetch(`${API_URL}/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: question })
    })

    const data = await response.json()
    
    messages.value.push({ 
      role: 'assistant', 
      content: data.response,
      sources: data.sources
    })
  } catch (error) {
    messages.value.push({ 
      role: 'assistant', 
      content: 'Ошибка соединения с сервером. Убедитесь, что API запущен на порту 8000.' 
    })
  } finally {
    isLoading.value = false
    await scrollToBottom()
  }
}

async function scrollToBottom() {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}
</script>

<style scoped>
.chat-widget {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
  font-family: system-ui, sans-serif;
}

.chat-button {
  background: #ff6a00;
  color: white;
  border: none;
  border-radius: 30px;
  padding: 14px 24px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(255, 106, 0, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}

.chat-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 106, 0, 0.5);
}

.chat-window {
  width: 380px;
  height: 550px;
  background: #1e1e1e;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-header {
  user-select: none;
  background: #ff6a00;
  color: white;
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.close-btn:hover {
  opacity: 0.8;
}

.chat-messages {
  user-select: none;
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #252525;
}

.welcome-message {
  color: #888;
  text-align: center;
  margin-top: 40px;
  font-size: 14px;
}

.message {
  max-width: 85%;
  padding: 12px 16px;
  border-radius: 18px;
  font-size: 14px;
  line-height: 1.5;
}

.message.user {
  background: #ff6a00;
  color: white;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}

.message.assistant {
  background: #333;
  color: #eee;
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}

.sources {
  margin-top: 8px;
  font-size: 11px;
  opacity: 0.7;
  color: #aaa;
}

.chat-input {
  display: flex;
  padding: 16px;
  background: #1e1e1e;
  border-top: 1px solid #333;
  gap: 10px;
}

.chat-input input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #444;
  border-radius: 30px;
  background: #2c2c2c;
  color: white;
  font-size: 14px;
  outline: none;
}

.chat-input input:focus {
  border-color: #ff6a00;
}

.chat-input input::placeholder {
  color: #888;
}

.chat-input button {
  background: #ff6a00;
  color: white;
  border: none;
  border-radius: 50%;
  width: 44px;
  height: 44px;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.chat-input button:hover:not(:disabled) {
  background: #e05a00;
}

.chat-input button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 4px 0;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background: #888;
  border-radius: 50%;
  animation: typing 1.4s infinite;
}

.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-8px); }
}
</style>