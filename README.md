# beyond-mcp

**Warning: This project is currently under development and may not be stable.**

This is a test MCP (Model Context Protocol) project that provides a set of tools to boost programmer productivity, particularly in the realm of AI development.

## Logo

**Note:** I am unable to create a visual logo directly. However, I can provide a textual description of what the logo could look like.

The logo for beyond-mcp could be a stylized brain composed of interconnected dots, representing the interconnectedness of tools and the focus on AI development. The dots could be different sizes and colors to create a sense of depth and dynamism.

The color scheme could use a gradient of blues and greens to convey a sense of intelligence, growth, and innovation. Alternatively, a simpler logo could use a stylized "b" and "m" (for beyond-mcp) formed from dots. The dots could be colored in a vibrant, modern palette, such as a combination of teal, magenta, and yellow.

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
    *   Arguments: `code_type`, `name`, `language` (optional, defaults to "python")
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

To use the `generate_code` tool, send the following request:

```json
{
    "tool_name": "generate_code",
    "arguments": {
        "code_type": "class",
        "name": "MyClass",
        "language": "python"
    }
}
```

## Installation

To install the project, follow these steps:

1.  Clone the repository:
    ```bash
    git clone https://github.com/uncoder-cloud/beyond-mcp.git
    ```
2.  Change to the project directory:
    ```bash
    cd beyond-mcp
    ```
3.  Install the project and its dependencies:
    ```bash
    pip install -e .
    ```
This will install the project in editable mode, allowing you to make changes to the code and have them reflected immediately.

## Contributing

We welcome contributions to this project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with appropriate comments.
4.  Add unit tests to verify your changes.
5.  Submit a pull request with a detailed description of your changes.
