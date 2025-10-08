async function minhaFuncaoAssincrona(user) {
    const buscaApi = await fetch("https://raw.githubusercontent.com/raimundoludgerio/material-didatico/refs/heads/main/web/javascript/aula02/usuarios.json");
    const res = await buscaApi.json()
    res.forEach(u => {
        if (u.email === user.email) console.log(u);
    });
}

async function essaFuncaoTemErro() {
    try {
        const buscaApi = await fetch("url_invalida");
        if (!buscaApi.ok) throw new Error("Requisição Falhou");
        const res = await buscaApi.json()
        return res;
    } catch (erro) {
        console.error("Erro capturado: " + erro)
    }
}


const userFind = {
    "nome": "Bruno Oliveira",
    "email": "bruno.oliveira@example.com"
}
minhaFuncaoAssincrona(userFind)
