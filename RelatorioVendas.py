
""" 
    Relatório de Vendas
        ...
        O programa Relatório de Vendas tem como objetivo criar uma classe que execute comandos de entrada, armazenamento e tratamento de dados.
        Para sua execução, serão criadas funções para determinados comandos, de modo que sejam iteráveis entre sí.

        Recomenda-se usá-lo em sistemas de gestão de vendas e estoque.
"""

import re
import os
import csv
import locale


class RelatorioVendas:
    
    def __init__(self):
        """
            Dar início ao programa e todas as instâncias de classe criadas.
                ...
                Gerar um relatório de vendas como dicionário para armazenar os dados de venda inseridos.
        """
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        
        self.relatorio_de_vendas = {}


    def solicitar_vendas(self):
        """
            Gerar inputs ao usuário.
                ...
                O input 'produto' recebe o nome do produto.
                O input 'entrada' tem como propósito receber o valor de venda, filtrando apenas valores numéricos.

                Para os dois inputs criados, dar a opção de saída ao usuário ao inserir 'sair', retornando ao menu principal.
            
                
            Não exige parâmetros.
        """
        while True:
            produto = input("Insira o nome do produto (ou 'sair' para voltar ao menu): ").lower()
            if not produto:
                print("\nEntrada inválida. Insira o nome do produto.\n")
                print("-" * 40)
                print()
                continue
            if produto == "sair":
                return None
            while True:
                entrada = input("Insira o valor da venda (ou 'sair' para voltar ao menu): ").lower()
                if entrada == "sair":
                    return None
                try:
                    vendas = float(entrada)
                    if vendas <= 0:
                        print("\nEntrada inválida. O valor da venda deve ser positivo.\n")
                        print("-" * 40)
                        print()
                        continue
                    return produto, vendas
                except ValueError:
                    print("\nEntrada inválida. Digite um valor numérico.\n")
                    print("-" * 40)
                    print()
                

    def atualizar_dados(self, relatorio_de_vendas, vendedor, produto, vendas):
        """
            Atualizar os dados para cada valor inserido pelo usuário.
                ...
                Gerar um novo dicionário inserindo todos os dados ao novo vendedor usando uma estrutura if.
                Caso o vendedor já exista no relatório de vendas, inserir os dados e atualizar o dicionário do vendedor.

                
            Parâmetros: dicionário 'relatorio_de_vendas', nome do vendedor, nome do produto e valor das vendas.
        """
        if vendedor not in relatorio_de_vendas:
            relatorio_de_vendas[vendedor] = {
                "produtos": {produto},
                "quantidade_vendas": 1,
                "total_vendas": vendas
                }
            print(f"\nO vendedor {vendedor.title()} foi adicionado ao Relatório de Vendas.\n")
            print("-" * 40)
        else:
            self.relatorio_de_vendas[vendedor]["total_vendas"] += vendas
            self.relatorio_de_vendas[vendedor]["quantidade_vendas"] += 1
            self.relatorio_de_vendas[vendedor]["produtos"].add(produto)
            print(f"\nFoi adicionado o valor de R${vendas:.2f} ao Relatório de Vendas do vendedor {vendedor.title()}.\n")
            print("-" * 40)


    def remover_vendedor(self):
        """
            Gerar ao usuário a opção de remoção de um determinado vendedor do relatório de vendas.
                ...
                O input 'vendedor' recebe o nome do vendedor a ser removido do relatório de vendas.
                Caso o vendedor não exista no relarório de vendas, o programa exibe uma mensagem de alerta e retorna ao menu automaticamente.

                Para o input 'vendedor', dar a opção de saída ao usuário ao inserir 'sair', retornando ao menu principal.

                
            Não exige parâmetros.
        """
        if not self.relatorio_de_vendas:
            print("\nNão há registros no Relatório de Vendas.\n")
            print("-" * 40)
            return

        while True:
            vendedor = input("\nDigite o nome do vendedor a ser removido (ou 'sair' para voltar ao menu): ").lower()
            if vendedor == "sair":
                print("\nOperação cancelada. Voltando ao menu principal.\n")
                print("-" * 40)
                return None
            elif vendedor not in self.relatorio_de_vendas:
                print(f"\nO vendedor {vendedor.title()} não consta no Relatório de Vendas.\n")
                print("-" * 40)
                continue
            del self.relatorio_de_vendas[vendedor]
            print(f"\nO vendedor {vendedor.title()} foi removido do Relatório de Vendas.\n")
            print("-" * 40)


    def buscar_vendedor(self):
        """
            Gerar ao usuário a opção de busca por um vendedor no relatório de vendas.
                ...
                O input 'vendedor' recebe o nome do vendedor para consulta no relatório de vendas.
                Caso o vendedor não exista no relatório de vendas, o programa emite uma mensagem de alerta e retorna ao menu automaticamente.

                Para o input 'vendedor', dar a opção de saída ao usuário inserindo 'sair', retornando ao menu principal.

                A consulta irá exibir:
                    
                    Nome do Vendedor,
                    Quantidade de Vendas,
                    Valor Médio de Vendas,
                    Valor Total de Vendas,
                    Nome dos Produtos Vendidos.

                    
            Não exige parâmetros.
        """
        if not self.relatorio_de_vendas:
            print("\nNão há registros no Relatório de Vendas.\n")
            print("-" * 40)
            return

        while True:
            vendedor = input("\nDigite o nome do vendedor para fazer uma consulta (ou 'sair' para voltar ao menu): ").lower()
            if vendedor == "sair":
                print("\nOperação cancelada. Voltando ao menu principal.\n")
                print("-" * 40)
                return None
            elif vendedor not in self.relatorio_de_vendas:
                print(f"\nO vendedor {vendedor.title()} não consta no Relatório de Vendas.\n")
                print("-" * 40)
                continue

            print(f"\n -- Dados do vendedor {vendedor.title()} --\n")

            print(f"{'Vendedor':<25}{'Qtde Vendas':<19}{'Valor Médio':<20}{'Venda Total':<20}{'Produtos':<30}")
            print("-" * 100)

            dados = self.relatorio_de_vendas[vendedor]
            produtos = ', '.join(sorted(dados["produtos"]))
            quantidade_vendas = dados["quantidade_vendas"]
            total_vendas = dados["total_vendas"]
            media_vendas = total_vendas / quantidade_vendas

            media_formatada = locale.format_string("%.2f", media_vendas, grouping=True)
            total_formatado = locale.format_string("%.2f", total_vendas, grouping=True)

            print(f"{vendedor.title():<19}{"|":<4}{quantidade_vendas:>13}{"|":>4}{media_formatada:>15}{"|":>5}{total_formatado:>15}{"|":>5}    {produtos.title():<30}")
            print("-" * 100)


    def exibir_relatorio(self):
        """
            Gerar ao usuário a opção de exibição do relatório de vendas.
                ...
                Para cada vendedor no relatório de vendas, será exibido:
                    
                    Nome do Vendedor,
                    Quantidade de Vendas,
                    Valor Médio de Vendas,
                    Valor Total de Vendas,
                    Nome dos Produtos Vendidos.

                    
            Não exige parâmetros.
        """
        if not self.relatorio_de_vendas:
            print("\nNão há registros no Relatório de Vendas.\n")
            print("-" * 40)
            return

        print("\n-- Relatório de Vendas --\n")

        print(f"{'Vendedor':<25}{'Qtde Vendas':<19}{'Valor Médio':<20}{'Venda Total':<20}{'Produtos':<30}")
        print("-" * 100)

        for vendedor, dados in self.relatorio_de_vendas.items():
            produtos = ', '.join(sorted(dados["produtos"]))
            quantidade_vendas = dados["quantidade_vendas"]
            total_vendas = dados["total_vendas"]
            media_vendas = total_vendas / quantidade_vendas

            media_formatada = locale.format_string("%.2f", media_vendas, grouping=True)
            total_formatado = locale.format_string("%.2f", total_vendas, grouping=True)

            print(f"{vendedor.title():<19}{"|":<4}{quantidade_vendas:>13}{"|":>4}{media_formatada:>15}{"|":>5}{total_formatado:>15}{"|":>5}    {produtos.title():<30}")
            print("-" * 100)


    def exportar_relatorio_csv(self):
        """
            Exportar o Relatório de Vendas para um arquivo CSV.
                ...
                Será gerado um arquivo CSV com as colunas: 
                'Vendedor', 'Produto Vendido', 'Valor do Produto'.

            
            Não exige parâmetros.
        """
        if not self.relatorio_de_vendas:
            print("\nNão há registros no Relatório de Vendas.\n")
            print("-" * 40)
            return

        try:
            caminho_arquivo = r"C:\Users\Rufinissimo\Documents\Cursos\Hashtag Treinamentos\Python\Python Impressionador\Projetos\Sistemas\Relatório de Vendas\relatorio_vendas.csv"
            
            with open(caminho_arquivo, mode="w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(["Vendedor", "Produto Vendido", "Valor do Produto"])
                for vendedor, dados in self.relatorio_de_vendas.items():
                    for produto in dados["produtos"]:   
                        valor_venda = dados["total_vendas"]
                        valor_formatado = f"R$ {valor_venda:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")
                        writer.writerow([vendedor.title(), produto.title(), valor_formatado])
            
            print(f"\nRelatório de Vendas exportado com sucesso para: {os.path.abspath(caminho_arquivo)}.\n")
            print("-" * 40)

        except Exception as e:
            print(f"\nErro ao exportar o relatório: {e}\n")
            print("-" * 40)


    def sair_menu(self):
        """
            Gerar ao usuário a opção de encerramento do programa.
                ...
                O input 'sair' recebe a resposta do usuário; 'sim' para encerrar o programa ou 'nao' para continuar.

                
            Não exige parâmetros.
        """
        while True:
            sair = input("\nDeseja encerrar a consulta? (sim/nao): ").lower()
            if sair == "sim":
                print("\nObrigado! Até a próxima consulta.\n")
                return True
            elif sair == "nao":
                print()
                print("-" * 40)
                return False
            else:
                print("\nEntrada inválida. Digite 'sim' para encerrar ou 'nao' pra continuar.\n")
                print("-" * 40)


    def main(self):
        """
            Função principal do programa.
                ...
                Gerar ao usuário um menu exibindo cada opção de escolha.

                Para cada opção, executar o determinado comando relacionado às funções criadas:
                    
                    Opção 1 (Adicionar venda):
                        ...
                        O programa irá executar os comandos criados na função solicitar_vendas().
                        Para o input 'vendedor', não serão aceitos caracteres especiais.
                        Caso o vendedor inserido já exista no relatório de vendas, a função atualizar_dados() será usada para atualizar o dicionário do vendedor.
                        
                    Opção 2 (Remover vendedor):
                        ...
                        O programa irá executar os comandos criados na função remover_vendedor().
                        Caso o relatório de vendas esteja vazio ou não conste o vendedor, o programa irá exibir uma mensagem de alerta e retornar ao menu automaticamente.
                        
                    Opção 3 (Consultar vendedor):
                        ...
                        O programa irá executar os comandos criados na função buscar_vendedor().
                        Caso o relatório de vendas esteja vazio ou não conste o vendedor, o programa irá exibir uma mensagem de alerta e retornar ao menu automaticamente.
                        
                    Opção 4 (Exibir o Relatório de Vendas):
                        ...
                        O programa irá executar os comandos criados na função exibir_relatório().
                        Caso o relatório de vendas esteja vazio, o programa irá exibir uma mensagem de alerta e retornar ao menu automaticamente.

                    Opção 5 (Exportar o Relatório para CSV):
                        ...
                        O programa irá exportar o relatório de vendas para um arquivo csv.    

                    Opção 6 (Sair):
                        ...
                        O programa irá executar os comandos criados na função sair().              

                Caso o usuário insira um valor diferente das opções de escolhas, o programa irá exibir uma mensagem de alerta e retornar ao menu automaticamente.  

                
            Não exige parâmetros.      
        """
        print("\nRelatório de Vendas")

        while True:
            print("\n1 - Adicionar venda")
            print("2 - Remover vendedor")
            print("3 - Consultar vendedor")
            print("4 - Exibir o Relatório de Vendas")
            print("5 - Exportar o Relatório para CSV")
            print("6 - Sair")

            escolha = input("\nEscolha uma opção: ")

            if escolha.isdigit() and 1 <= int(escolha) <= 6:
                escolha = int(escolha)

                if escolha == 1:
                    while True:
                        vendedor = input("\nDigite o nome do vendedor (ou 'sair' para voltar ao menu): ").lower()
                        if not re.match("^[a-záàâãéèêíïóôõöúçñ0-9 -]+$", vendedor):
                            print("\nEntrada inválida. Insira o nome do vendedor sem caracteres especiais.\n")
                            print("-" * 40)
                            continue
                        elif vendedor == "sair":
                            print("\nOperação cancelada. Voltando ao menu principal.\n")
                            print("-" * 40)
                            break
                        vendas_info = self.solicitar_vendas()
                        if vendas_info is None:
                            print("\nOperação cancelada. Voltando ao menu principal.\n")
                            print("-" * 40)
                            break
                        produto, vendas = vendas_info
                        self.atualizar_dados(self.relatorio_de_vendas, vendedor, produto, vendas)

                elif escolha == 2:
                    self.remover_vendedor()

                elif escolha == 3:
                    self.buscar_vendedor()

                elif escolha == 4:
                    self.exibir_relatorio()

                elif escolha == 5:
                    self.exportar_relatorio_csv()

                elif escolha == 6:
                    if self.sair_menu():
                        break
                    
            else:
                print("\nEntrada inválida. Tente novamente inserindo um valor de 1 a 6.\n")
                print("-" * 40)


if __name__ == "__main__":
    relatorio = RelatorioVendas()
    relatorio.main()