# mcp-project
# mcp-project

**Warning: This project is currently under development and may not be stable.**

This is a test MCP (Model Context Protocol) project that provides a set of tools to boost programmer productivity.

## Available Tools

*   **hello_world:** A simple tool that returns a greeting.
    *   Arguments: `name`
    *   Output: `Hello, {name}!`
*   **generate_code:** A tool that generates boilerplate code for common tasks.
    *   Arguments: `code_type`, `name`
    *   Output: The generated code.
*   **debug_code:** A tool that allows users to simulate debugging code.
    *   Arguments: `code`, `breakpoints`
    *   Output: `Debugging started (simulated).`
*   **analyze_code:** A tool that performs static analysis to identify potential errors and code quality issues.
    *   Arguments: `code`
    *   Output: A dictionary containing lists of errors and warnings.
*   **version_control:** A tool that interacts with Git to perform common version control operations.
    *   Arguments: `command`
    *   Output: The output of the Git command.
*   **task_management:** A tool that allows users to create and manage tasks.
    *   **create_task:** Creates a new task.
        *   Arguments: `name`, `description`
        *   Output: `Task created`
    *   **list_tasks:** Lists all tasks.
        *   Arguments: None
        *   Output: A list of tasks with their names, descriptions, and statuses.
    *   **update_task_status:** Updates the status of a task.
        *   Arguments: `name`, `status`
        *   Output: `Task status updated`
*   **memory_tool:** A tool that uses the memory MCP server to store and retrieve information.
    *   **add:** Adds a new observation to the entity.
        *   Arguments: `action`, `entity_name`, `content`
        *   Output: The response from the memory MCP server.
    *   **get:** Searches for the entity and returns its observations.
         *   Arguments: `action`, `entity_name`, `entity_type` (optional), `keywords` (optional)
         *   Output: The response from the memory MCP server.
*   **sequential_thinking_tool:** A tool that uses the sequential thinking MCP server to help with complex tasks.
    *   Arguments: `thought`, `nextThoughtNeeded`, `thoughtNumber`, `totalThoughts`, `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts`
    *   Output: The response from the sequentialthinking MCP server.
*   **file_management:** A tool that allows users to create, read, write, and delete files and directories.
    *   **create_file:** Creates a new file with the specified content.
        *   Arguments: `path`, `content`
        *   Output: `File '{path}' created`
    *   **read_file:** Reads the content of the file.
        *   Arguments: `path`
        *   Output: The content of the file.
    *   **write_file:** Writes the specified content to the specified file.
        *   Arguments: `path`, `content`
        *   Output: `File '{path}' written`
    *   **delete_file:** Deletes the specified file.
        *   Arguments: `path`
        *   Output: `File '{path}' deleted`
    *   **create_directory:** Creates a new directory.
        *   Arguments: `path`
        *   Output: `Directory '{path}' created`
    *   **delete_directory:** Deletes the specified directory.
        *   Arguments: `path`
        *   Output: `Directory '{path}' deleted`
    *   **list_directory:** Lists the contents of the specified directory.
        *   Arguments: `path`
        *   Output: A comma-separated list of the files and directories in the specified directory.

## Usage

To use the tools, send a JSON request to the MCP server with the following format:

```json
{
    "tool_name": "tool_name",
    "arguments": {
        "arg1": "value1",
        "arg2": "value2"
    }
}
```

Replace `tool_name` with the name of the tool you want to use, and replace `arg1` and `arg2` with the arguments required by the tool.

## Example

To use the `hello_world` tool, send the following request:

```json
{
    "tool_name": "hello_world",
    "arguments": {
        "name": "Test User"
    }
}
```
