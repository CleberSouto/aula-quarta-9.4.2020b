ta_arq = float(input('Digite o tamanho do arquivo em MB '))

ve_int = float(input('Digite a velocidade de sua conexão de internet em Mbps '))

t_envio = (ta_arq / (ve_int/8)) / 60
print('O tempo de envio é: ', round(t_envio),'min')