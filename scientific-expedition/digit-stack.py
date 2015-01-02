def digit_stack(commands):
    stack = []
    total = 0

    for command in commands:
        if 'PUSH' in command:
            push, number = command.split()
            stack.append(int(number))
        elif command == 'POP':
            if len(stack) > 0:
                total += stack.pop()
        elif command == 'PEEK':
            if len(stack) > 0:
                total += stack[-1]

    return total

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
