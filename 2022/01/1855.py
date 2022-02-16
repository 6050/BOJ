if __name__ == '__main__':

    col = int(input())
    cypher = input()
    row = len(cypher) // col
    table = [[""] * col for _ in range(row)]

    idx = 0
    for i in range(row):
        for j in range(col):
            table[i][j] = cypher[idx]
            idx += 1

    for i in range(len(table)):
        if i % 2 != 0:
            table[i].reverse()

    for j in range(col):
        for i in range(row):
            print(table[i][j], end="")
