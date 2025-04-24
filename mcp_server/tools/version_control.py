import subprocess

def version_control(command):
    try:
        process = subprocess.run(["git"] + command.split(), capture_output=True, text=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
