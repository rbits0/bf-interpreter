import os, sys, argparse


def runBf(text, debugMode=None, breakpointsEnabled=True, numColumns = 1):
    memory = [0] * numColumns
    memoryPointer = 0
    textPointer = 0
    userInput = ''
    
    try:
        while True:
            validChar = True

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
                if debugMode is not None:
                    print('Output:', chr(memory[memoryPointer]), ':', memory[memoryPointer])
                else:
                    print(chr(memory[memoryPointer]), end='')
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
                    else:
                        textPointer = bracketIndex
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
                    else:
                        textPointer = bracketIndex
            else:
                validChar = False
            
            if debugMode is not None and validChar:
                print(text[textPointer], ':', ' '.join([str(x) for x in memory]))
                print('    ' + ''.join([' ' * (len(str(x)) + 1) for x in memory[:memoryPointer]])+ '^') # Correct padding for pointer

            if debugMode == 'debug': 
                input()

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
    parser.add_argument('-n', required=False, help='number of columns if debug or display is enabled')
    parser.add_argument("file")
    args = parser.parse_args()

    try:
        file_path = os.path.expanduser(args.file)

        with open(file_path, 'r') as file:
            text = file.read()
        
        debugMode = 'debug' if args.debug else 'display' if args.display else None
        numColumns = args.n if args.n else 50 if debugMode else 1
        runBf(text, debugMode, not args.nobreak, numColumns)
    except FileNotFoundError:
        print(f'File "{file_path}" not found')


if __name__ == '__main__':
    main()