import http from 'http';
// Fazendo uma requisição GET
const options = {
    hostname: 'jsonplaceholder.typicode.com',
    port: 80,
    path: '/posts/1',
    method: 'GET'
};

const req = http.request(options, (res) => {
    let data = '';
    res.on('data', (chunk) => {
        data += chunk;
    });
    res.on('end', () => {
        console.log('Resposta:', JSON.parse(data));
    });
});
req.on('error', (error) => {
    console.error('Erro:', error);
});
req.end();

const http = require('http');

const express = require('express');

const app = express();

// ROTEAMENTO SIMPLES E INTUITIVO
app.get('/users', (req, res) => {
    // Lógica para GET /users
});

app.post('/users', (req, res) => {
    // Lógica para POST /users
});

app.get('/users/:id', (req, res) => {
    // Lógica para GET /users/:id
});