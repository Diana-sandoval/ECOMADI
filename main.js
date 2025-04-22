
let energia = 100;
let agua = 100;
let residuos = 0;

function elegir(opcion) {
  const mensaje = document.getElementById('mensaje');
  if (opcion === 'si') {
    energia += 10;
    residuos += 5;
    mensaje.innerText = 'Invertiste en energía solar. ¡Buen paso!';
  } else {
    energia -= 10;
    mensaje.innerText = 'No hiciste la inversión. La energía baja.';
  }
  actualizarStats();
}

function actualizarStats() {
  document.getElementById('energia').innerText = energia;
  document.getElementById('agua').innerText = agua;
  document.getElementById('residuos').innerText = residuos;
}
