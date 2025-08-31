import unittest
import desafios_a as desafios


class TesteFuncoes(unittest.TestCase):

    def test_ola_mundo(self):
        self.assertEqual(desafios.ola_mundo(), "Olá, Mundo!")

    def test_saudacao(self):
        self.assertEqual("Olá, João! Seja bem-vindo(a).", desafios.saudacao("João"))
        self.assertEqual(desafios.saudacao("Maria"), "Olá, Maria! Seja bem-vindo(a).")

    def test_dobro(self):
        self.assertEqual(desafios.dobro(5), 10)
        self.assertEqual(desafios.dobro(-3), -6)
        self.assertEqual(desafios.dobro(0), 0)

    def test_media(self):
        self.assertEqual(desafios.media(5, 7, 9), 7.0)
        self.assertEqual(desafios.media(10, 10, 10), 10.0)
        self.assertEqual(desafios.media(0, 0, 0), 0)

    def test_maior_de_idade(self):
        self.assertTrue(desafios.maior_de_idade(18))
        self.assertFalse(desafios.maior_de_idade(17))
        self.assertFalse(desafios.maior_de_idade(0))

    def test_contador(self):
        self.assertEqual(desafios.contador(1, 10, 2), [1, 3, 5, 7, 9])
        self.assertEqual(desafios.contador(0, 5, 1), [0, 1, 2, 3, 4])
        self.assertEqual(desafios.contador(10, 0, -2), [10, 8, 6, 4, 2])

    def test_somar_lista(self):
        self.assertEqual(desafios.somar_lista([1, 2, 3]), 6)
        self.assertEqual(desafios.somar_lista([-1, -2, -3]), -6)
        self.assertEqual(desafios.somar_lista([]), 0)

    def test_analisar_texto(self):
        self.assertEqual(desafios.analisar_texto("Python é incrível!"), ("Python é incrível!", 20, 3))
        self.assertEqual(desafios.analisar_texto("Olá, Mundo!"), ("Olá, Mundo!", 12, 2))
        self.assertEqual(desafios.analisar_texto(""), ("", 0, 0))

    def test_palindromo(self):
        self.assertTrue(desafios.palindromo("arara"))
        self.assertFalse(desafios.palindromo("python"))
        self.assertTrue(desafios.palindromo("radar"))

    def test_ordem_crescente(self):
        self.assertEqual(desafios.ordem_crescente(3, 1, 2), [1, 2, 3])
        self.assertEqual(desafios.ordem_crescente(5, 4, 6), [4, 5, 6])
        self.assertEqual(desafios.ordem_crescente(10, 20, 15), [10, 15, 20])

    def test_inverte_texto(self):
        self.assertEqual(desafios.inverte_texto("Python"), "nohtyP")
        self.assertEqual(desafios.inverte_texto("Olá"), "álO")
        self.assertEqual(desafios.inverte_texto(""), "")

    def test_media_varios(self):
        self.assertEqual(desafios.media(5, 10, 15), 10.0)
        self.assertEqual(desafios.media(1, 2, 3, 4, 5), 3.0)
        self.assertEqual(desafios.media(), 0.0)

    def test_numero_maior(self):
        self.assertEqual(desafios.numero_maior(1, 2, 3), 3)
        self.assertEqual(desafios.numero_maior(10, 5, 8), 10)
        self.assertEqual(desafios.numero_maior(-1, -2, -3), -1)

    def test_fatorial(self):
        self.assertEqual(desafios.fatorial(5), 120)
        self.assertEqual(desafios.fatorial(0), 1)
        self.assertEqual(desafios.fatorial(1), 1)
        self.assertEqual(desafios.fatorial(3), 6)


if __name__ == '__main__':
    unittest.main()
