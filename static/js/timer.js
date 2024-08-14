// Tiempo inicial en segundos
let timeLeft = 60;  // 1 minuto = 60 segundos
const timerElement = document.getElementById('timer');

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

const timer = setInterval(() => {
    if (timeLeft > 0) {
        timeLeft--;
        timerElement.textContent = formatTime(timeLeft);
    } else {
        clearInterval(timer);
        timerElement.textContent = '00:00';
        alert('¡El tiempo ha terminado!');
    }
}, 1000); // Actualiza cada 1000 milisegundos (1 segundo)
