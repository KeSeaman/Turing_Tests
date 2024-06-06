def solution(n: int) -> int:
    # Base cases
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # Initialize a list to store the number of ways to reach each rock
    dp = [0] * (n + 1)

    # There is 1 way to reach the first rock and 2 ways to reach the second rock
    dp[1] = 1
    dp[2] = 2

    # Fill the dp list using the recurrence relation
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # The number of ways to reach the nth rock
    return dp[n]

# README
if __name__ == '__main__':
    n = int(input())
    print(solution(n))
