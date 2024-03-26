def forca_bruta(Itens, peso_maximo):
    utilidade_maxima = 0
    sequencia_otima = []

    def forca_bruta_r(indice, sacola):
        nonlocal utilidade_maxima, sequencia_otima

        if indice == len(Itens):
            if sacola['utilidade'] > utilidade_maxima:
                utilidade_maxima = sacola['utilidade']
                sequencia_otima[:] = sacola['itens']
            return

        item_atual = Itens[indice]

        # Tenta incluir o item atual na mochila
        if sacola['peso'] + item_atual['peso'] <= peso_maximo:
            novo_sacola = {
                'utilidade': sacola['utilidade'] + item_atual['utilidade'],
                'peso': sacola['peso'] + item_atual['peso'],
                'itens': sacola['itens'] + [indice]
            }
            forca_bruta_r(indice + 1, novo_sacola)

        # Tenta não incluir o item atual na mochila
        forca_bruta_r(indice + 1, sacola)

    forca_bruta_r(0, {'utilidade': 0, 'peso': 0, 'itens': []})

    return sequencia_otima, utilidade_maxima

# Exemplo de utilização
Itens = [
    {'utilidade': 60, 'peso': 10},
    {'utilidade': 100, 'peso': 20},
    {'utilidade': 120, 'peso': 30}
]
peso_maximo = 50

sequencia_otima, utilidade_maxima = forca_bruta(Itens, peso_maximo)
print("Sequência ótima:", sequencia_otima)
print("Utilidade máxima:", utilidade_maxima)
