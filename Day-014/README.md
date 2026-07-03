# 📅 Day 014

# Problem

The Invisibility Cloak Catastrophe

Repair the corrupted Hogwarts enchantment engine by fixing syntax errors, logical mistakes, missing statements, and runtime issues.

---

## Objectives

- Validate magical spells.
- Hide student names using '*'.
- Unlock the scroll only if the password is a palindrome.
- Display initials.
- Match the expected output exactly.

---

# Bugs Fixed

## Bug 1

### Problem

Python indentation was missing.

### Fix

Properly indented every block.

---

## Bug 2

### Problem

Palindrome check used:

```python
clean == clean[::1]
```

This compares the string with itself.

### Fix

```python
clean == clean[::-1]
```

---

## Bug 3

### Problem

Scroll unlocked message was missing.

### Added

```python
print("Scroll unlocked!")
```

---

## Bug 4

### Problem

Initials were created but never printed.

### Added

```python
print("Initials:", initials)
```

---

## Bug 5

### Problem

Program continued even after an invalid spell.

### Fix

```python
return
```

after printing "Invalid spell!"

---

# Concepts Learned

- Debugging
- Python Indentation
- List Comprehension
- String Reversal
- Palindrome Checking
- Early Return

---

# Complexity

Time Complexity : O(n)

Space Complexity : O(n)

---

## ✅ Status

✔ Completed

**Language Used:** Python 🐍