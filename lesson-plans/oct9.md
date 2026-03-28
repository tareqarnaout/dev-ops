---
layout: page
title:  October 9
nav_exclude: true
author: Ibrahim Albluwi
---

# **3.** Variables & Expressions
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 9, 2025</span>

{: .tip-title}
> Note
>
> This outline is based on [P4E.2](https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf#page=31.16). The expectation is to cover the whole chapter in this lecture.

## Suggested Teaching Method
- Use **interactive live coding** with the students. Don't use slides.
- Rely mostly on the Python `REPL` instead of writing the program in a file, and then clicking on run. This is more efficient.
- You can summarize using very short bullet points on the side of the board, so that students can keep track of what was covered.

## Things To Cover 
1. **Values have types** (e.g., `int`, `str`, `float`, etc.). 
- You can check the type by typing `type(17.5)` or `type('hello')`.
- Knowing the type is important as we will see in the future (e.g. `5` is not the same as `'5'`)

2. **Variables**:
    - Assignment statements.<br>
    Assignment $$\neq$$ equality (e.g., `x = 1` is not the same as `1 = x`).
    - `x = 1` makes `type(x)` an `int`, whereas `x = 1.5` changes it to `float` and `x = 'hello'` changes it to `str`.
    - Variable Naming:
        - Rules.
        - Best Practices (choose good names, use `camelCase` or `snake_case`).
3. **Operators:**
    - `+`, `-`, `*`, `/`, `//`, `**`.
    - Order of operations and operator precedence (Parantheses $$\rightarrow$$ `**` $$\rightarrow$$ `*`, `/`, `//` left-to-right $$\rightarrow$$ `+` and `-`).
    - Modulus operator: `%`.
    - Using `+` and `*` with strings.
4. **Getting User Input**.
    - `name = input()`.
    - `age = int(input())`.
5. **Comments**.
    - Cover `#` only.
    - Explain why they are useful.
    - If there is time, show that comments can act as prompts for GitHub Copilot in VS Code.
6. **Errors**.
    - Show examples of errors:
        - Syntax error: `my age = 20`.
        - Logic Error: `1/2*3.14` (is it `1/(2*3.14)` or `(1/2)*3.14`?)
