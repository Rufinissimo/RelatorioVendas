
""" Relatório Básico de Vendas """

import re
    
def solicitar_vendas():
    while True:
        entrada = input("Insira o valor da venda (ou 'sair' para voltar ao menu): ").lower()
        if entrada == "sair":
            return None 
        try:
            vendas = float(entrada)
            return vendas
        except ValueError:
            print("\nEntrada inválida. Digite um valor numérico ou 'sair' para voltar ao menu.\n")
            continue

def atualizar_dados(relatorio_de_vendas, vendedor, vendas):
    if vendedor not in relatorio_de_vendas:
        relatorio_de_vendas[vendedor] = {"total_vendas": vendas, "quantidade_vendas": 1} # Se o vendedor não consta no dicionário, irá adiciona-lo, assim como uma chave para os valores de vendas (total_vendas) e uma chave para a quantidade de vendas (quantidade_vendas).
        print(f"\nO vendedor {vendedor.title()} foi adicionado ao Relatório de Vendas.\n")
    else:
        relatorio_de_vendas[vendedor]["total_vendas"] += vendas # Se o vendedor consta no relatório, irá adicionar o valor de venda inserido na chave de vendas (total_vendas) do vendedor.
        relatorio_de_vendas[vendedor]["quantidade_vendas"] += 1 # ... da mesma forma, irá adicionar 1 venda a mais na chave de quantidade de vendas (quantidade_vendas).
        print(("\nFoi adicionado o valor de R${:,.2f} ao Relatório de Vendas do vendedor {}.\n").format(vendas, vendedor.title()).replace(",", "."))

def remover_vendedor(relatorio_de_vendas):
    while True:
        vendedor = input("\nDigite o nome do vendedor a ser removido do Relatório de Vendas (ou 'sair' para voltar ao menu): ").lower()
        if vendedor == "sair":
            break
        if vendedor not in relatorio_de_vendas:
            print(f"\nO vendedor {vendedor.title()} não consta no Relatório de Vendas.\n")
            continue
        try:
            if vendedor in relatorio_de_vendas:
                del relatorio_de_vendas[vendedor]
                print(f"\nO vendedor {vendedor.title()} foi removido do Relatório de Vendas.\n")
        except KeyError:
            print(f"\nErro ao tentar remover o vendedor {vendedor.title()}. Tente novamente.")

def buscar_vendedor(relatorio_de_vendas):
    while True:
        vendedor = input("\nDigite o nome do vendedor para fazer uma consulta (ou 'sair' para voltar ao menu): ").lower()
        if vendedor == "sair":
            break
        if vendedor not in relatorio_de_vendas:
            print(f"\nO vendedor {vendedor.title()} não consta no Relatório de Vendas.\n")
            continue
        dados = relatorio_de_vendas[vendedor]
        print(f"\nVendedor: {vendedor.title()}")
        print(f"Total de Vendas: R${dados['total_vendas']:.2f}".replace(",", "."))
        print(f"Quantidade de Vendas: {dados['quantidade_vendas']}\n")

def exibir_relatorio(relatorio_de_vendas):
    print("\n-- Relatório de Vendas --\n")
    for vendedor, dados in relatorio_de_vendas.items(): # Determinar "dados" como argumento para importar os valores das chaves total_vendas e quantidade_vendas.
        total_vendas = dados["total_vendas"]
        quantidade_vendas = dados["quantidade_vendas"]
        media_vendas = total_vendas / dados["quantidade_vendas"]
        print(f"Vendedor: {vendedor.title()}\nVenda Total: R${total_vendas:,.2f}\nValor Médio: R${media_vendas:,.2f}\nQuantidade de Vendas: {quantidade_vendas}\n".replace(",", "."))

def sair_menu():
    while True:
        sair = input("\nDeseja encerrar a consulta? (sim/nao): ").lower()
        if sair == "sim":
            print("\nObrigado! Até a próxima consulta.\n")
            return True
        if sair == "nao":
            return False
        else:
            print("\nEntrada inválida. Digite 'sim' para encerrar ou 'nao' pra continuar.\n")
            continue

def main():
    print("\nRelatório de Vendas")

    relatorio_de_vendas = {}
    vendedor = None
    vendas = 0

    while True:
        print("\n1 - Adicionar venda")
        print("2 - Remover vendedor")
        print("3 - Consultar um vendedor")
        print("4 - Exibir o Relatório de Vendas")
        print("5 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha.isdigit() and 1 <= int(escolha) <= 5:
            escolha = int(escolha)
            if escolha == 1:
                while True:
                    vendedor = input("\nDigite o nome do vendedor (ou 'sair' para voltar ao menu): ").lower()
                    if not re.match("^[a-záàâãéèêíïóôõöúçñ0-9 -]+$", vendedor):
                        print("\nEntrada inválida. Insira o nome do vendedor sem caracteres especiais.")
                        continue
                    if vendedor == "sair":
                        break
                    vendas = solicitar_vendas()
                    if vendas is None:
                        print("\nOperação cancelada. Voltando ao menu principal.\n")
                        break
                    atualizar_dados(relatorio_de_vendas, vendedor, vendas)
            elif escolha == 2:
                if not relatorio_de_vendas:
                    print("\nNão há registros no Relatório de Vendas.\n")
                    continue
                remover_vendedor(relatorio_de_vendas)
            elif escolha == 3:
                if not relatorio_de_vendas:
                    print("\nNão há registros no Relatório de Vendas.\n")
                    continue
                buscar_vendedor(relatorio_de_vendas)
            elif escolha == 4:
                if not relatorio_de_vendas:
                    print("\nNão há registros no Relatório de Vendas.\n")
                    continue
                exibir_relatorio(relatorio_de_vendas)
            elif escolha == 5:
                print("\nObrigado! Até a próxima consulta.\n")
                break
        else:
            print("\nEntrada inválida. Tente novamente inserindo um valor de 1 a 5.\n")

if __name__ == "__main__":
    main()
