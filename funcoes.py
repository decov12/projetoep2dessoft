import random
def rolar_dados(n):
    lista=[]
    i=0
    while i < n:
        numero=random.randint(1,6)
        lista.append(numero)
        i+=1
    return lista

def guardar_dado(dados_rolados,dados_guardados,dado_para_guardar):
    for i in range (len(dados_rolados)):
        if dado_para_guardar==dados_rolados[i]:
            dados_guardados.append(dado_para_guardar)
    return dados_guardados

