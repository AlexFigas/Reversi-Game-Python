#########################################################
#       Instituto Superior de Engenharia de Lisboa      #
#  Licenciatura em Engenharia Informática e Multimédia  #
#           Matemática Discreta e Programação           #
#              @autor Alexandre Figueiredo              #
#########################################################

def inserir_pecas_iniciais(grelha):
    """
    Função inserir_pecas_iniciais

    Argumentos
                1. grelha: A grelha do jogo, ainda sem peças colocadas

    Retorno
    Retorna a grelha com as peças iniciais colocadas
    """
    grelha[3][3] = 1  # Coloca a peça 1 na linha 4, coluna 4
    grelha[4][4] = 1  # Coloca a peça 1 na linha 5, coluna 5
    grelha[3][4] = 2  # Coloca a peça 2 na linha 4, coluna 5
    grelha[4][3] = 2  # Coloca a peça 2 na linha 5, coluna 4


def reversi_novo_jogo():
    """
    Função reversi_novo_jogo

    Argumentos
    Não tem argumentos.

    Retorno
    Retorna a estrutura de dados usada para armazenar um jogo, inicializada com um jogo pronto para se começar a jogar.

    Descrição
    Permite criar um jogo pronto para se começar a jogar. Com as 4 peças
    centrais já colocadas.
    """
    grelha = [  # Inicializa a grelha com 0s (vazia para o jogo)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    inserir_pecas_iniciais(grelha)  # Coloca na grelha as peças iniciais
    proximo_a_jogar = 1  # No inicio do jogo o próximo a jogar é o primeiro jogador a jogar ou seja o jogador 1
    jogador_que_passou = None  # No inicio do jogo ainda não passou nenhum jogador portanto None
    jogadas_possiveis = 0  # Lista com as jogadas possiveis
    pecas_a_conquistar = []  # Lista com listas [linha, coluna] a conquistar
    jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou)  # A estrutura de dados
    # que armazena o jogo.
    return jogo


def reversi_valor(jogo, linha, coluna):
    """
    Função reversi_valor

    Argumentos
              1. jogo: A estrutura de dados que armazena o jogo.
              2. linha: O número da linha de uma posição da grelha.
              3. coluna: O número da coluna de uma posição da grelha.

    Retorno
    Retorna o valor que está armazenado na posição da grelha do jogo, na
    linha linha e na coluna coluna. O retorno é um número inteiro. Esse
    número é:
              • 1 se a posição está ocupada pelo primeiro jogador a jogar;
              • 2 se a posição está ocupada pelo segundo jogador a jogar;
              • 0 se a posição está vazia.

    Descrição
    Esta função permite obter os valores que estão na grelha do jogo. Permite que parte gráfica represente graficamente
    o jogo.
    """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    grelha = jogo[0]
    valor = grelha[linha - 1][coluna - 1]
    return valor


def espaco_valido(linha, coluna):
    """
    Função espaco_valido
    Argumentos
              1. linha: O número da linha de uma posição da grelha.
              2. coluna: O número da coluna de uma posição da grelha.

    Retorno
    Retorna True se as coordenadas estiverem localizadas no tabuleiro e False caso contrário.
    """
    return (0 <= linha - 1 <= 7) and (0 <= coluna - 1 <= 7)


