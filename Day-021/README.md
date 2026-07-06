# 📅 Day 021

# Problem

The Avengers Assembly Glitch

A linked list implementation contains multiple logical bugs. Fix the code so that:

- Heroes are inserted correctly.
- The linked list prints correctly.
- Hero deletion works.
- Middle hero is found correctly.

---

# Bugs Fixed

## Bug 1

### Problem

When inserting the first hero, the head pointer was never updated.

### Incorrect

```c
if(head==NULL){
    return;
}
```

### Fixed

```c
if(head==NULL){
    head=newNode;
    return;
}
```

---

## Bug 2

### Problem

The new node's next pointer wasn't initialized.

### Fixed

```c
newNode->next=NULL;
```

---

## Bug 3

### Problem

Display loop used

```c
while(temp!=head)
```

which never prints anything.

### Fixed

```c
while(temp!=NULL)
```

---

## Bug 4

### Problem

Wrong memory was freed.

### Incorrect

```c
free(prev);
```

### Fixed

```c
free(temp);
```

---

## Bug 5

### Problem

Fast pointer moved only one step.

### Incorrect

```c
fast=fast->next;
```

### Fixed

```c
fast=fast->next->next;
```

---

# Concepts Learned

- Debugging
- Linked List
- Memory Management
- Pointer Manipulation
- Fast & Slow Pointer
- Node Deletion

---

# Complexity

Insert : O(n)

Delete : O(n)

Display : O(n)

Find Middle : O(n)

---

## ✅ Status

✔ Completed

**Language Used:** C