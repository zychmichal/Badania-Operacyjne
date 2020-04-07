import numpy as np

M = np.array([[20, -150, -250],[150, -80, -100],[250, 100, 40]])


def find_minmax_for_1_player(M):
  list_of_min = []
  for row in M:
    list_in_row = []
    for j in row:
      list_in_row.append(j)
    list_of_min.append(min(list_in_row))
  return max(list_of_min)

def find_minmax_for_2_player(M):
  list_of_max = []
  for column in M.T:
    list_in_column = []
    for j in column:
      list_in_column.append(j)
    list_of_max.append(max(list_in_column))
  return min(list_of_max)


minmax_1 = find_minmax_for_1_player(M)
minmax_2 = find_minmax_for_2_player(M)
print(minmax_1)
print(minmax_2)

if minmax_1 == minmax_2:
  print("Obydwie wartosci minmax sa rowne wiec powinni wybrac ta strategie (A3,B3) wedlug rownowagi Nasha")

