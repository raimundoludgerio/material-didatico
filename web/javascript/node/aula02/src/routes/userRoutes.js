// routes/userRoutes.js
import express from 'express';
import {
  getUsers,
  getUser,
  updateUser,
  deleteUser
} from '../controllers/userController.js';
import { protect, authorize } from '../middlewares/auth.js';

const router = express.Router();

// Todas as rotas protegidas
router.use(protect);

router.get('/', getUsers);
router.get('/:id', authorize('admin'), getUser);
router.put('/:id', updateUser); // Usuário pode atualizar próprio perfil
router.delete('/:id', authorize('admin'), deleteUser);

export default router;