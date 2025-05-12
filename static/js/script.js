document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('upload-form');
  const fileInput = document.getElementById('file');
  const fileNameDisplay = document.getElementById('file-name');
  const loading = document.getElementById('loading');
  const error = document.getElementById('error');
  const success = document.getElementById('success');
  const submitButton = form.querySelector('button[type="submit"]');

  // Función para ocultar todos los mensajes
  function resetMessages() {
    loading.style.display = 'none';
    error.style.display = 'none';
    success.style.display = 'none';
  }

  // Actualizar nombre del archivo seleccionado
  fileInput.addEventListener('change', function () {
    const name = this.files[0]?.name || '';
    fileNameDisplay.textContent = name;
    fileInput.classList.remove('is-invalid');
    resetMessages();
  });

  // Validación y manejo de formulario al enviar
  form.addEventListener('submit', function (e) {
    resetMessages();  // Limpiar mensajes previos

    // Si no se seleccionó archivo
    if (fileInput.files.length === 0) {
      e.preventDefault();  // Evitar el envío
      fileInput.classList.add('is-invalid');  // Resaltar como inválido
      error.textContent = "Por favor, selecciona un archivo válido.";
      error.style.display = 'block';  // Mostrar mensaje de error
      return;
    }

    // Deshabilitar el botón de submit para evitar múltiples clics
    submitButton.disabled = true;

    // Si todo está bien, mostrar mensaje de carga
    loading.style.display = 'block';
  });
});

$(document).ready(function () {
  $('#resultTable').DataTable({
    responsive: true,
    pageLength: 5,
    language: {
      lengthMenu: "Mostrar _MENU_ registros",
      zeroRecords: "No se encontraron resultados",
      info: "Página _PAGE_ de _PAGES_",
      infoEmpty: "No hay datos disponibles",
      infoFiltered: "(filtrado de _MAX_ filas)",
      search: "Buscar:",
      paginate: {
        previous: "Anterior",
        next: "Siguiente"
      }
    }
  });
});


// static/js/script.js
document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('menuToggle');
  const overlay = document.getElementById('overlay');

  // Toggle para el menú en pantallas pequeñas
  toggleBtn.addEventListener('click', function () {
    if (window.innerWidth <= 768) {
      sidebar.classList.toggle('show');
      overlay.classList.toggle('show');
    } else {
      sidebar.classList.toggle('collapsed');
    }
  });

  // Cerrar sidebar cuando se hace click en el overlay
  overlay.addEventListener('click', function () {
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  });
});