def get_sequencia(jogo, linha, coluna):
    """
        Função get_sequencia
        Argumentos
                  1. jogo: A estrutura de dados que armazena o jogo.
                  2. linha: O número da linha de uma posição da grelha.
                  3. coluna: O número da coluna de uma posição da grelha.

        Retorno
        Retorna a sequência de valores a trocar. Caso a jogada não seja possivel retorna uma lista vazia.
        """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    jogo = list(jogo)
    proximo_a_jogar = jogo[1]
    if proximo_a_jogar == 1:  # Se o proximo jogador a jogar for 1 vou procurar por 2's á minha volta
        outro_jogador = 2
    else:
        outro_jogador = 1  # Se não for procuro por 1's
    sequencia = []
    direcoes = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]  # Vetores de todas as direções
    for incremento_linha, incremento_coluna in direcoes:  # Incremento linha toma o valor de indice 0 dentro de cada
        # direção, incremento coluna toma o valor de indice 1 dentro de cada direção
        linha_inicial = linha  # Serve para reiniciar o valor da linha e coluna para podermos ver todos os valores á
        # volta dessa linha e coluna
        coluna_inicial = coluna
        if espaco_valido(linha, coluna) and reversi_valor(jogo, linha, coluna) == 0:  # Se o espaço for válido e se o
            # valor numa dada linha, coluna seja 0, é uma potencial jogada possivel portanto incrementamos o valor das
            # direções
            linha = linha + incremento_linha
            coluna = coluna + incremento_coluna
            while espaco_valido(linha, coluna) and reversi_valor(jogo, linha, coluna) == outro_jogador:  # Enquanto o
                # espaço continuar a ser válido e o valor numa dada linha, coluna nas direções sejam iguais ao valor do
                # outro jogador, fazer append desse valor de linha e coluna e incrementar a direção.
                sequencia.append([linha, coluna])
                linha = linha + incremento_linha
                coluna = coluna + incremento_coluna
                if espaco_valido(linha, coluna) and reversi_valor(jogo, linha, coluna) == 0:  # Caso depois de
                    # incrementar o valor da direção, o valor na linha e coluna seja 0 não é uma jogada possivel
                    # portanto dá reset á lista
                    sequencia = []
                    break
                elif espaco_valido(linha, coluna) and reversi_valor(jogo, linha, coluna) == proximo_a_jogar:  # Caso
                    # seja um espaco valido e o valor é igual ao valor do proximo a jogar, então é uma jogada valida
                    sequencia.append([linha_inicial, coluna_inicial])  # Append linha inicial e coluna inicial para
                    # completar a sequencia
        linha = linha_inicial  # Reinicializa a linha
        coluna = coluna_inicial  # Reinicializa a coluna
    jogo[3] = sequencia  # Atualiza o jogo
    return sequencia


def reversi_jogada_possivel(jogo, linha, coluna):
    """
    Função reversi_jogada_possivel

    Argumentos
              1. jogo: A estrutura de dados que armazena o jogo.
              2. linha: O número da linha de uma posição da grelha.
              3. coluna: O número da coluna de uma posição da grelha.

    Retorno
    Retorna True caso o próximo jogador a jogar possa jogar na posição
    na linha linha e na coluna coluna. Retorna False, caso contrário.

    Descrição
    Esta função permite que a parte gráfica indique ao jogador quais são
    as suas jogadas possíveis.
    """
    if len(get_sequencia(jogo, linha, coluna)) > 0:  # Se houver jogadas possiveis, também há uma sequencia possivel
        # para virar portanto retorna True
        return True
    else:
        return False  # Se não retorna False


def contar_valor(jogo, valor):
    """
    Função contar_valor

    Argumentos
              1. jogo: A estrutura de dados que armazena o jogo.
              2. valor: O valor que pertendo procurar na grelha.

    Retorno
    Retorna a quantidade de valores valor da grelha.

    Descrição
    Esta função permite verificar se o jogo chegou ao fim e contar os pontos de cada jogador.
    """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    grelha = jogo[0]  # A grelha do jogo
    numero_ocorrencias = 0  # No inicio, ainda não se contou nada portanto começa em 0
    for linha in range(len(grelha)):  # len(grelha) e não 8 para poder ser implementado não importe o tamanho da grelha
        for coluna in range(len(grelha[linha])):  # len(grelha[linha]) pelo mesmo motivo acima
            if grelha[linha][coluna] == valor:  # Se houver um valor nessa linha, coluna
                numero_ocorrencias = numero_ocorrencias + 1  # Contar essa ocorrencia.
    return numero_ocorrencias  # Retornar o numero de vezes que um determinado valor (valor) aparece.


def reversi_fim_jogo(jogo):
    """
    Função reversi_fim_jogo


    Argumentos
    1. jogo: A estrutura de dados que armazena o jogo.

    Retorno
    Retorna True, se já não há mais jogadas possíveis e portanto o jogo
    chegou ao fim. Ou False, caso contrário.

    Descrição
    Permite que a parte gráfica saiba se o jogo chegou ao fim. Se chegou ao
    fim, mostra as mensagens finais. Senão chegou ao fim, o jogo procede
    normalmente.
    """
    proximo_a_jogar = jogo[1]
    if proximo_a_jogar is None:  # Se não houver próximo a jogar o jogo acaba ou seja retorna True
        return True
    else:
        return False  # Se não estiver retorna False


