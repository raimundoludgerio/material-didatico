import http from 'http'

const server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "text/json");
    res.write(JSON.stringify({
        name: "Marcos"
    }));
    res.end();
});


server.listen(3001, ()=>{
    console.log("Servidor rodando na porta 3001");
});
