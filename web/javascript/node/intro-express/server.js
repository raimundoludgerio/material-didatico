import express from 'express';

const app = express();

app.get("/dashboard/:nome", (req, res) => {
    res.json({
        nome: req.params.nome
    });
});

app.listen(3000, () => {
    console.log("Meu servidor está on");
});