import time
import sys
import random
sys.setrecursionlimit(1000000000)

# Função para gerar entradas aleatórias 
def generate_fixed_value_inputs(n, m, max_coin_value):
    inputs = []
    for _ in range(m):
        value = n  
        coins = [random.randint(1, max_coin_value) for _ in range(random.randint(1, 10))]
        inputs.append((value, coins))
    return inputs

# Função para comparar os algoritmos
def compare_algorithms(n_sizes, m, max_coin_value):
    for n in n_sizes:
        inputs = generate_fixed_value_inputs(n, m, max_coin_value)
        
        start_time = time.time()
        for value, coins in inputs:
            ProbTrocoMin_recursive(value, coins)
        recursive_time = (time.time() - start_time) / m
        
        start_time = time.time()
        for value, coins in inputs:
            ProbTrocoMin_iterative(value, coins)
        iterative_time = (time.time() - start_time) / m
        
        print(f"Tamanho da entrada: {n}")
        print(f"Tempo médio (recursivo com memoização): {recursive_time:.6f} segundos")
        print(f"Tempo médio (iterativo): {iterative_time:.6f} segundos")
        print()

n_sizes = [10, 50, 100, 500, 1000]
m = 100  
max_coin_value = 100

def ProbTrocoMin_recursive(value, coins):
    # Implementação recursiva com memoização
    memo = {}
    return helper(value, coins, memo)

def helper(currentValue, coins, memo):
    if currentValue == 0:
        return 0
    if currentValue in memo:
        return memo[currentValue]
    
    minCoins = float("inf")
    for coin in coins:
        if coin <= currentValue:
            numCoins = helper(currentValue - coin, coins, memo)
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


compare_algorithms(n_sizes, m, max_coin_value)
