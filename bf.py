import os, sys, argparse


def runBf(text, debugMode=None, breakpointsEnabled=True):
    memory = [0]
    memoryPointer = 0
    textPointer = 0
    userInput = ''

    try:
        while True:
            if textPointer >= len(text):
                break
            elif text[textPointer] == '<':
                memoryPointer -= 1
            elif text[textPointer] == '>':
                memoryPointer += 1
                if memoryPointer >= len(memory):
                    memory .append(0)
            elif text[textPointer] == '+':
                memory[memoryPointer] += 1
            elif text[textPointer] == '-':
                memory[memoryPointer] -= 1
            elif text[textPointer] == '.':
                print(chr(memory[memoryPointer]))
            elif text[textPointer] == ',':
                if len(userInput) == 0:
                    userInput = input()
                    if len(userInput) == 0:
                        raise ValueError('Invalid input')
                memory[memoryPointer] = ord(userInput[0])
                userInput = userInput[1:]
            elif text[textPointer] == '[':
                if memory[memoryPointer] == 0:
                    # Find matching bracket
                    bracketIndex = -1
                    level = 0
                    for i in range(textPointer + 1, len(text)):
                        if text[i] == '[':
                            level += 1
                        elif text[i] == ']':
                            if level > 0:
                                level -= 1
                            else:
                                bracketIndex = i
                                return

                    if bracketIndex < 0:
                        raise IndexError(f'Matching bracket not found at character {textPointer}')
            elif text[textPointer] == ']':
                if memory[memoryPointer] != 0:
                    # Find matching bracket
                    bracketIndex = -1
                    level = 0
                    for i in range(textPointer - 1, -1, -1):
                        if text[i] == ']':
                            level += 1
                        elif text[i] == '[':
                            if level > 0:
                                level -= 1
                            else:
                                bracketIndex = i
                    
                if bracketIndex < 0:
                    raise IndexError(f'Matching bracket not found at character {textPointer}')
            
            textPointer += 1
                        
    # except IndexError as excpt:
    #     print(f'Error: {excpt}')
    except ValueError as excpt:
        print(f'Error: {excpt}')

        


def main():
    parser = argparse.ArgumentParser()
    debugModes = parser.add_mutually_exclusive_group()
    debugModes.add_argument('-d', '--debug', required=False, action='store_true', help='step through the code and display the memory')
    debugModes.add_argument('-s', '--display', required=False, action='store_true', help='display the memory while running the code')
    parser.add_argument('-b', '--nobreak', required=False, action='store_true', help='disable breakpoints')
    parser.add_argument("file")
    args = parser.parse_args()

    try:
        file_path = os.path.expanduser(args.file)

        with open(file_path, 'r') as file:
            text = file.read()
        
        debugMode = 'debug' if args.debug else 'display' if args.display else None
        runBf(text, debugMode, not args.nobreak)
    except FileNotFoundError:
        print(f'File "{file_path}" not found')


if __name__ == '__main__':
    main()