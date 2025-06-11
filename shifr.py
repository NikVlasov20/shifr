
set_numbers: list = [str(j) for j in range(0, 10)]


def disassemble(commands: str, i: int = 0):
    number: str = ''
    result: str = ''
    while i < len(commands):
        while commands[i] in set_numbers:
            number += commands[i]
            i += 1
            continue
        if commands[i] == '[':
            i += 1
            sub_result, new_i = disassemble(commands, i)
            result += int(number) * sub_result
            number = ''
            i = new_i
        elif commands[i] == ']':
            i += 1
            return result, i
        else:
            result += commands[i]
            i += 1
    return result


def main():
    commands: str = input()
    print(disassemble(commands))


if __name__ == '__main__':
    main()
