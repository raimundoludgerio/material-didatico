import express from 'express';
import cors from 'cors';
const server = express()

server.use(cors())

server.get("/", (req, res) => {
    res.send("<h1> Oiii </h1>");
})

server.post("/cadastrar", async (req, res) => {
    const usuario = await req.body;
    console.log(req.query.search)
    return res.json({
        mensagem: "Usuário cadastrado"
    })
})
server.get("/cadastrar", (req, res) => {
    const usuario = req.body;
    console.log(usuario)
})

server.listen(5000, () => {
    console.log("Servidor executando na porta 5000")
});