nome_qualquer = "Raimundo"
print(nome_qualquer.encode("utf-8"))
deslocamento = 3
resultado = ""
for char in nome_qualquer:
    if char.isalpha():  # Verifica se é uma letra
        # Pega o código ASCII da letra, adiciona o deslocamento e aplica o módulo 26
        # (123 para 'a' minúsculo, 65 para 'A' maiúsculo)
        codigo_base = ord('a') if char.islower() else ord('A')
        codigo_cifrado = (ord(char) - codigo_base + deslocamento) % 26 + codigo_base
        resultado += chr(codigo_cifrado)
    else:
        resultado += char  # Mantém caracteres não alfabéticos

print(resultado)