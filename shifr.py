# 139232218
def disassemble(commands: str, index: int = 0):
    number: str = ''
    result: str = ''
    while index < len(commands):
        element = commands[index]
        if element.isdigit():
            number += element
        elif element == '[':
            sub_result, new_index = disassemble(commands, index+1)
            result += int(number) * sub_result
            number = ''
            index = new_index
        elif element == ']':
            return result, index
        else:
            result += element
        index += 1
    return result


def main():
    commands: str = input()
    print(disassemble(commands))


if __name__ == '__main__':
    main()
