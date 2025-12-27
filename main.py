import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount, coins=COINS):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result


def find_min_coins(amount, coins=COINS):
    coin_count = [float("inf")] * (amount + 1)
    coin_count[0] = 0

    last_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and coin_count[i - coin] + 1 < coin_count[i]:
                coin_count[i] = coin_count[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current = amount

    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def measure(func, amount, repeat=5, number=100):
    times = timeit.repeat(lambda: func(amount), repeat=repeat, number=number)
    return min(times)


def main():
    amount = 113
    print("Amount:", amount)
    print("Greedy:", find_coins_greedy(amount))
    print("Dynamic Programming:", find_min_coins(amount))

    amounts = [10, 100, 1000, 5000, 10000]

    print("\nBenchmark (seconds):")
    print("{:<8} {:>12} {:>12}".format("amount", "greedy", "dp"))
    print("-" * 34)

    for a in amounts:
        greedy_time = measure(find_coins_greedy, a)
        dp_time = measure(find_min_coins, a, number=10)

        print("{:<8} {:>12.6f} {:>12.6f}".format(a, greedy_time, dp_time))


main()
