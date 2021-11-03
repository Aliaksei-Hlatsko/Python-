def coins(price):
    coin_five = int(price/5)
    lost = price%5
    coin_two = int(lost/2)
    coin_one = lost%2
    sum = coin_five+coin_two+coin_one
    print(sum)
coins(22)