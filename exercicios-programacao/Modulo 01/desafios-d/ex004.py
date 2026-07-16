"""
    Leia as notas da 1ª e 2ª avaliações de um aluno.
    Calcule a média aritmética simples e
    exiba uma mensagem informando se o aluno foi aprovado ou reprovado.
    Além disso, mostre a média calculada.

    Solução desenvolvida por: Jeiciely Hardman Soare
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
resultado = "Aprovado." if media >= 7 else "Reprovado."
print(f"Sua média final foi {media} e você foi {resultado}")