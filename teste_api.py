import requests

moeda = input('Digite a moeda: ').upper()

res = requests.get( f"https://api.binance.com/api/v3/ticker/price?symbol={moeda}")

dados = res.json()

print(f'Moeda: {dados["symbol"]}')
print(f'Preço: R$ {dados["price"]}')



#Candles
intervalo = input('Defina o intervalo: ')

limite = int(input('Defina um limite da candles: '))

candle = requests.get(f"https://api.binance.com/api/v3/klines?symbol={moeda}&interval={intervalo}&limit={limite}")

dado2 = candle.json()

for candle in dado2:
    abertura = float(candle[1])
    maxima = float(candle[2])
    minima = float(candle[3])
    fechamento = float(candle[4])
    volume = float(candle[5])

    print(f'Abertura:   R$ {abertura:,.2f}')
    print(f'Máxima:   R$ {maxima:,.2f}')
    print(f'Mínima:   R$ {minima:,.2f}')
    print(f'Fechamento:   R$ {fechamento:,.2f}')
    print(f'Volume:   {volume:,.2f} {moeda}')
    print(f'-'*40)