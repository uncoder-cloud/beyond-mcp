def generate_code(code_type, name, language="python"):
    if language == "python":
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
    elif language == "javascript":
        if code_type == "class":
            return f"""
class {name} {{
    constructor() {{

    }}

    method() {{

    }}
}}
"""
        elif code_type == "function":
            return f"""
function {name}() {{

}}
"""
        else:
            return "Invalid code type."
    elif language == "cpp":
        if code_type == "class":
            return f"""
class {name} {{
public:
    {name}() {{

    }}

    void method() {{

    }}
}};
"""
        elif code_type == "function":
            return f"""
void {name}() {{

}}
"""
        else:
            return "Invalid code type."
    else:
        return "Invalid language."
