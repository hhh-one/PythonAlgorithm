# %포맷팅으로 할 수 있나 해서 고민
n = int(input())
for i in range(1, n+1):
    print(" "  * (n - i) + "*" * i)