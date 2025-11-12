import express from "express";

const app = express();

// Rota básica
app.get('/', (req, res) => {
    res.send('Olá Mundo com Express!');
});

// Query parameters
app.get('/search', (req, res) => {
    res.json({
        query: req.query.nome,
    });
});




// Parâmetros de rota
app.get('/users/:userId', (req, res) => {
    res.json({
        userId: req.params.userId
    });
});




app.listen(3000, () => {
  console.log("Servidor rodando na porta 3000");
});