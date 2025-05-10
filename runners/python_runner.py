import subprocess

def run_python_code(code):
    with open("/tmp/code.py", "w") as f:
        f.write(code)
    result = subprocess.run(["python3", "/tmp/code.py"], capture_output=True, text=True)
    return result.stdout + result.stderr
