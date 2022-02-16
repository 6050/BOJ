if __name__ == '__main__':

    C = int(input())
    cypher = input()
    R = len(cypher) // C
    table = [[""] * C for _ in range(R)]

    idx = 0
    for i in range(R):
        for j in range(C):
            table[i][j] = cypher[idx]
            idx += 1

    for i in range(R):
        if i % 2 != 0:
            table[i].reverse()

    for j in range(C):
        for i in range(R):
            print(table[i][j], end="")
