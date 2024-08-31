def calculate_structure_sum(data):
    total = 0
    if isinstance(data, list):
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, set):
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for keys in data.keys():
            total += calculate_structure_sum(keys)
        for value in data.values():
            total += calculate_structure_sum(value)
    elif isinstance(data, tuple):
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, int):
        total += data
    elif isinstance(data, str):
        total += len(data)
    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
