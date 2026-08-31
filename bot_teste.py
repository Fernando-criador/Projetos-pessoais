print('Bot iniciado')
while True:
    comando = input('Digite um comando: ')
    if comando.upper() == 'PREÇO':
        preco_alvo = float(input('Preço alvo: ''(0 para sair) '))
        while True:
            
            preco_atual = float(input("Preço atual: " "(0 para sair)"))

            if preco_atual == 0 or preco_alvo == 0:
                print('Encerrado')
                break
        
            elif preco_atual > preco_alvo:
                print(f'ALERTA! PREÇO ALVO ATINGINDO!!\n A cota está: R$ {preco_atual:.2f}')

            elif preco_atual == preco_alvo:
                print(f'A cota se mantém estável.\n A cota está: R$ {preco_atual:.2f}')

            else: 
                print(f'Preço alvo ainda não atigindo\nA cota está: R$ {preco_atual:.2f}')

                 
    elif comando.upper() == 'OI':
        print('Oi eu sou seu bot')

    
    elif comando.upper() == 'SAIR':
        print('Bot encerrado.')
        break
    else:
        print('Não entendi o seu comando.')
    
    
        
