def is_valid(string_of_parentheses: str) -> bool:
    stack = []
    for c in string_of_parentheses:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if c == ")" and top != "(":
                return False
            elif c == "]" and top != "[":
                return False
            elif c == "}" and top != "{":
                return False
    return not stack


def main():
    string_of_parentheses = "{()[]}"
    print(is_valid(string_of_parentheses))


if __name__ == '__main__':
    main()
