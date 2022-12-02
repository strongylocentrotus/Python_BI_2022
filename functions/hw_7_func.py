import sys

def sequential_map (*args):
    *funcs , numbers = args
    for func in funcs:
        cont = list(map(func, numbers))
    return cont

def consensus_filter (*args):
    *funcs , numbers = args
    for func in funcs:
        cont = list(filter(func, numbers))
    return cont

def conditional_reduce (func_1, func_2, cont):
    cont = list(filter(func_1, cont))
    result = cont[0]
    for anoth in cont[1:]:
        result = func_2(result, anoth)
    return result

def func_chain (*args):
    def new_chain(numbers):
        ant = args[0](numbers)
        for i in range(1, len(args)):
            ant = args[i](ant)
        return ant
    return new_chain

def sequential_map_two (*args):
    *funcs , numbers = args
    chain = func_chain(*funcs)
    return chain(numbers)

def my_print (*args, sep=' ', end='\n', file=sys.stdout):
    for i in range(len(args)):
        file.write(str(args[i]))
        if i != len(args) - 1:
            file.write(sep)
        else:
            file.write(end)
