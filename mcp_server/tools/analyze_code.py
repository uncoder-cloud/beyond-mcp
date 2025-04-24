import subprocess
import os

def analyze_code(code):
    # Create a temporary file to store the code
    with open("temp_code.py", "w") as f:
        f.write(code)

    # Run flake8 on the temporary file
    process = subprocess.run(["flake8", "temp_code.py"], capture_output=True, text=True)

    # Extract the errors and warnings from the output
    output = process.stdout
    errors = []
    warnings = []
    for line in output.splitlines():
        if "E" in line:
            errors.append(line)
        elif "W" in line:
            warnings.append(line)

    # Clean up the temporary file
    os.remove("temp_code.py")

    # Return the errors and warnings
    return {"errors": errors, "warnings": warnings}
