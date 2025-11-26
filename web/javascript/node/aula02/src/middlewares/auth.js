// middleware/authMiddleware.js
import jwt from 'jsonwebtoken';
import { User } from '../models/User.js';

// Middleware para proteger rotas
export const protect = async (req, res, next) => {
  try {
    let token;

    // Verifica se o token está no header
    if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
      token = req.headers.authorization.split(' ')[1];
    }

    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Acesso negado. Token não fornecido.'
      });
    }

    try {
      // Verifica o token
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      
      // Busca usuário pelo ID do token (sem a senha)
      req.user = await User.findById(decoded.id).select('-password');
      
      if (!req.user) {
        return res.status(401).json({
          success: false,
          message: 'Token inválido. Usuário não encontrado.'
        });
      }

      next();
    } catch (error) {
      return res.status(401).json({
        success: false,
        message: 'Token inválido.'
      });
    }
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Erro no servidor'
    });
  }
};

// Middleware para autorizar por roles
export const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        success: false,
        message: `Usuário com role ${req.user.role} não tem acesso a esta rota`
      });
    }
    next();
  };
};

