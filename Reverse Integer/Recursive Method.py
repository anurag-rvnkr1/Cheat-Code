def reverse(x):
    INT_MAX = 2**31 - 1

    def helper(n, res):
        if n == 0:
            return res

        res = res*10 + n%10
        return helper(n//10, res)

    sign = -1 if x < 0 else 1
    x = abs(x)

    ans = helper(x, 0) * sign
    return ans if -2**31 <= ans <= INT_MAX else 0
