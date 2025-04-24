# beyond-mcp

**Warning: This project is currently under development and may not be stable.**

This is a test MCP (Model Context Protocol) project that provides a set of tools to boost programmer productivity, particularly in the realm of AI development.

## Logo

![Project Logo](https://via.placeholder.com/150)
## Motivation

This project aims to create a centralized platform for managing and executing various tasks related to software development, with a particular focus on AI-related workflows. By leveraging the Model Context Protocol (MCP), we can create a flexible and extensible system that allows developers to easily integrate and utilize different tools and services.

## Code Structure

The project is organized as follows:

*   `mcp_server/mcp_server.py`: This is the main file that implements the MCP server. It handles loading tools, executing requests, and communicating with the MCP client.
*   `mcp_server/tools/`: This directory contains the individual tools that can be used by the MCP server. Each tool is implemented as a separate Python module.
*   `mcp_server/tools/analyze_code.py`: A tool that performs static analysis to identify potential errors and code quality issues.
*   `mcp_server/tools/debug_code.py`: A tool that allows users to simulate debugging code.
*   `mcp_server/tools/file_management.py`: A tool that allows users to create, read, write, and delete files and directories.
*   `mcp_server/tools/generate_code.py`: A tool that generates boilerplate code for common tasks in various programming languages.
*   `mcp_server/tools/memory_tool.py`: A tool that uses the memory MCP server to store and retrieve information.
*   `mcp_server/tools/sequential_thinking_tool.py`: A tool that uses the sequential thinking MCP server to help with complex tasks.
*   `mcp_server/tools/task_management.py`: A tool that allows users to create and manage tasks.
*   `mcp_server/tools/test_tools.py`: A file containing unit tests for the tools.
*   `request.json`: A sample JSON file that can be used to send requests to the MCP server.
*   `README.md`: This file, which provides an overview of the project.

## Available Tools

*   **generate_code:** A tool that generates boilerplate code for common tasks.
    *   Arguments: `code_type`, `name`, `language` (optional, defaults to "python"), `description` (optional)
    *   Output: The generated code.
*   **debug_code:** A tool that allows users to simulate debugging code.
    *   Arguments: `code`, `breakpoints` (optional, defaults to empty list)
    *   Output: `Debugging started (simulated).`
*   **analyze_code:** A tool that performs static analysis to identify potential errors and code quality issues.
    *   Arguments: `code`
    *   Output: A dictionary containing lists of errors and warnings.
*   **version_control:** A tool that interacts with Git to perform common version control operations.
    *   Arguments: `command`, `repo_path` (optional, defaults to current directory)
    *   Output: The output of the Git command.
*   **task_management:** A tool that allows users to create and manage tasks.
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
*   **memory_tool:** A tool that uses the memory MCP server to store and retrieve information.
    *   **add:** Adds a new observation to the entity.
        *   Arguments: `action`, `entity_name`, `content`, `entity_type` (optional)
        *   Output: The response from the memory MCP server.
    *   **get:** Searches for the entity and returns its observations.
         *   Arguments: `action`, `entity_name`, `entity_type` (optional), `keywords` (optional), `limit` (optional, defaults to 5)
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
    *   **file_exists:** Checks if a file exists.
        *   Arguments: `path`
        *   Output: `True` if the file exists, `False` otherwise.
    *   **directory_exists:** Checks if a directory exists.
        *   Arguments: `path`
        *   Output: `True` if the directory exists, `False` otherwise.

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
