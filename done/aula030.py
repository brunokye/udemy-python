velocidade = 50  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR = 60  # velocidade máxima do radar
LOCAL = 100  # local onde o radar está
DISTANCIA = 1  # A distância onde o radar pega

antes_radar = local_carro >= (LOCAL - DISTANCIA)
depois_radar = local_carro <= (LOCAL + DISTANCIA)

verifica_velocidade = velocidade > RADAR
verifica_radar = antes_radar and depois_radar
verifica_multa = verifica_radar and verifica_velocidade

if verifica_velocidade:
    print('Velocidade do carro maior que a permitida.')

if verifica_radar:
    print('Carro passou do radar.')

if verifica_multa:
    print('Carro foi mutado no radar.')
