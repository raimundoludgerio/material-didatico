// server.js
import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import { connectDB } from './config/database.js';

import authRoutes from './routes/authRoutes.js';
import userRoutes from './routes/userRoutes.js';
// Carrega variáveis de ambiente
dotenv.config();

// Conecta ao banco de dados
connectDB();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Rotas
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);

// Rota padrão
app.get('/', (req, res) => {
    res.json({
        message: 'API funcionando!',
        timestamp: new Date().toISOString()
    });
});

// Rota não encontrada
app.use('/*splat', (req, res) => {
    res.status(404).json({
        success: false,
        message: 'Rota não encontrada'
    });
});

// Middleware de erro - DEVE VIR DEPOIS DAS ROTAS
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        success: false,
        message: 'Erro interno do servidor'
    });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});