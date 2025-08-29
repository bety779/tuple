# XI. Filter even numbers from a tuple
def even_tuple(t):
    return tuple(x for x in t if x % 2 == 0)

print(even_tuple((1, 2, 3, 4, 5, 6)))  # (2, 4, 6)


# XII. Sort list of tuples by second element
def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second([('a', 3), ('b', 1)]))  # [('b', 1), ('a', 3)]


# XIII. Flatten a nested list
def flatten_list(lst):
    result = []
    for sub in lst:
        if isinstance(sub, list):
            result.extend(sub)
        else:
            result.append(sub)
    return result

print(flatten_list([[1, 2], [3, 4]]))  # [1, 2, 3, 4]


# XIV. Remove all occurrences of an element from a list
def remove_element(lst, elem):
    return [x for x in lst if x != elem]

print(remove_element([1, 2, 3, 2, 4, 2, 5], 2))  # [1, 3, 4, 5]


# XV. Invert a dictionary (group by values)
def invert_dict(d):
    inv = {}
    for k, v in d.items():
        inv.setdefault(v, []).append(k)
    return inv

print(invert_dict({'a': 1, 'b': 2, 'c': 1}))  # {1: ['a', 'c'], 2: ['b']}


# XVI. Student with highest average
def best_student(marks):
    best = None
    best_avg = -1
    for student, scores in marks.items():
        avg = sum(scores)/len(scores)
        if avg > best_avg:
            best = student
            best_avg = avg
    return best, best_avg

students = {"Alice": [80, 90, 100], "Bob": [70, 60], "Charlie": [95, 85, 90]}
print(best_student(students))  # ('Alice', 90.0)
