import http from 'http';

const server = http.createServer((req, res) => {
    if (req.url === '/home') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <html>
                <head><title>Meu Site</title></head>
                <body>
                    <h1>Bem-vindo!</h1>
                    <p>Servido com HTTP nativo</p>
                </body>
            </html>
        `);
    }
    // Configurar cabeçalhos
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('X-Powered-By', 'Node.js');
    // Status code
    res.statusCode = 200;
    // Escrever resposta
    res.write(JSON.stringify({ message: 'Sucesso' }));
    // Finalizar
    res.end();
});

server.listen(3000, () => {
    console.log('Servidor rodando...');
});
