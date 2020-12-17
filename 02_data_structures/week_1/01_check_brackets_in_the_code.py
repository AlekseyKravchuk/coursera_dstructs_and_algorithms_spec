from collections import namedtuple


def isBalanced(s):
    Elm = namedtuple('Elm', ['open_bracket', 'idx'])
    d = {'[': ']',
         '{': '}',
         '(': ')'}
    stack = []

    for idx, ch in enumerate(s):
        if ch in d.keys():  # if OPENING bracket occurs
            stack.append(Elm(ch, idx))
        if ch in d.values():  # if CLOSING bracket occurs
            if stack:  # if stack containing opening brackets is NOT empty
                tpl = stack.pop()
                if d[tpl.open_bracket] != ch:
                    return idx + 1
            else:  # if opening stack IS EMPTY
                return idx + 1
    if stack:  # if some brackets left unmatched in stack
        return stack.pop().idx + 1
    else:
        return 0


def main():
    s = input()
    res = isBalanced(s)
    print(res if res else 'Success')


if __name__ == '__main__':
    main()
