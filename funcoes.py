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

def calcula_pontos_regra_simples(dados_rolados):
    dicio = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    for dado in dados_rolados:
        if dado in dicio:
            dicio[dado] += dado

    return dicio

def calcula_pontos_soma(dados_rolados):
    soma=0
    for dado in dados_rolados:
        soma+=dado
    return soma

def calcula_pontos_sequencia_baixa(dados_rolados):
    for dado in dados_rolados:
        if dado in dados_rolados and dado+1 in dados_rolados and dado+2 in dados_rolados and dado+3 in dados_rolados:
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados_rolados):
    for dado in dados_rolados:
        if dado in dados_rolados and dado+1 in dados_rolados and dado+2 in dados_rolados and dado+3 in dados_rolados and dado+4 in dados_rolados:
            return 30
    return 0
        
def calcula_pontos_full_house(dados_rolados):
    i = 0
    trio = 0
    duo = 0
    soma=0
    while i < len(dados_rolados):
        j = 0
        contador = 0
        while j < len(dados_rolados):
            if dados_rolados[j] == dados_rolados[i]:
                contador += 1
            j += 1
        if contador == 3:
            trio = dados_rolados[i]
        elif contador == 2 and dados_rolados[i] != trio:
            duo = dados_rolados[i]
        soma+=dados_rolados[i]
        i += 1
    
    if trio != 0 and duo != 0:
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(dados_rolados):
    i=0
    soma=0
    quadra=0
    while i < len (dados_rolados):
        j=0
        contador=0
        while j<len(dados_rolados):
            if dados_rolados[i]==dados_rolados[j]:
                contador+=1
            j+=1
        if contador>3:
            quadra=1
        soma+=dados_rolados[i]
        i+=1
    if quadra==1:
        return soma
    else:
        return 0
    
def calcula_pontos_quina(dados_rolados):
    i=0
    quina=0
    while i < len(dados_rolados):
        j=0
        contador=0
        while j<len(dados_rolados):
            if dados_rolados[i]==dados_rolados[j]:
                contador+=1
            j+=1
        if contador>4:
            quina=1
        i+=1
    if quina==1:
        return 50
    else:
        return 0
    
def calcula_pontos_regra_avancada(dados_rolados):
    dicio={}
    dicio['cinco_iguais']=calcula_pontos_quina(dados_rolados)
    dicio['full_house']=calcula_pontos_full_house(dados_rolados)
    dicio['quadra']=calcula_pontos_quadra(dados_rolados)
    dicio['sem_combinacao']=calcula_pontos_soma(dados_rolados)
    dicio['sequencia_alta']=calcula_pontos_sequencia_alta(dados_rolados)
    dicio['sequencia_baixa']=calcula_pontos_sequencia_baixa(dados_rolados)
    return dicio




            
