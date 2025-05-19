# Whitespace Cleaner

This is the most basic text processing script — the starting point of a dataflow framework. It focuses on a **single responsibility**: stripping leading and trailing whitespace from each line of input.

## 📋 Task Description

Build a Python script that:

- Reads input from **stdin** line by line
- **Strips** leading and trailing whitespace
- Writes the cleaned lines to **stdout**

---

## 🧪 Example

### Input:

- Hello World!
- This is line two.
- This is line three.

### Output:

```bash
Hello world
This is a line with spaces
Another one
```

## ▶️ Usage

Run the script by piping input to it:

```bash
cat input.txt | python3 main.py
```

- or

```bash
 python3 main.py
```
