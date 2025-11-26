import express from 'express';
const server = express();
const users = []

server.use(express.json())

server.get('/', (req, res) => {
    res.send('Hello, world!');
});

server.post("/users", (req, res) => {
    const user = { id: users.length + 1, ...req.body }
    console.log(user)
    res.status(201).json(user);
    users.push(user);
});

server.get("/users/:id", (req, res) => {
    const { id } = req.params
    const user = users.find(u => u.id == id)
    if (user) res.json(user)
    else res.status(404).send("Usuário não encontrado")
})

server.get("/users", (req, res) => {
    const { q } = req.query;
    const usuarios = users.filter(u => u.nome.includes(q))
    if (usuarios.length > 0) res.json(usuarios)
    res.json(users);
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
