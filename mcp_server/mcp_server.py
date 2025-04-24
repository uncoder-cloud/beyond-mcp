import os
import json
import importlib.util
import importlib.machinery

def load_tools(tools_dir):
    tools = {}
    for filename in os.listdir(tools_dir):
        if filename.endswith(".py") and filename != "test_tools.py":
            tool_name = filename[:-3]
            tool_path = os.path.join(tools_dir, filename)
            spec = importlib.util.spec_from_file_location(tool_name, tool_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            tools[tool_name] = module
    return tools

def execute_tool(tool_name, arguments, tools):
    if tool_name not in tools:
        return {"status": "error", "message": f"Tool '{tool_name}' not found."}

    try:
        module = tools[tool_name]
        if tool_name == "memory_tool":
            result = execute_memory_tool(module, arguments)
        elif tool_name == "sequential_thinking_tool":
            result = execute_sequential_thinking_tool(module, arguments)
        elif tool_name == "file_management":
            result = execute_file_management_tool(module, arguments)
        else:
            command = arguments.pop("command")
            result = getattr(module, command)(**arguments)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def execute_memory_tool(module, arguments):
    return module.memory_tool(**arguments)

def execute_sequential_thinking_tool(module, arguments):
    return module.sequential_thinking_tool(**arguments)

def execute_file_management_tool(module, arguments):
    command = arguments.pop("command")
    return getattr(module, command)(**arguments)

def handle_request(request, tools):
    tool_name = request["tool_name"]
    arguments = request["arguments"]
    return execute_tool(tool_name, arguments, tools)

def main():
    tools_dir = os.path.join(os.path.dirname(__file__), "tools")
    tools = load_tools(tools_dir)

    # Read request from file
    with open("request.json", "r") as f:
        request = json.load(f)

    response = handle_request(request, tools)
    print(json.dumps(response))

if __name__ == "__main__":
    main()
