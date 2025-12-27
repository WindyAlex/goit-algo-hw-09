# Greedy vs Dynamic Programming (Coin Change)

## Introduction
Two functions were implemented for making change with coins [50, 25, 10, 5, 2, 1]:
- find_coins_greedy(amount) — greedy approach
- find_min_coins(amount) — dynamic programming approach (minimum number of coins)

## Algorithms

### Greedy Algorithm

The greedy algorithm always takes the largest possible coin first.  
It works very fast and gives the correct result for this set of coins.

Time complexity: **O(n)**, where n is the number of coin denominations.

---

### Dynamic Programming

The dynamic programming algorithm finds the minimum number of coins needed to make a given amount.  
It guarantees the optimal solution but works slower for large amounts.

Time complexity: **O(amount × n)**.

---

## Performance Comparison

Amount: 113  
Greedy: {50: 2, 10: 1, 2: 1, 1: 1}  
Dynamic Programming: {50: 2, 10: 1, 2: 1, 1: 1}

Benchmark (seconds):
amount         greedy           dp
----------------------------------
10           0.000035     0.000048  
100          0.000036     0.000515  
1000         0.000036     0.006285  
5000         0.000037     0.032394  
10000        0.000036     0.065003  

Benchmark results show that:

- The greedy algorithm works almost instantly even for large amounts.
- The dynamic programming algorithm becomes significantly slower as the amount increases.
- For this coin system, both algorithms return the same result, but greedy is much faster.

---

## Conclusion

For this specific set of coins, the greedy algorithm is the most efficient choice.  
Dynamic programming is more universal, but it is not practical for large amounts due to its higher time complexity.