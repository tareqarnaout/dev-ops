---
layout: page
title:  Nov 16
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}
</style>

# List Copying and References

## Example 1: List Assignment

What is the output of the following code?

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
print(b)
```

You might think the output is:
```
[1, 2, 3]
[99, 2, 3]
```
However, the actual output is:
```
[99, 2, 3]
[99, 2, 3]
```

This happens because when we do `b = a`, we are not creating a new copy of the list. Instead, both `a` and `b` refer to the same list in memory. Therefore, modifying `b` also affects `a`.

Here is a visualization of what happens in memory:

<div class="pt-container"> <iframe src="https://pythontutor.com/iframe-embed.html#code=a%20%3D%20%5B1%2C%202%2C%203%5D%0Ab%20%3D%20a%0Ab%5B0%5D%20%3D%2099%0Aprint(a)%0Aprint(b)&py=3&curInstr=0&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false"></iframe></div>

To make an actual copy of the list, you can use one of the following methods:
```python
# Method 1: Using the list() function
b = list(a)

# Method 2: Use slicing
# A slice is a list containing copied elements 
# from the original list
b = a[:]

# Method 3: Using the copy() method
b = a.copy()
```

## Example 2: Function Argument Passing

What happens when you pass a list to a function? 

Let's begin by studying the following code:

```python
def fun(a):
    a[0] = 42
    print("Inside fun:", a)

a = [1, 2, 3]
fun(a)
print("After fun:", a)
```

The output will be:
```
Inside fun: [42, 2, 3]
After fun: [42, 2, 3]
```

Why did modifying `a` in the function modify `a` outside the function? Shouldn't there be two separate `a`'s, one in the global frame and another local to `fun`? The answer is yes, but both `a`'s are **references** to the same list.

If you visualize the execution of the code, you will see that sending a list to a function passes a reference to that list, not a copy of the list itself.

<div class="pt-container"> <iframe src="https://pythontutor.com/iframe-embed.html#code=def%20fun(a)%3A%0A%20%20%20%20a%5B0%5D%20%3D%2042%0A%20%20%20%20print(%22Inside%20fun%3A%22%2C%20a)%0A%0Aa%20%3D%20%5B1%2C%202%2C%203%5D%0Afun(a)%0Aprint(%22After%20fun%3A%22%2C%20a)&py=3&curInstr=0&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false"></iframe></div>

## Example 3: Reassigning vs. Modifying

Let's now look at the following example:

```python
def half(a):
    a = a[:len(a) // 2]
    print("Inside the function:", a)

a = [1, 2, 3, 4, 5, 6]
half(a)
print("Outside the function:", a)
```

The output will be:
```
Inside the function: [1, 2, 3]
Outside the function: [1, 2, 3, 4, 5, 6]
```

The statement `a = a[:len(a) // 2]` creates a new list that is half the size of the original list and reassigns the local variable `a` to refer to this new list. This does not affect the original list outside the function.

<div class="pt-container"> <iframe src="https://pythontutor.com/iframe-embed.html#code=def%20half(a)%3A%0A%20%20%20%20a%20%3D%20a%5B%3Alen(a)%20%2F%2F%202%5D%0A%20%20%20%20print(%22Inside%20the%20function%3A%22%2C%20a)%0A%0Aa%20%3D%20%5B1%2C%202%2C%203%2C%204%2C%205%2C%206%5D%0Ahalf(a)%0Aprint(%22Outside%20the%20function%3A%22%2C%20a)&py=3&curInstr=0&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false"></iframe></div>

To understand the difference between modification and reassignment better, consider the following example that combines both:

<div class="pt-container"> <iframe src="https://pythontutor.com/iframe-embed.html#code=def%20fun(a)%3A%0A%20%20%20%20a.append(777)%0A%20%20%20%20a%20%3D%20%5B888%2C%20999%5D%0A%20%20%20%20print(%22Inside%20fun%3A%22%2C%20a)%0A%0Aa%20%3D%20%5B1%2C%202%2C%203%5D%0Afun(a)%0Aprint(%22After%20fun%3A%22%2C%20a)&py=3&curInstr=0&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false"></iframe></div>

Visualize the execution to see how the list is modified and how reassignment works.

<!--
<style>
/* Reusable card style */
.pt-container {
  max-width: 650px;
  margin: 20px auto;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border: 1px solid #e5e5e5;
  background: #fff;
}

.pt-container iframe {
  width: 100%;
  height: 400px;
  border: 0;
  border-radius: 8px;
}
</style>

<div style="max-width:650px;margin:20px auto;font-family:sans-serif;">
  <h3>PythonTutor Embed Generator</h3>
  <textarea id="pt-code" rows="8" style="width:100%;"># Paste your Python code here
a = [1,2,3]
b = a
b[0] = 99
print(a)
print(b)</textarea>
  <button onclick="generateEmbed()" style="margin-top:10px;">Generate Embed</button>

  <h4>Embed code:</h4>
  <textarea id="pt-output" rows="4" style="width:100%;"></textarea>

  <h4>Preview:</h4>
  <div id="pt-preview"></div>
</div>

<script>
function generateEmbed() {
  const code = document.getElementById('pt-code').value;
  const encoded = encodeURIComponent(code);
  const iframeHTML = `
    <div class="pt-container">
      <iframe src="https://pythontutor.com/iframe-embed.html#code=${encoded}&py=3&curInstr=0&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false"></iframe>
    </div>
  `.trim();

  document.getElementById('pt-output').value = iframeHTML;
  document.getElementById('pt-preview').innerHTML = iframeHTML;
}
</script>
-->