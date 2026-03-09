# Day 3 — Loops & Conditional Statements

> **DSA Partner Challenge** | Week 1: Language Basics + Maths for DSA

---

## 📌 Topic of the Day

##notes : https://drive.google.com/file/d/1v3HDmEBw5-Mc1zVyB6-mgiBOqnMcBiTG/view?usp=sharing

**Loops & Conditional Statements — keeping it light, making it stick**

Conditionals decide *what* to do. Loops decide *how many times* to do it. Together they power almost every algorithm you'll ever write.

---

## 🎥 Resource

| Language | Resource |
|----------|----------|
| ☕ Java | [Loops & Conditionals — Tutorial](https://youtu.be/ldYLYRNaucM?si=_rqKIyyeEVk5Xmbf) |
| 🐍 Python | Same concepts — find equivalent in CampusX 100 Days of Python |
| ⚙️ C++ | Same concepts — Love Babbar / Striver playlist |

---

## 🧠 What to Learn Today

### Conditional Statements

**if / else if / else**
- Checks a boolean condition — only ONE branch runs
- Java/C++: `if (condition) {}` | Python: `if condition:`
- Common mistake: `=` is assignment, `==` is comparison

**Ternary Operator**
- One-line if-else: `int max = (a > b) ? a : b;`
- Python: `max_val = a if a > b else b`
- Use for simple conditions only — don't nest ternaries

**switch Statement (Java & C++)**
- Cleaner than long if-else chains for exact value matching
- Always add `break` — without it, execution falls through to the next case
- Python has no switch — use `if-elif` or a dictionary

---

### Loops

**for loop** — use when you know the count
```java
for (int i = 0; i < 5; i++) { }         // Java / C++
```
```python
for i in range(5):     # 0–4
for i in range(1, 6):  # 1–5
for i in range(0, 10, 2):  # 0,2,4,6,8
```

**while loop** — use when you don't know the count
```java
while (condition) { }   // Java / C++
```
```python
while condition:        # Python
```
- Always ensure the condition eventually becomes false — or you get an infinite loop

**do-while** — runs body at least once, then checks condition
```java
do { } while (condition);   // Java & C++ only
```
- Python has no do-while — simulate with `while True: ... if cond: break`

**break and continue**

| Keyword | What it does |
|---------|-------------|
| `break` | Immediately exits the loop |
| `continue` | Skips current iteration, goes to next |

**Nested Loops**
- A loop inside a loop
- Two nested loops = O(n²) — be aware of this in DSA

---

## 💻 Practice Questions

Solve in Java (or your language). Push solutions to your fork.

**1.** Area of Circle
> Formula: π × r²  (use Math.PI in Java)

**2.** Area of Triangle
> Formula: ½ × base × height

**3.** Area of Rectangle
> Formula: length × breadth

**4.** Area of Isosceles Triangle
> Formula: ½ × base × height

**5.** Area of Parallelogram
> Formula: base × height

**6.** Area of Rhombus
> Formula: ½ × d1 × d2  (d1 and d2 are the diagonals)

**7.** Area of Equilateral Triangle
> Formula: (√3 / 4) × side²

**8.** Perimeter of Circle (Circumference)
> Formula: 2 × π × r

**9.** Perimeter of Equilateral Triangle
> Formula: 3 × side

**10.** Perimeter of Parallelogram
> Formula: 2 × (a + b)  (a and b are adjacent sides)

> 💡 For all questions: take input from the user, calculate, and print the result rounded to 2 decimal places.

---

## ✅ Checklist Before You Sleep

- [ ] I understand how if / else if / else flows
- [ ] I know the difference between `=` and `==`
- [ ] I can write a ternary operator
- [ ] I know when to use switch vs if-else
- [ ] I know the for loop structure: init ; condition ; update
- [ ] I understand while vs do-while
- [ ] I know what `break` and `continue` do
- [ ] Solved at least 6 of the 10 practice questions

---

## 💬 Community

Stuck on any formula or syntax? Drop it in the community.

**Solved all 10? Drop a 🔥 in the community.**

---

*Next up → Day 4: Functions, Methods & Introduction to Recursion*
