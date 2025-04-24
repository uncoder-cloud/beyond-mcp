# beyond-mcp

**Warning: This project is currently under development and may not be stable.**

This project, beyond-mcp, leverages the Model Context Protocol (MCP) to enhance programmer productivity, especially in Artificial Intelligence. It provides a centralized hub for managing and executing development tasks, streamlining workflows, and integrating various tools and services.

## Logo

![Project Logo](/logo.jpg)

## Motivation

This project enhances programmer productivity, especially in AI, by providing a centralized development platform using the Model Context Protocol (MCP).
## Code Structure

*   `mcp_server/mcp_server.py`: Implements the MCP server, handling tool loading, request execution, and client communication.
*   `mcp_server/tools/`: Contains individual tools as Python modules.
*   `mcp_server/tools/analyze_code.py`: Tool for static code analysis.
*   `mcp_server/tools/debug_code.py`: Tool for simulating code debugging.
*   `mcp_server/tools/file_management.py`: Tool for file and directory operations.
*   `mcp_server/tools/generate_code.py`: Tool for generating boilerplate code.
*   `mcp_server/tools/memory_tool.py`: Tool using the memory MCP server.
*   `mcp_server/tools/sequential_thinking_tool.py`: Tool using the sequential thinking MCP server.
*   `mcp_server/tools/task_management.py`: Tool for creating and managing tasks.
*   `mcp_server/tools/test_tools.py`: Unit tests for the tools.
*   `request.json`: Sample JSON request file.
*   `setup.py`: Packaging and distribution file.
*   `requirements.txt`: Project dependencies list.
*   `README.md`: Project overview.
## Available Tools

*   **generate_code:** Generates boilerplate code.
    *   Arguments: `code_type`, `name`, `language` (optional, defaults to "python")
    *   Output: The generated code.
*   **debug_code:** Simulates debugging code.
    *   Arguments: `code`, `breakpoints` (optional, defaults to empty list)
    *   Output: `Debugging started (simulated).`
*   **analyze_code:** Performs static code analysis.
    *   Arguments: `code`
    *   Output: A dictionary containing lists of errors and warnings.
*   **version_control:** Interacts with Git.
    *   Arguments: `command`, `repo_path` (optional, defaults to current directory)
    *   Output: The output of the Git command.
*   **task_management:** Manages tasks.
    *   **create_task:** Creates a new task.
        *   Arguments: `name`, `description`, `priority` (optional, defaults to "medium")
        *   Output: `Task created`
    *   **list_tasks:** Lists all tasks.
        *   Arguments: None
        *   Output: A list of tasks with their names, descriptions, priorities, and statuses.
    *   **update_task_status:** Updates the status of a task.
        *   Arguments: `name`, `status`
        *   Output: `Task status updated`
    *   **delete_task:** Deletes a task.
         *   Arguments: `name`
         *   Output: `Task deleted`
*   **memory_tool:** Uses the memory MCP server.
    *   **add:** Adds a new observation.
        *   Arguments: `action`, `entity_name`, `content`, `entity_type` (optional)
        *   Output: The response from the memory MCP server.
    *   **get:** Searches for entities and returns observations.
         *   Arguments: `action`, `entity_name`, `entity_type` (optional), `keywords` (optional), `limit` (optional, defaults to 5)
         *   Output: The response from the memory MCP server.
*   **sequential_thinking_tool:** Uses the sequential thinking MCP server.
    *   Arguments: `thought`, `nextThoughtNeeded`, `thoughtNumber`, `totalThoughts`, `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts`
    *   Output: The response from the sequentialthinking MCP server.
*   **file_management:** Manages files and directories.
    *   **create_file:** Creates a new file.
        *   Arguments: `path`, `content`
        *   Output: `File '{path}' created`
    *   **read_file:** Reads the content of a file.
        *   Arguments: `path`
        *   Output: The content of the file.
    *   **write_file:** Writes content to a file.
        *   Arguments: `path`, `content`
        *   Output: `File '{path}' written`
    *   **delete_file:** Deletes a file.
        *   Arguments: `path`
        *   Output: `File '{path}' deleted`
    *   **create_directory:** Creates a new directory.
        *   Arguments: `path`
        *   Output: `Directory '{path}' created`
    *   **delete_directory:** Deletes a directory.
        *   Arguments: `path`
        *   Output: `Directory '{path}' deleted`
    *   **list_directory:** Lists the contents of a directory.
        *   Arguments: `path`
        *   Output: A comma-separated list of the files and directories in the specified directory.
    *   **file_exists:** Checks if a file exists.
        *   Arguments: `path`
        *   Output: `True` if the file exists, `False` otherwise.
    *   **directory_exists:** Checks if a directory exists.
        *   Arguments: `path`
        *   Output: `True` if the directory exists, `False` otherwise.

## Usage

Send a JSON request to the MCP server:
```json
{
    "tool_name": "tool_name",
    "arguments": {
        "arg1": "value1",
        "arg2": "value2"
    }
}
```

