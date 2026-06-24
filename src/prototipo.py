"""
Ia-Vet-Doc
Protótipo inicial para organização e consulta simples de documentos veterinários.

Este script demonstra uma primeira versão do fluxo:
1. Receber um documento veterinário fictício;
2. limpar e organizar o texto;
3. dividir o conteúdo em trechos;
4. buscar trechos relacionados a uma pergunta ou palavra-chave;
5. exibir resultados encontrados.

Nesta versão inicial, o projeto ainda não usa API externa nem banco vetorial.
A busca é feita por palavras-chave para simular a etapa de recuperação de contexto.
"""


def limpar_texto(texto):
    """
    Remove espaços excessivos e organiza quebras de linha.
    """
    linhas = texto.splitlines()
    linhas_limpas = []

    for linha in linhas:
        linha = linha.strip()
        if linha:
            linhas_limpas.append(linha)

    return "\n".join(linhas_limpas)


def dividir_em_trechos(texto, tamanho_maximo=400):
    """
    Divide o texto em trechos menores com base em um tamanho máximo aproximado.
    """
    palavras = texto.split()
    trechos = []
    trecho_atual = []

    tamanho_atual = 0

    for palavra in palavras:
        tamanho_atual += len(palavra) + 1
        trecho_atual.append(palavra)

        if tamanho_atual >= tamanho_maximo:
            trechos.append(" ".join(trecho_atual))
            trecho_atual = []
            tamanho_atual = 0

    if trecho_atual:
        trechos.append(" ".join(trecho_atual))

    return trechos


def buscar_trechos(trechos, termos_busca):
    """
    Busca trechos que contenham pelo menos um dos termos informados.
    """
    resultados = []

    for indice, trecho in enumerate(trechos, start=1):
        trecho_minusculo = trecho.lower()

        for termo in termos_busca:
            if termo.lower() in trecho_minusculo:
                resultados.append({
                    "trecho": indice,
                    "termo_encontrado": termo,
                    "conteudo": trecho
                })
                break

    return resultados


def exibir_resultados(resultados):
    """
    Exibe os resultados encontrados de forma organizada.
    """
    if not resultados:
        print("Nenhum trecho relacionado foi encontrado.")
        return

    print("\nTrechos relacionados encontrados:\n")

    for resultado in resultados:
        print(f"Trecho {resultado['trecho']}")
        print(f"Termo encontrado: {resultado['termo_encontrado']}")
        print(f"Conteúdo: {resultado['conteudo']}")
        print("-" * 80)


if __name__ == "__main__":
    documento_ficticio = """
    Paciente canina, fêmea, 9 anos, em acompanhamento por alterações urinárias.
    Tutor relata aumento da frequência urinária, urina com odor mais forte e discreto desconforto abdominal.

    Ao exame ultrassonográfico fictício, os rins apresentam topografia habitual,
    dimensões preservadas e discreto aumento de ecogenicidade cortical.
    A relação corticomedular encontra-se parcialmente preservada.

    A bexiga urinária está moderadamente preenchida, com conteúdo anecogênico.
    A parede vesical apresenta discreto espessamento regular.
    Não foram observadas estruturas compatíveis com cálculos no lúmen vesical.

    O fígado apresenta contornos regulares e parênquima discretamente heterogêneo.
    O baço apresenta dimensões preservadas, contornos regulares e ecotextura homogênea.

    Os achados são inespecíficos e devem ser correlacionados com exame clínico
    e exames laboratoriais.
    """

    pergunta_usuario = "Quais alterações urinárias e renais aparecem no documento?"

    termos_busca = ["urinária", "urina", "renal", "renais", "rins", "bexiga"]

    texto_limpo = limpar_texto(documento_ficticio)
    trechos = dividir_em_trechos(texto_limpo)
    resultados = buscar_trechos(trechos, termos_busca)

    print("Pergunta do usuário:")
    print(pergunta_usuario)

    exibir_resultados(resultados)
