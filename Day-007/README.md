# 📅 Day 007

# Problem

FIFA World Cup – The Corrupted Goal Tracker

The program contained several logical bugs causing incorrect stadium records, incorrect total goals, incorrect top scorer, and out-of-bounds array access.

---

# Bugs Fixed

## Bug 1

### Problem

Goals for Stadium 2 were being stored in Stadium 1.

### Incorrect Code

```c
goals[1][goalCount[2]] = minute;
```

### Fixed Code

```c
goals[2][goalCount[2]] = minute;
```

---

## Bug 2

### Problem

Loop exceeded array size.

### Incorrect Code

```c
for(int s=0; s<=STADIUMS; s++)
```

### Fixed Code

```c
for(int s=0; s<STADIUMS; s++)
```

---

## Bug 3

### Problem

Top scorer calculation ignored Player 0.

### Fixed

Initialize:

```c
maxG = playerGoals[0];
winner = 0;
```

---

## Bug 4

### Problem

Display function accessed one extra element.

### Incorrect

```c
i <= goalCount[stadium]
```

### Fixed

```c
i < goalCount[stadium]
```

---

# Concepts Learned

- Array Indexing
- Debugging
- Boundary Checking
- Off-by-One Errors
- Array Traversal

---

# Complexity

All functions run in O(n).

---

# Status

✔ Completed