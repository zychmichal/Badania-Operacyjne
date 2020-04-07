import numpy as np
from scipy.optimize import linprog
import math


"""OPIS PROBLEMU:

f(x1,x2) = 23x1 + 17x2 ----> max

4x1 + 3x2 <=190
x1 + x2 <=55

x1, x2 naleza do liczb naturalnych
"""

global_list_of_task = []
global_free_id = 1


class Task:
    def __init__(self, id, value, is_good, A, b, c, bad_index, result):
        self.id = id
        self.value = value
        self.is_good = is_good
        self.A = A
        self.b = b
        self.c = c
        self.bad_index = bad_index
        self.result = result.copy()

    @classmethod
    def createTask(cls, A, b, c, id):
        x_b = (0, None)
        res = linprog(c, A, b, bounds=(x_b, x_b))
        if not res.success:
            return cls(id, None, res.success, A, b, c, None, res.x)
        result = [round(x, 3) for x in res.x]
        is_good, bad_index = Task.check_if_results_are_int(result)
        return cls(id, round(res.fun, 3), is_good, A, b, c, bad_index, result)

    @staticmethod
    def check_if_results_are_int(results):
        for i in range(0, len(results)):
            if not math.isclose(round(results[i], 0), results[i], abs_tol=1e-5):
                return False, i
        return True, None

    def __eq__(self, other):
        return self.value == other.value and self.result[0] == other.result[0] and self.result[1] == other.result[1]

    def __repr__(self):
        return "is_g: " + str(self.is_good) +" v: " + str(self.value) + " r: " + str(self.result)


def divide_task(A, b, result, bad_index):
    l1, l2 = prepare_lists_to_append(result, bad_index)
    A1 = A.copy()
    A2 = A.copy()
    A1.append(l1)
    A2.append(l2)
    b1 = b.copy()
    b2 = b.copy()
    b1.append(math.floor(result[bad_index]))
    b2.append(-(math.floor(result[bad_index]) + 1))
    return A1, b1, A2, b2


def prepare_lists_to_append(results, index_of_bad):
    list1 = []
    list2 = []
    for i in range(0, len(results)):
        if i == index_of_bad:
            list1.append(1)
            list2.append(-1)
        else:
            list1.append(0)
            list2.append(0)
    return list1, list2


def delete_unnecessary_task_from_list():
    min_f = 0
    index = 0
    for task in global_list_of_task:
        if task.is_good:
            if task.value < min_f:
                min_f = task.value
                index = task.id

    to_delete = []

    for task in global_list_of_task:
        if not task.value or (task.value >= min_f and index != task.id):
            to_delete.append(task)

    for task in to_delete:
        global_list_of_task.remove(task)


def count_int():
    global global_free_id
    if len(global_list_of_task) == 1 and global_list_of_task[0].is_good:
        return global_list_of_task[0]
    if len(global_list_of_task) == 0:
        return "Problem nie da sie rozwiazac programowaniem liniowym"

    actual_task = None

    for task in global_list_of_task:
        if not task.is_good:
            actual_task = task
            break

    A1, b1, A2, b2 = divide_task(actual_task.A, actual_task.b, actual_task.result, actual_task.bad_index)

    T1= Task.createTask(A1, b1, c, global_free_id + 1)
    T2= Task.createTask(A2, b2, c, global_free_id + 2)

    global_list_of_task.append(T1)
    global_list_of_task.append(T2)

    global_free_id += 2

    global_list_of_task.remove(actual_task)

    delete_unnecessary_task_from_list()
    return count_int()


c = [-23, -17]
A = [[4, 3], [1, 1]]
b = [190, 55]


T1 = Task.createTask(A, b, c, 1)
global_list_of_task.append(T1)



best_task = count_int()

print("Liczba lancuszkow: " + str(best_task.result[0]))
print("Liczba pierscionkow: " + str(best_task.result[1]))
print("Zysk: " + str(-best_task.value))



