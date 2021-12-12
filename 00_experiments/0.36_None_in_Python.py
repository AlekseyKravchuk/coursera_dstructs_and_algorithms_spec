class DontAppend:
    pass



def bad_function(new_elm, starter_list=[]):
    starter_list.append(new_elm)
    print(f'The list: {starter_list} and its ID: {id(starter_list)}')
    return starter_list


def good_function(new_elm, starter_list=None):
    if starter_list is None:
        starter_list = []

    starter_list.append(new_elm)
    print(f'The list: {starter_list} and its ID: {id(starter_list)}')
    return starter_list


if __name__ == '__main__':
    starter_list = [1, 2, 3]
    bad_function(4, starter_list)
    bad_function(6)
    bad_function(100)
