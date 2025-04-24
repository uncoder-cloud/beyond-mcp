def generate_code(code_type, name):
    if code_type == "class":
        return f"""
class {name}:
    def __init__(self):
        pass

    def method(self):
        pass
"""
    elif code_type == "function":
        return f"""
def {name}():
    pass
"""
    else:
        return "Invalid code type."
