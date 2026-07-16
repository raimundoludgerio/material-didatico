import http from 'http';


let users = [
    { id: 1, name: 'João' },
    { id: 2, name: 'Maria' },
    { id: 3, name: 'Antônio' },
    { id: 4, name: 'Carlos' }
];

const server = http.createServer((req, res) => {
    if (req.url === '/cadastro') {
        return res.end(`
                <html>
                    <head>
                        <title>Cadastro</title>
                        <meta charset="UTF-8">
                    </head>
                    <body>
                        <h1>Formulário de Cadastro</h1>
                        <form action="/cadastro" method="post">
                            <label for="nome">Nome:</label><br>
                            <input type="text" id="nome" name="nome"><br><br>
                            <input type="submit" value="Enviar">
                        </form>
                    </body> 
                </html>
            `);
    } else if (req.url.match(/\/users\/([0-9]+)/) && req.method === 'GET') {
        const id = parseInt(req.url.split('/')[2]);
        const user = users.find(u => u.id === id);
        if (user) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(user));
        } else {
            res.writeHead(404);
            res.end('Usuário não encontrado');
        }
    } else {
        res.end(`
            <html>
                <head>
                    <title>Servidor Node.js</title>
                    <meta charset="UTF-8">
                </head>
                <body>
                    <h1>Olá, mundo!</h1>
                    <p>Este é um servidor básico usando Node.js.</p>
                </body> 
            </html>
        `);
    }
});

server.listen(3001, () => {
    console.log('Servidor rodando em http://localhost:3000');
});