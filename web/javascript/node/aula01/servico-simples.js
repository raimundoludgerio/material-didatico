import http from 'http';

let users = [
    { id: 1, name: 'João' },
    { id: 2, name: 'Maria' },
    { id: 3, name: 'Antônio' },
    { id: 4, name: 'Carlos' }
];

const server = http.createServer((req, res) => {
    // GET /users
    if (req.url === '/users' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(users));
    }
    
    // GET /users/1
    else if (req.url.match(/\/users\/([0-9]+)/) && req.method === 'GET') {
        const id = parseInt(req.url.split('/')[2]);
        const user = users.find(u => u.id === id);
        
        if (user) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(user));
        } else {
            res.writeHead(404);
            res.end('Usuário não encontrado');
        }
    }
    
    // POST /users
    else if (req.url === '/users' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => body += chunk.toString());
        req.on('end', () => {
            const newUser = { id: users.length + 1, ...JSON.parse(body) };
            users.push(newUser);
            res.writeHead(201, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(newUser));
        });
    }
    
    // Rota não encontrada
    else {
        res.writeHead(404);
        res.end('Rota não encontrada');
    }
});

server.listen(3000);