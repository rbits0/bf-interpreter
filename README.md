# bf-interpreter
A brainfuck interpreter in Python, with debugging and functions

## Usage
python ./bf.py [-d] [-s] [-n N] [-b] [-f] file.bf

-s displays the memory while running the code

-d steps through the code while displaying the memory

-n is the number of memory locations to display when using -d or -s

-b disables breakpoints

-f disables functions

## Breakpoints and functions
"*" will create a breakpoint

"*def myFunction" will define a function

"*func myFunction" will jump to a function

"*return" will return to where you jumped from

Remember to include the "*" before those keywords

## Comments
Any text that does not include <>+-.,[]* will be treated as a comment