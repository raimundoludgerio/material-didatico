# Material de Aula: JavaScript Backend com Node.js

---
header: 'Aula de JavaScript Backend com Node.js'
footer: '© 2023 - Professor Raimundo'
---

# História e Definição do Node.js

## O que é Node.js?

- Ambiente de execução JavaScript no lado do servidor
- Construído no motor V8 do Chrome
- Modelo event-driven e non-blocking I/O
- Permite JavaScript no backend

---

## História do Surgimento

- **2009**: Criado por Ryan Dahl
- **Inspiração**: Servidor de upload de arquivos do Flickr
- **Problema**: Espera do upload bloqueava todo o processo
- **Solução**: Modelo não-bloqueante com callbacks
- **2010**: NPM (Node Package Manager) lançado
- **2015**: Node.js Foundation criada

---

# Primeiros Passos: Node.js sem Express

## Criando um Servidor HTTP Básico

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Página Inicial</h1>');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Página não encontrada');
  }
});

server.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});
```

## História e Definição do Node.js

### O Que é Node.js?
- **Ambiente de execução JavaScript** no lado do servidor
- **Construído no motor V8** do Chrome (Google)
- **Event-driven** e **non-blocking I/O**
- **Permite JavaScript no backend**

### História do Surgimento
- **2009**: Criado por **Ryan Dahl**
- **Inspiração**: Servidor de upload de arquivos do Flickr
- **Problema**: Espera do upload bloqueava todo o processo
- **Solução**: Modelo não-bloqueante com callbacks
- **2010**: NPM (Node Package Manager) lançado
- **2015**: Node.js Foundation criada

---

## Primeiros Passos: Aplicação Node.js sem Express

### Criando um Servidor HTTP Básico

```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>Meu Primeiro Servidor Node.js!</h1>');
    } else if (req.url === '/api/users') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify([{ id: 1, name: 'João' }]));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Página não encontrada');
    }
});

server.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
```

### Executando a Aplicação
```bash
node server.js
```

---

## Introdução ao Express.js

### O Que é Express?
- **Framework web** mínimo e flexível para Node.js
- **Facilita criação** de aplicações web e APIs
- **Sistema de rotas** robusto
- **Middleware** para funcionalidades extras

### Vantagens do Express
- ✅ Simplicidade e flexibilidade
- ✅ Grande ecossistema
- ✅ Comunidade ativa
- ✅ Curva de aprendizado suave

---

## Exemplo de Aplicação com Express

### Estrutura do Projeto
```
meu-projeto/
├── package.json
├── server.js
└── routes/
    └── users.js
```

### server.js
```javascript
const express = require('express');
const userRoutes = require('./routes/users');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use('/users', userRoutes);

app.get('/', (req, res) => {
    res.send('<h1>Bem-vindo ao Express!</h1>');
});

app.listen(PORT, () => {
    console.log(`Servidor Express rodando na porta ${PORT}`);
});
```

### routes/users.js
```javascript
const express = require('express');
const router = express.Router();

let users = [
    { id: 1, name: 'João', email: 'joao@email.com' },
    { id: 2, name: 'Maria', email: 'maria@email.com' }
];

router.get('/', (req, res) => {
    res.json(users);
});

router.get('/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) return res.status(404).send('Usuário não encontrado');
    res.json(user);
});

module.exports = router;
```

---

## Próximos Passos no Aprendizado

### 1. **Conceitos de Middleware**
- \`app.use()\` para middleware global
- Middleware de terceiros
- Criar middleware customizado

### 2. **Template Engines**
- EJS, Pug, Handlebars
- Renderização no servidor

### 3. **Banco de Dados**
- MongoDB com Mongoose
- PostgreSQL com Sequelize
- MySQL

### 4. **Autenticação & Autorização**
- JWT (JSON Web Tokens)
- Sessions
- OAuth

### 5. **APIs RESTful**
- CRUD completo
- Validação de dados
- Paginação e filtros

### 6. **Segurança**
- Helmet.js
- CORS
- Rate limiting

### 7. **Deploy & DevOps**
- Docker
- PM2
- Deploy na nuvem

### 8. **Testes**
- Jest
- Supertest
- Testes unitários e de integração

---

## Recursos Recomendados

### Documentação Oficial
- [Node.js Documentation](https://nodejs.org/docs/)
- [Express.js Guide](https://expressjs.com/)

### Ferramentas Úteis
- **Nodemon**: Reinício automático
- **Postman**: Teste de APIs
- **VS Code**: Editor recomendado

### Boas Práticas
- Estrutura escalável
- Variáveis de ambiente
- Logging apropriado
- Tratamento de erros
- Código modular

---
*Material para aula de JavaScript Backend - Node.js e Express*