def reversi_proximo_a_jogar(jogo):
    """
    Argumentos
                1. jogo: A estrutura de dados que armazena o jogo.

    Retorno
    Retorna o tuplo:
                (proximo_a_jogar, jogador_que_passou)
    Onde:
                • proximo_a_jogar é o identificador do próximo jogador a jogar,
    isto é, 1 ou 2, ou None caso o jogo tenha chegado ao fim.
                • jogador_que_passou é None caso o próximo jogador a jogar possa
    jogar porque tem jogadas possíveis. Ou, o identificador do jogador
    que passou, isto é, 1 ou 2, caso o jogador que deveria jogar tenha
    tido que passar por não ter jogadas possíveis.

    Descrição
    Permite que a parte gráfica saiba qual é o próximo jogador a jogar, e
    se o jogador que deveria jogar passou, porque não tinha como jogar.
    Assim a parte gráfica pode solicitar ao próximo jogador a jogar que
    jogue, e ao mesmo tempo indicar ao jogador que teve que passar que
    passou.
    """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    proximo_a_jogar = jogo[1]
    jogador_que_passou = jogo[4]
    return proximo_a_jogar, jogador_que_passou


def reversi_pontuacao(jogo):
    """
    Função reversi_pontuacao

    Argumentos
                1. jogo: A estrutura de dados que armazena o jogo.

    Retorno
    Retorna o tuplo:
                (pontos_jogador_1, pontos_jogador_2)

    Onde:
                • pontos_jogador_1 é o número (inteiro) de casas ocupadas pelo
    primeiro jogador a jogar.
                • pontos_jogador_2 é o número (inteiro) de casas ocupadas pelo
    segundo jogador a jogar.

    Descrição
    """
    pontos_jogador_1 = contar_valor(jogo, 1)
    pontos_jogador_2 = contar_valor(jogo, 2)
    return pontos_jogador_1, pontos_jogador_2


def trocar_jogador(jogo):
    """
    Função trocar_jogador

    Argumentos
                1. jogo: A estrutura de dados que armazena o jogo.

    Retorno
    Retorna a estrutura de dados usada para armazenar um jogo, com o próximo a jogar atualizado.

    Descrição
    Permite o modo texto ir alternando os jogadores.
    """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    jogo = list(jogo)
    proximo_a_jogar = jogo[1]
    if proximo_a_jogar == 1:  # Se o proximo a jogar for 1, o a seguir é o 2
        proximo_a_jogar = 2
    else:
        proximo_a_jogar = 1  # Se não for o a seguir é o 1
    jogo[1] = proximo_a_jogar
    return jogo


def get_jogadas_possiveis(jogo):
    """
    Função get_jogadas_possiveis

    Argumentos
                1. jogo: A estrutura de dados que armazena o jogo.

    Retorno
    Retorna uma lista com os valores de onde é possivel jogar.

    Descrição
    Permite saber se o jogador pode jogar ou não, se não poder passa ao próximo.
    """
    grelha = jogo[0]
    jogadas = []
    for linha in range(len(grelha)):
        for coluna in range(len(grelha[linha])):
            if reversi_jogada_possivel(jogo, linha + 1, coluna + 1):
                jogadas.append([linha + 1, coluna + 1])
    return jogadas


def reversi_jogar(jogo, linha, coluna):
    """
    Argumentos
                1. jogo: A estrutura de dados que armazena o jogo.
                2. linha: O número da linha de uma posição da grelha.
                3. coluna: O número da coluna de uma posição da grelha.

    Retorno
    Retorna a estrutura de dados usada para armazenar um jogo, atualizada com a
    jogada. Caso a posição indicada não seja a de uma jogada possível, ignora a
    jogada, retornando o jogo recebido como argumento.

    Descrição
    Permite indicar qual é a posição em que o próximo jogador a jogar
    jogou.
    """
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    # jogo = (grelha, proximo_a_jogar, jogadas_possiveis, pecas_a_conquistar, jogador_que_passou), apenas auxiliar para
    # perceber onde se encontravam os valores dentro do tuplo do jogo.
    jogo = list(jogo)
    grelha = jogo[0]
    proximo_a_jogar = jogo[1]
    sequencia = get_sequencia(jogo, linha, coluna)  # Sequencia de valores a virar
    for jogada_linha, jogada_coluna in sequencia:  # Para cada uma das posições da grelha onde preciso trocar a peça
        if proximo_a_jogar == 1:  # Se o jogador for o 1, trocar as peças para o 1
            grelha[jogada_linha - 1][jogada_coluna - 1] = 1
        else:  # Se não trocar para o 2
            grelha[jogada_linha - 1][jogada_coluna - 1] = 2
    jogo = trocar_jogador(jogo)  # Muda a vez do jogador
    if len(get_jogadas_possiveis(jogo)) == 0:  # Se não existirem jogadas possiveis trocar de jogador
        jogo = trocar_jogador(jogo)
        if len(get_jogadas_possiveis(jogo)) == 0:  # Se não existirem jogadas possiveis o proximo jogador é None e o
            # jogo termina
            jogo[1] = None
    return jogo