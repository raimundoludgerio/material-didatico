// Exemplo de "componente" de card
function criarCardUsuario(usuario) {
  const card = document.createElement('div');
  card.classList.add('card');

  card.innerHTML = `
      <h3>${usuario.nome}</h3>
      <p><strong>Email:</strong> ${usuario.email}</p>
    `;

  return card;
}

async function carregarUsuarios() {
  const usuariosPromise = await fetch(
    "https://raw.githubusercontent.com/raimundoludgerio/material-didatico/refs/heads/main/web/javascript/aula02/usuarios.json",
  );
  const users = await usuariosPromise.json();
  return users
}
carregarUsuarios().then(usuarios => {
  const container = document.getElementById('container');
  console.log(usuarios)
  usuarios.forEach(usuario => {
    const card = criarCardUsuario(usuario);
    container.appendChild(card);
  });
})
