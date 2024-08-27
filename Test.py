
# def ProbTrocoMinMemo(N, S, memo={}):
#     if N == 0:
#         return 0
#     if N in memo:
#         return memo[N]

#     numMoedasDisp = len(S)
#     smallest = float("inf")
#     for j in range(numMoedasDisp):
#         if S[j] <= N:
#             smallest = min(smallest, 1 + ProbTrocoMinMemo(N - S[j], S, memo))

#     memo[N] = smallest
#     return smallest


# def ProbTrocoMinRec(N, S, memo=None):
#     if memo is None:
#         memo = [-1] * (N + 1)
#     if N == 0:
#         return 0
#     if memo[N] != -1:
#         return memo[N]
#     min_coins = float('inf')
#     for coin in S:
#         if N >= coin:
#             num_coins = ProbTrocoMinRec(N - coin, S, memo)
#             if num_coins != float('inf'):
#                 min_coins = min(min_coins, num_coins + 1)
#     memo[N] = min_coins
#     return memo[N]
# def ProbTrocoMinRec(N, S, memo=None):
#     if memo is None:
#         memo = [-1] * (N + 1)
#     if N == 0:
#         return 0
#     if memo[N] != -1:
#         return memo[N]
#     min_coins = float('inf')
#     for coin in S:
#         if N >= coin:
#             num_coins = ProbTrocoMinRec(N - coin, S, memo)
#             if num_coins != float('inf'):
#                 min_coins = min(min_coins, num_coins + 1)
#     memo[N] = min_coins
#     return memo[N]




# if __name__ == '__main__':
#     N = 998
#     S = [1, 5, 10, 25, 50, 100]
#     print(ProbTrocoMin(N, S))
#     print(ProbTrocoMinRec(N, S))


def ProbTrocoMin(N, S):
  Opt = [0 for i in range(0, N+1)]
  numMoedasDisp = len(S)

  for i in range(1, N+1):
    smallest = np.inf
    for j in range (0, numMoedasDisp):
      if (S[j] <= i):
        smallest = min(smallest, Opt[i - S[j]])
    Opt[i] = 1 + smallest
  return Opt[N]




def ProbTrocoMinRec(N, S, memo=None):
    if memo is None:
        memo = [-1] * (N + 1)
    if N == 0:
        return 0
    if memo[N] != -1:
        return memo[N]
    min_coins = float('inf')
    for coin in S:
        if N >= coin:
            num_coins = ProbTrocoMinRec(N - coin, S, memo)
            if num_coins != float('inf'):
                min_coins = min(min_coins, num_coins + 1)
    memo[N] = min_coins
    return memo[N]



