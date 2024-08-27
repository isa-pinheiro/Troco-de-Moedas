import timeit
import sys

sys.setrecursionlimit(1000000000)

def compare_algorithms_varying_coins(n, max_coins=10):
    recursive_times = []
    iterative_times = []
    coin_sets = [list(range(1, i + 1)) for i in range(1, max_coins + 1)]
    
    for coins in coin_sets:
        # Medição de tempo para a função recursiva com memoização
        recursive_time = timeit.timeit(lambda: ProbTrocoMin_recursive(n, coins), number=1)
        recursive_times.append(recursive_time)
        
        # Medição de tempo para a função iterativa
        iterative_time = timeit.timeit(lambda: ProbTrocoMin_iterative(n, coins), number=1)
        iterative_times.append(iterative_time)
        
        print(f"Conjunto de moedas: {coins}")
        print(f"Tempo (recursivo com memoização): {recursive_time:.6f} segundos")
        print(f"Tempo (iterativo): {iterative_time:.6f} segundos")
        print()

def compare_algorithms_varying_n(n_sizes, coins):
    recursive_times = []
    iterative_times = []
    
    for n in n_sizes:
        value = n
        
        # Medição de tempo para a função recursiva com memoização
        recursive_time = timeit.timeit(lambda: ProbTrocoMin_recursive(value, coins), number=1)
        recursive_times.append(recursive_time)
        
        # Medição de tempo para a função iterativa
        iterative_time = timeit.timeit(lambda: ProbTrocoMin_iterative(value, coins), number=1)
        iterative_times.append(iterative_time)
        
        print(f"Tamanho da entrada: {n}")
        print(f"Tempo (recursivo com memoização): {recursive_time:.6f} segundos")
        print(f"Tempo (iterativo): {iterative_time:.6f} segundos")
        print()

def ProbTrocoMin_recursive(value, coins):
    # Implementação recursiva com memoização
    memo = {}
    return ProbTrocoMin_Aux(value, coins, memo)

def ProbTrocoMin_Aux(currentValue, coins, memo):
    if currentValue == 0:
        return 0
    if currentValue in memo:
        return memo[currentValue]
    
    minCoins = float("inf")
    for coin in coins:
        if coin <= currentValue:
            numCoins = ProbTrocoMin_Aux(currentValue - coin, coins, memo)
            if numCoins != float("inf"):
                minCoins = min(minCoins, numCoins + 1)
    
    memo[currentValue] = minCoins
    return minCoins

def ProbTrocoMin_iterative(value, coins):
    # Implementação iterativa
    if value < 0:
        return -1
    
    minCoins = [float("inf")] * (value + 1)
    minCoins[0] = 0
    
    for currentValue in range(1, value + 1):
        for coin in coins:
            if coin <= currentValue:
                minCoins[currentValue] = min(minCoins[currentValue], minCoins[currentValue - coin] + 1)
    
    return minCoins[value] if minCoins[value] != float("inf") else -1

# Teste N variando
n_sizes = list(range(1, 1001))
coins = [1, 5, 10, 25, 50, 100]  # Conjunto fixo de moedas
# compare_algorithms_varying_n(n_sizes, coins)

# Teste Número de moedas variando
n = 1000
compare_algorithms_varying_coins(n)
