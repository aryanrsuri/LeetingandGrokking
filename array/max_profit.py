
def max_profit(prices):
    high = prices[-1]
    delta = 0
    for p in reversed(prices):
        if p > high:
            high = p
        if delta < high - p:
            delta = high - p
    return delta
tc =[7,1,5,3,6,4]
print(max_profit(tc))