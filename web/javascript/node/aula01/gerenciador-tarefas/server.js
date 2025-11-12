import express from 'express';
const app = express();
const port = 3003;

// Middleware para permitir JSON no corpo das requisições
app.use(express.json());

// Banco de dados em memória (array)
let tarefas = [
    { id: 1, titulo: "Estudar Node.js", concluida: false },
    { id: 2, titulo: "Ler sobre Express", concluida: true }
];

app.get('', (req, res) => {
    res.send('Todas as tarefas serão listadas aqui.');
});

app.get('/tarefas', (req, res) => {
    res.json(tarefas);
});

app.post('/tarefas', (req, res) => {
    const { titulo } = req.body;
    const novaTarefa = {
        id: tarefas.length + 1,
        titulo,
        concluida: false
    };
    tarefas.push(novaTarefa);
    res.status(201).json(novaTarefa);
});

app.put('/tarefas/:id', (req, res) => {
    const { id } = req.params;
    const { titulo, concluida } = req.body;
    const tarefa = tarefas.find(t => t.id === parseInt(id));

    if (!tarefa) return res.status(404).json({ erro: "Tarefa não encontrada" });

    tarefa.titulo = titulo ?? tarefa.titulo;
    tarefa.concluida = concluida ?? tarefa.concluida;

    res.json(tarefa);
});

app.delete('/tarefas/:id', (req, res) => {
    const { id } = req.params;
    tarefas = tarefas.filter(t => t.id !== parseInt(id));
    res.status(204).send();
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
