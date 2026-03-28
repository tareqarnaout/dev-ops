---
layout: page
title:  October 7
nav_exclude: true
author: Ibrahim Albluwi
---

# **2.** Introduction to Python
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 7, 2025</span>

{: .tip-title}
> Note
>
> This outline is based on [P4E.1](https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf#page=13.16). However, the chapter has a lot of yada yada that we can ignore. 

## Goals
1. Introduce basic programming concepts.
2. Present the different tools used in the course.
    - Python Environment.
    - VSCode.
    - Python Plugin for VSCode.
    - GitHub Copilot.
3. Write simple Python programs.
    - Use the interactive terminal.
    - Write code in a file and run it.
    - See simple arithmetic operations (full lecture on this later) and simple print statements.
    - See a syntax error, a semantic error, a logic error.


## Terminology to introduce
1. Programming Language.
    - High-level language, Python.
    - Low-level language, machine code.
2. Compiler & Interpreter.
3. Code Editor & IDE.
4. Errors:
    - Syntax Error.
    - Semantic Error.
    - Logic Error.

## Suggested Outline
1. Introduce the meaning of terminology 1-3.<br>
   You can make use of the following website to show the difference between high and low level languages: [https://www.codeconvert.ai/python-to-assembly-converter](https://www.codeconvert.ai/python-to-assembly-converter) (the even/odd example down the page is good to use!)
2. Present each of the tools we will use (relating them to the introduced terminology).
    - **Python**: The programming language we will use. We need to download the interpreter!
      (Downloading Python automatically downloads the interpreter, a simple IDE, standard libraries, etc.)
    - **VS Code**: An IDE that:
        - Provides a code editor with syntax highlighting.
        - Allows running Python programs.
        - Allows installing plugins (e.g., GitHub Copilot).
        - Many other things.
    - **VS Code Python Plugin**: We need to configure VS Code to work with Python.
    - **GitHub Copilot**: Provide AI assistance in coding (autocomplete and chat).

3. Show how to run simple python programs:
    - Open the VSCode terminal and type things like: 
        ```python 
         >>> 1 + 2
         1 + 2
         >>> print('hello')
         hello
         >>> x = 7 + 5
         >>> print(x)
         12
        ````
    - Create a new file and type in it: 
      ```python 
         print('hello') 
         x = 7 + 5
         print(x)
      ```
      Show how to run this program.
4. Show examples of:
    - Syntax errors: 
        - `1 2` (must add an operator between the numbers)
        - `print 'hello'` (must add parentheses)
    - Semantic errors:
        - `print(y)` (what is y?)
    - Logic errors:
        - ```python
             side = 5
             area = side + side
             print(area)
          ```
