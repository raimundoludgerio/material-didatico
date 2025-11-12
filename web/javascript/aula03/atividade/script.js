const container = document.getElementById('container');
const statusEl = document.getElementById('status');
const buscaInput = document.getElementById('busca');

async function carregarDeputados() {
  try {
    statusEl.textContent = "⏳ Carregando deputados...";
    const resp = await fetch('https://dadosabertos.camara.leg.br/api/v2/deputados');
    const json = await resp.json();

    statusEl.textContent = "";

    const deputados = json.dados;
    exibirDeputados(deputados);

    // Filtro por nome
    buscaInput.addEventListener('input', e => {
      const termo = e.target.value.toLowerCase();
      const filtrados = deputados.filter(d =>
        d.nome.toLowerCase().includes(termo)
      );
      exibirDeputados(filtrados);
    });
  } catch (erro) {
    statusEl.textContent = "❌ Erro ao carregar dados.";
    console.error(erro);
  }
}

function exibirDeputados(lista) {
  container.innerHTML = "";
  lista.forEach(dep => {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
      <img src="${dep.urlFoto}" alt="${dep.nome}">
      <div class="card-content">
        <h3>${dep.nome}</h3>
        <p>${dep.siglaPartido} - ${dep.siglaUf}</p>
      </div>
    `;
    container.appendChild(card);
  });
}

carregarDeputados();
