import express from 'express';

const app = express();

app.get("/dashboard/", (req, res) => {
    const nome = req.query.nome;
    res.send(`
        <script> alert("olá") </script>
        <h1> Olá, ${nome}. Seja bem vindo! </h1>    
    `);
});

app.listen(3000, () => {
    console.log("Meu servidor está on");
});