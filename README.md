# 🚀 rcinpy

**rcinpy** is a lightweight Python bridge that lets you execute C code directly from Python without manual compilation. It handles GCC compilation in the background and cleans up generated binaries automatically.

---

## ✨ Features
- Run raw C strings (no temporary file required).
- Execute `.c` files by path.
- Automatic compilation using `gcc`.
- Converts Python arguments to C `argv` strings.
- Auto-removes temporary binaries after execution.

---

## 🛠 Installation

> Make sure you have `git`, `python` (and `pip`) and `gcc` installed on your system.

```bash
pip install git+https://github.com/777Tu/rcinpy.git
```

- Termux example (if `git` is not installed):
```bash
pkg update -y
pkg install -y git python gcc
pip install git+https://github.com/777Tu/rcinpy.git
```

---

## 🚀 Usage

Import the package and call `rcinpy.cpy(...)`. The function accepts either:
- a filename (path to a `.c` file), or
- a string containing C source code.

Any extra positional arguments passed to `rcinpy.cpy(...)` are forwarded as `argv` (all converted to strings). The function returns the program's stdout as a Python string.

### Running a C file
```python
import rcinpy

# 1. Prepare your C file
c_file = "example.c"
c_code_content = """
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Hello, world!\\n");
    if (argc > 1) {
        printf("Arguments received:\\n");
        for (int i = 1; i < argc; i++) {
            printf("%s\\n", argv[i]);
        }
    }
    return 0;
}
"""

with open(c_file, "w") as f:
    f.write(c_code_content)

# 2. Execute the C file and capture stdout
result = rcinpy.cpy(c_file, "Alice", 77)
print(result)
```

### Running C code from a string
```python
import rcinpy

c_code_str = """
#include <stdio.h>

int main() {
    printf("Hello from string code!\\n");
    return 0;
}
"""

result = rcinpy.cpy(c_code_str)
print(result)  # "Hello from string code!\n"
```

---

## 📦 API (short)
- `rcinpy.cpy(source, *args)`  
  - `source`: path to a `.c` file OR a string containing C source code.  
  - `*args`: additional values forwarded to the compiled program as `argv` (all cast to strings).  
  - Returns: stdout of the program as `str`. Raises on compilation/runtime failure (see implementation for exact exceptions).

---

## ⚠️ Notes & Constraints
- Requires `gcc` on PATH.
- Arguments are passed as strings only (no complex type marshalling).
- Temporary binaries are removed after execution.
- Use carefully with untrusted code—executing arbitrary C is dangerous.

---

## 🧾 License
MIT

---

## 📎 Links
- Repository: [rcinpy on GitHub](https://github.com/<username>/rcinpy)
