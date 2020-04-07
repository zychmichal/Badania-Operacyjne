class Node:
    def __init__(self, value, stos, player, turn_value, list_visit_first, list_visit_second, first_not_moves=False, second_not_moves=False):
        self.children = []
        self.value = value
        self.stos = stos
        self.player = player
        self.turn_value = turn_value
        self.list_visit_first = list_visit_first
        self.list_visit_second = list_visit_second
        self.first_not_moves = first_not_moves
        self.second_not_moves = second_not_moves

    def add_child(self, child):
        self.children.append(child)


def get_all_possible_moves(node):
    all_possible_moves = []
    last_value = node.turn_value
    stos = node.stos
    if node.player == 1:
        for k, v in stos.items():
            if k not in node.list_visit_first:
                if last_value > 0:
                    if 1 <= v < last_value * 2:
                        for i in range(1, v + 1):
                            all_possible_moves.append((k, i))
                    elif v >= last_value * 2:
                        for i in range(1, last_value * 2 + 1):
                            all_possible_moves.append((k, i))
                else:
                    if v > 0:
                        all_possible_moves.append((k, 1))
        return all_possible_moves
    else:
        for k, v in stos.items():
            if k not in node.list_visit_second:
                if last_value > 0:
                    if 1 <= v < last_value * 2:
                        for i in range(1, v+1):
                            all_possible_moves.append((k, i))
                    elif v >= last_value * 2:
                        for i in range(1, last_value * 2 + 1):
                            all_possible_moves.append((k, i))
                else:
                    if v > 0:
                        all_possible_moves.append((k, 1))
        return all_possible_moves


def generates_children_from_moves(node, moves):
    stos = node.stos
    for k,v in moves:
        new_stos = stos.copy()
        new_stos[k] -= v
        if node.player == 1:
            visit_first = node.list_visit_first.copy()
            visit_second = node.list_visit_second.copy()
            visit_first.append(k)
            node.add_child(Node(node.value + v, new_stos, 2, v, visit_first, visit_second, node.first_not_moves, node.second_not_moves))
        if node.player == 2:
            visit_first = node.list_visit_first.copy()
            visit_second = node.list_visit_second.copy()
            visit_second.append(k)
            node.add_child(Node(node.value - v, new_stos, 1, v, visit_first, visit_second, node.first_not_moves, node.second_not_moves))


def minmax(node):
    moves = get_all_possible_moves(node)
    if not moves:
        if node.player == 1:
            node.first_not_moves = True
        else:
            node.second_not_moves = True
        # Sprawdzamy czy to tylko 1 gracz nie ma ruchu (wtedy dodajemy dziecko do Noda zmieniajac gracza) czy juz 2 graczy nie ma ruchu (koniec rozgrywki - zwracamy wartosc)
        if node.first_not_moves and node.second_not_moves:
            return node.value
        else:
            if node.player == 1:
                player = 2
                turn_value = 0
                node.add_child(Node(node.value, node.stos.copy(), player, turn_value, node.list_visit_first.copy(), node.list_visit_second.copy(), node.first_not_moves, node.second_not_moves))
            else:
                player = 1
                turn_value = 0
                node.add_child(Node(node.value, node.stos.copy(), player, turn_value, node.list_visit_first.copy(), node.list_visit_second.copy(), node.first_not_moves, node.second_not_moves))
    else:
        generates_children_from_moves(node, moves)
    if node.player == 1:            #1 gracz wykonuje ruch wiec interesuje nas maksymalna wartosc
        value = -1000
        for child in node.children:
            value_result = minmax(child)
            if value_result > value:
                value = value_result
    elif node.player == 2:          #1 gracz wykonuje ruch wiec interesuje nas minimalna wartosc
        value = 1000
        for child in node.children:
            value_result = minmax(child)
            if value_result < value:
                value = value_result
    return value


if __name__ == '__main__':
    print("Konwencja: wartosci dodatnie - przewaga 1 gracza, wartosci ujemne - przewaga 2 gracza (czyli np. -1 oznacza ze gracz 2 wygral majac o 1 monete więcej).")
    case_1 = [2,2,2]  #liczba monet w stosie a,b,c
    case_2 = [3,3,3]
    case_3 = [1,2,6]
    list_of_cases = [case_1, case_2, case_3]
    for case in list_of_cases:
        dict_of_stack = {'a': case[0], 'b': case[1], 'c': case[2]}
        print("Case: ", dict_of_stack)
        if case[0] == case[1] == case[2]:
            list_of_visited_first = []
            dict_of_stack['a'] -= 1
            list_of_visited_first.append('a')
            root = Node(1, dict_of_stack, 2, 1, list_of_visited_first, [])
            print("Result: ", minmax(root))
        else:
            # Tutaj musimy od poczatku isc gdyz drzewo nie bedzie symetryczne
            print("Result: ", minmax(Node(0, dict_of_stack, 1, 0, [], [])))
