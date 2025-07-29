def extrair_prefixo(texto):
    return texto.strip().split()[0]  # Pega o "C6.", "C13.", etc.


def corrigir_exercicios_por_prefixo(gabarito, respostas):
    prefixos_gabarito = {extrair_prefixo(g) for g in gabarito}
    corretas = 0
    erradas = 0

    for resposta in respostas:
        prefixo = extrair_prefixo(resposta)
        print("Resposta usuário", prefixo)
        print(prefixos_gabarito)
        if prefixo in prefixos_gabarito:
            corretas += 1
        else:
            erradas += 1
        print(corretas)
        print(erradas)
    return {
        "corretas": corretas,
        "erradas": erradas
    }

GABARITO_CT = ["CT2. Input(25/03/2019, 26/03/2019) Output(140)", 
               "CT5. Input(25/03/2019, 03/04/2019) Output(1485)", 
               "CT6. Input(25/03/2019, 06/04/2019) Output(2210)",
                "CT8. Input(01/04/2019, 07/04/2019) Output(990)",
               "CT9. Input(25/03/2019, 28/03/2019) Output(420)", 
               "CT11. Input( cartao e 49 ) Output( 49.0 )", 
               "CT13. Input( cashback e 800 ) Output( 704.0 )", 
               "CT14. Input(25/03/2019-24/03/2019) Output(0)",
               "CT15. Input(cliente normal e -10) ArgumentoInvalidoException"]

GABARITO_CE =["C2. 3 < dataEntrega - dataFimContrato <= 10 (multa 65%)", 
              "C3. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%)",
               "C8. dataEntrega < 0 ou dataFimContrato < 0 (ArgumentoIlegalException)",
              "C10. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%)",
              "C5. dataEntrega - dataFimContrato > 10 (multa 65% + R$230)", 
              "C6. dataEntrega <= dataFimContrato (sem multa)", 
              "C9. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%)",
              "C12. dataEntrega = nulo (ArgumentoIlegalException)", 
              "C13. dataEntrega = nulo ou dataFimContrato = nulo (ArgumentoIlegalException)",
              "C14. dataEntrega = nulo = nulo ou dataFimContrato = nulo (ArgumentoIlegalException)"
]


RESPOSTA_DUPLA = "CT1. Input(25/03/2019-24/03/2019) Output(ArgumentoInvalidoException), CT2. Input(25/03/2019-26/03/2019) Output(140), CT5. Input(25/03/2019-03/04/2019) Output(1485), CT6. Input(25/03/2019-06/04/2019) Output(1650), CT7. Input(01/04/2019-06/04/2019) Output(500), CT8. Input(01/04/2019-07/04/2019) Output(990), CT9. Input(25/03/2019-28/03/2019) Output(420), CT11. Input(26/03/2019-06/04/2019) Output(2045), CT13.  Input(25/03/2019-34/03/2019) Output(ArgumentoInvalidoException), CT14. Input(25/03/2019-24/03/2019) Output(0), CT15. Input(25/03/2019-24/03/2019) Output(0)".split(',')


RESPOSTA_DUPLA_CE = "C3. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%), C4. 3 =< dataEntrega - dataFimContrato < 10 (multa 65%), C5. dataEntrega - dataFimContrato > 10 (multa 65% + R$230,00), C6. dataEntrega <= dataFimContrato (sem multa), C8. dataEntrega < 0 ou dataFimContrato < 0 (ArgumentoIlegalException), C10. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%), C12. dataEntrega - dataFimContrato >= 10 (multa 65% + R$230,00), C13. dataEntrega <= dataFimContrato (sem multa), C14. dataEntrega = nulo = nulo ou dataFimContrato = nulo (ArgumentoIlegalException)".split(',')


RESPOSTA_DUPLA_CT = [
    "C2. 3 < dataEntrega - dataFimContrato <= 10 (multa 65%)",
    "C5. dataEntrega - dataFimContrato > 10 (multa 65% + R$230)", 
    "C6. sem atraso (sem multa), C8. dataEntrega < 0 ou dataFimContrato < 0 (ArgumentoIlegalException)", 
    "C10. 0 < dataEntrega - dataFimContrato <= 3 (multa 40%)", 
    "C13. dataEntrega <= dataFimContrato (sem multa)", 
    "C14. dataEntrega = nulo = nulo ou dataFimContrato = nulo (ArgumentoIlegalException)"
]
print(corrigir_exercicios_por_prefixo(GABARITO_CE, RESPOSTA_DUPLA_CE))


print(RESPOSTA_DUPLA)