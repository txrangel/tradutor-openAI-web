document.addEventListener('DOMContentLoaded', () => {
    const form          = document.getElementById('tradutor-form');
    const textoInput    = document.getElementById('texto');
    const idiomaInput   = document.getElementById('idioma');
    const resultadoDiv  = document.getElementById('resultado-traducao');
  
    form.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const texto   = textoInput.value;
      const idioma  = idiomaInput.value;
  
      fetch('/traduzir', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ texto, idioma })
      })
        .then(response => response.json())
        .then(data => {
          resultadoDiv.textContent = `Tradução para ${idioma}: ${data.traducao}`;
        })
        .catch(error => {
          console.error('Ocorreu um erro:', error);
        });
    });
  });
  