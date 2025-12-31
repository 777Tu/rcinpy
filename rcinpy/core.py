import os
import subprocess as sub
import tempfile
import shutil
from typing import Union, Any

__author__ = "Tuscott"

class CinpyError(Exception):
    """Custom exception for cinpy related errors."""
    pass

def cpy(pcode: str, *args: Any) -> str:
    """
    Compiles and executes C code or a C file.
    Usage: cpy("main.c", "arg1", 2, 3.5)
    """
    if not shutil.which("gcc"):
        raise CinpyError("GCC compiler not found. Please install build-essential.")

    if os.path.exists(pcode):
        with open(pcode, "r") as f:
            fcode = f.read()
    else:
        fcode = pcode

    with tempfile.TemporaryDirectory() as tmpdir:
        c_source = os.path.join(tmpdir, "main.c")
        binary = os.path.join(tmpdir, "runbin")

        with open(c_source, "w") as f:
            f.write(fcode)

        try:
            sub.run(["gcc", c_source, "-o", binary], check=True, capture_output=True, text=True)
            str_args = [str(a) for a in args]
            result = sub.run([binary] + str_args, capture_output=True, check=True, text=True)
            return result.stdout
        except sub.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else e.stdout
            raise CinpyError(f"C Error: {error_msg}")
