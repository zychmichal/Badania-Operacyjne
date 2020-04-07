def translate_to_tournament(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > 1:
                M[i][j] = 1
            elif M[i][j] == 1:
                M[i][j] = 0
            else:
                M[i][j] = -1


def check_tournament_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != -M[j][i]:
                return False
    return True


def check_if_draw_is_possible(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0 and i != j:
                return True
    return False


def count_inconsistency_triples(M):
    counter =0
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            for k in range(j+1,len(M)):
                if M[i][j] == M[j][k] == M[k][i]:
                    counter += 1
    return counter


def count_inconsistency_triples_generalized(M):
    counter = 0
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            for k in range(j+1,len(M)):
                if abs(M[i][j]) + abs(M[j][k]) + abs(M[k][i]) == 1:
                    counter +=1
                elif abs(M[i][j]) + abs(M[j][k]) + abs(M[k][i]) == 2 and (M[i][j] == M[j][k] or M[j][k] == M[k][i] or M[i][j] == M[k][i]):
                    counter +=1
                elif M[i][j] == M[j][k] == M[k][i] != 0:
                    counter += 1
    return counter


def max_count_of_incosistency_triples_generalized(n):
    if n % 4 == 0:
        return (13*(n ** 3) - 24 * (n**2)-16*n) / 96
    elif n % 4 == 1:
        return (13*(n ** 3) - 24 * (n**2)-19*n+30) / 96
    elif n % 4 == 2:
        return (13*(n ** 3) - 24 * (n**2)-4*n) / 96
    elif n % 4 == 3:
        return (13*(n ** 3) - 24 * (n**2)-19*n+18) / 96


def max_count_of_incosistency_triples(n):
    if n % 2 == 0:
        return (n**3 - 4*n)/24
    else:
        return (n**3-n)/24


def count_kendall(M):
    TM = count_inconsistency_triples_generalized(M)
    yn = max_count_of_incosistency_triples_generalized(len(M))
    return 1-(abs(TM)/yn)


def count_clasic_kendall(M):
    TM = count_inconsistency_triples(M)
    In = max_count_of_incosistency_triples(len(M))
    return 1-(abs(TM)/In)

A=[[1,2/3,2,5/2,5/3,5],[3/2,1,3,10/3,3,9],[1/2,1/3,1,4/3,7/8,5/2],[2/5,3/10,3/4,1,5/6,12/5],[3/5,1/3,8/7,6/5,1,3],[1/5,1/9,2/5,5/12,1/3,1]]

B=[[1,2/5,3,7/3,1/2,1,2],[5/2,1,4/7,1,1,3,2/3],[1/3,7/4,1,1/2,2,1/2,1],[3/7,1,2,1,4,2,6],[2,1,1/2,1/4,1,1/2,3/4],[1,1/3,2,1/2,2,1,5/8],[1/2,3/2,1,1/6,4/3,8/5,1]]

C=[[1,2/3,2/15,1,8,12/5,1,1/2],[3/2,1,1,2,1,2/3,1/6,1],[15/2,1,1,5/2,7/8,2,1,1/5],[1,1/2,2/5,1,4/3,1,2/7,1],[1/8,1,8/7,3/4,1,1/5,2/7,1],[5/12,3/2,1/2,1,5,1,3,2],[1,6,1,7/2,7/2,1/3,1,3/11],[2,1,5,1,1,1/2,11/3,1]]

D=[[0,1,1,-1,-1,1,-1],[-1,0,0,1,1,-1,0],[-1,0,0,0,1,1,-1],[1,-1,0,0,1,0,1],[1,0,-1,-1,0,1,-1],[-1,1,-1,1,-1,0,0],[1,0,1,-1,1,0,0]]

E=[[0,1,0,0,-1],[-1,0,0,0,1],[0,0,0,1,0],[0,0,-1,0,0],[1,-1,0,0,0]]

F=[[0,-1,1,-1,1,-1,1,-1,1],[1,0,1,1,1,-1,-1,-1,-1],[-1,-1,0,-1,1,-1,1,1,1],[1,-1,1,0,-1,1,-1,1,-1],[-1,-1,-1,1,0,-1,1,1,1],[1,1,1,-1,1,0,-1,-1,-1],[-1,1,-1,1,-1,1,0,1,-1],[1,1,-1,-1,-1,1,-1,0,1],[-1,1,-1,1,-1,1,1,-1,0]]


if __name__ == "__main__":
    list_1 = [A, B, C]
    dict_1 = {'A': A, 'B': B, 'C': C}
    for M in dict_1.values():
        translate_to_tournament(M)

    dict_1['D'] = D
    dict_1['E'] = E
    dict_1['F'] = F
    list_of_keys_to_delete = []
    for k,M in dict_1.items():
        if not check_tournament_matrix(M):
            print("Macierz " + k + " nie jest macierza turniejowa.")
            print()
            list_of_keys_to_delete.append(k)

    for k in list_of_keys_to_delete:
        dict_1.pop(k)

    dict_with_draw = {}
    dict_without_draw = {}
    for k,M in dict_1.items():
        if check_if_draw_is_possible(M):
            dict_with_draw[k] = M
        else:
            dict_without_draw[k] = M

    dict_to_print = {}
    for k,M in dict_with_draw.items():
        dict_to_print[k] = [count_kendall(M)]
    for k,M in dict_without_draw.items():
        dict_to_print[k] = [count_kendall(M)]
        dict_to_print[k].append(count_clasic_kendall(M))
    tuples_of_results = sorted(dict_to_print.items())
    for k,v in tuples_of_results:
        if len(v) == 1:
            print("Macierz " + k + " ma indeks uogolniony rowny " + str(v[0]))
            print()
        elif len(v) == 2:
            print("Macierz " + k + " ma indeks klasyczny rowny " + str(v[1]))
            print("Macierz " + k + " ma indeks uogolniony rowny " + str(v[0]))
            print()

