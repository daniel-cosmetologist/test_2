########################################################

# C. Преобразование списка с использованием map и lambda

########################################################

def transform_list(input_list):
    return list(map(lambda x: f"abc_{x}_cba" if isinstance(x, str) else x**2, input_list))

def run():
    print(transform_list(['text', 2, 'another', 3]))