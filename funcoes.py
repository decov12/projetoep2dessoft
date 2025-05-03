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
    dados_guardados.append(dados_rolados[dado_para_guardar])
    del dados_rolados[dado_para_guardar]
    resultado=[]
    resultado.append(dados_rolados)
    resultado.append(dados_guardados)
    return resultado

def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]
    resultado=[]
    resultado.append(dados_rolados)
    resultado.append(dados_no_estoque)
    return resultado