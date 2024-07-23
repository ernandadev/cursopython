'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexobidade (ruim)
'''
Velocidade = 61  # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # A distância onde o radar

velocidade_carro_passou_radar_1 = Velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if Velocidade > RADAR_1:
    print('A Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em rada 1')