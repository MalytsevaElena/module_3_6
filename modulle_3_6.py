def calculate_structure_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, dict):
            for i in list(arg.items()):
                summa += calculate_structure_sum(i)
        elif isinstance(arg, (list, tuple, set)):
            for i in arg:
                summa += calculate_structure_sum(i)
        elif isinstance(arg, str):
            summa += len(arg)
        elif isinstance(arg, int):
            summa += arg
    return summa

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
