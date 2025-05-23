import os

def create_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
        return f"File '{path}' created"
    except Exception as e:
        return str(e)

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)

def write_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
        return f"File '{path}' written"
    except Exception as e:
        return str(e)

def delete_file(path):
    try:
        os.remove(path)
        return f"File '{path}' deleted"
    except Exception as e:
        return str(e)

def create_directory(path):
    try:
        os.mkdir(path)
        return f"Directory '{path}' created"
    except Exception as e:
        return str(e)

def delete_directory(path):
    try:
        os.rmdir(path)
        return f"Directory '{path}' deleted"
    except Exception as e:
        return str(e)

def list_directory(path):
    if not os.path.exists(path):
        return "No such file or directory"
    try:
        contents = os.listdir(path)
        return ", ".join(contents)
    except Exception as e:
        return str(e)
