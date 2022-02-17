univ = {0: "Soongsil", 1: "Korea", 2: "Hanyang"}

ptcp = list(map(int, input().split()))

if sum(ptcp) >= 100:
    print("OK")
else:
    print(univ[ptcp.index(min(ptcp))])
