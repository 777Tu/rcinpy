import rcinpy

# Since we put 'cpy' inside __init__.py, you can call it directly
c_code = "#include <stdio.h>\nint main() { printf(\"Package Installed Successfully!\\n\"); return 0; }"

try:
    print(rcinpy.cpy(c_code))
except Exception as e:
    print(f"Error: {e}")

