if __name__ == '__main__':

    name = list(input())

    scores, teams = [], []
    for i in range(int(input())):

        team = input()
        teams.append(team)

        team = list(team)
        L = name.count("L") + team.count("L")
        O = name.count("O") + team.count("O")
        V = name.count("V") + team.count("V")
        E = name.count("E") + team.count("E")
        scores.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)

    champions = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            champions.append(teams[i])

    champions.sort()
    print(champions[0])
