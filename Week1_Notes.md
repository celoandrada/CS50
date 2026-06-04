# Week 1 — CS50 Python

## Deep Thought

Goal:
Compare user input with a correct answer.

Concept learned:
if + ==

Example similar code learned:

```python
answer = input("Answer: ")

if answer == "42":
    print("Yes")
else:
    print("No")
```

Lesson:
Programs can make decisions based on conditions.

---

## Home Federal Savings Bank

Goal:
Respond differently based on how a greeting starts.

Concept learned:
if + elif + else

Example similar code learned:

```python
greeting = input("Greeting: ").lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
```

Lesson:
Programs can have multiple possible outcomes.

---

## File Extensions

Goal:
Identify file types from their extensions.

Concept learned:
Multiple elif statements

Example similar code learned:

```python
extension = input("Extension: ")

if extension == "jpg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
else:
    print("application/octet-stream")
```

Lesson:
Conditionals can classify information into categories.

---

## Math Interpreter

Goal:
Perform different calculations based on an operator.

Concept learned:
Comparison operators + arithmetic

Example similar code learned:

```python
x = 10
operator = "+"
y = 5

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
```

Lesson:
Programs can choose what calculation to perform.

---

## Meal Time

Goal:
Determine whether it is breakfast, lunch, or dinner time.

Concept learned:
Ranges + Boolean expressions

Example similar code learned:

```python
time = 7.5

if 7 <= time <= 8:
    print("breakfast time")
elif 12 <= time <= 13:
    print("lunch time")
elif 18 <= time <= 19:
    print("dinner time")
```

Lesson:
Conditions can check if a value falls inside a range.

---

## New Concepts Learned

### Comparison Operators

Concept learned:
Comparing values

Example similar code learned:

```python
score = 75

if score >= 60:
    print("Pass")
```

Lesson:
Conditions become either True or False.

---

### If Statements

Concept learned:
if

Example similar code learned:

```python
age = 20

if age >= 18:
    print("Adult")
```

Lesson:
Runs code only when a condition is True.

---

### Elif Statements

Concept learned:
elif

Example similar code learned:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
```

Lesson:
Checks another condition if the previous one was False.

---

### Else Statements

Concept learned:
else

Example similar code learned:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Lesson:
Provides a default outcome.

---

### Or

Concept learned:
or

Example similar code learned:

```python
animal = input("Animal: ")

if animal == "dog" or animal == "cat":
    print("Pet")
```

Lesson:
Only one condition needs to be True.

---

### And

Concept learned:
and

Example similar code learned:

```python
age = 20
gpa = 3.5

if age >= 18 and gpa >= 3.0:
    print("Eligible")
```

Lesson:
Both conditions must be True.

---

### Boolean Values

Concept learned:
True and False

Example similar code learned:

```python
is_even = True

if is_even:
    print("Even")
```

Lesson:
Conditionals work using Boolean values.

---

### Modulus Operator

Goal:
Find the remainder after division.

Concept learned:
%

Example similar code learned:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Lesson:
% is commonly used to check patterns like even and odd numbers.

---

### Match / Case

Goal:
Create cleaner alternatives to many if statements.

Concept learned:
match + case

Example similar code learned:

```python
house = "Harry"

match house:
    case "Harry":
        print("Gryffindor")
    case _:
        print("Unknown")
```

Lesson:
match makes multiple condition checks easier to read.

---

Big lesson this week:
Week 0 taught how to store and manipulate information.

Week 1 taught how programs make decisions.

Conditionals allow programs to react differently based on user input, which is what makes software interactive.
