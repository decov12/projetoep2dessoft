from funcoes import *

cartela = {
    "regra_simples": {i: -1 for i in range(1, 7)},
    "regra_avancada": {
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "full_house": -1,
        "quadra": -1,
        "cinco_iguais": -1,
        "sem_combinacao": -1
    }
}

rodadas = 0
while rodadas < 12:
    print(f"\n--- Rodada {rodadas + 1} ---")
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens_restantes = 2

    while True:
        print(f"\nDados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            entrada = input()
            if entrada.isdigit():
                idx = int(entrada)
                if 0 <= idx < len(dados_rolados):
                    resultado = guardar_dado(dados_rolados, dados_guardados, idx)
                    dados_rolados, dados_guardados = resultado
                else:
                    print("Índice inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            entrada = input()
            if entrada.isdigit():
                idx = int(entrada)
                if 0 <= idx < len(dados_guardados):
                    resultado = remover_dado(dados_rolados, dados_guardados, idx)
                    dados_rolados, dados_guardados = resultado
                else:
                    print("Índice inválido.")
            else:
                print("Entrada inválida.")

        elif opcao == '3':
            if rerrolagens_restantes > 0:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens_restantes -= 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            categoria = input()
            if categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] == -1:
                    faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    break
                else:
                    print("Essa combinação já foi utilizada.")
            elif categoria.isdigit():
                categoria_int = int(categoria)
                if categoria_int in cartela['regra_simples']:
                    if cartela['regra_simples'][categoria_int] == -1:
                        faz_jogada(dados_rolados + dados_guardados, categoria_int, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodadas += 1

print("\nFim do jogo! Cartela final:")
imprime_cartela(cartela)




