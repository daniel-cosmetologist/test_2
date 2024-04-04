####################################################

# B. Создание упорядоченного словаря из двух списков

####################################################

def lists_to_ordered_dict(keys, values):
    if len(keys) != len(values):
        return dict(sorted(zip(keys, values)))
    else:
        print("Длины списков должны быть разными.")
        return None

def run():
    print(lists_to_ordered_dict(['b', 'a', 'c'], [2, 1]))
    print(lists_to_ordered_dict(['alpha', 'theta'], [13, 28]))