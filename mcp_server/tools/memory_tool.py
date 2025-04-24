def memory_tool(action, entity_name, content=None):
    if action == "add":
        # Add a new observation to the entity
        arguments = {
            "observations": [
                {
                    "entityName": entity_name,
                    "contents": [content]
                }
            ]
        }
        return use_mcp_tool(server_name="memory", tool_name="add_observations", arguments=arguments)
    elif action == "get":
        # Search for the entity and return its observations
        arguments = {
            "query": entity_name
        }
        return use_mcp_tool(server_name="memory", tool_name="search_nodes", arguments=arguments)
    else:
        return "Invalid action."

def use_mcp_tool(server_name, tool_name, arguments):
    # This function simulates the use_mcp_tool function
    # In a real implementation, this would call the actual use_mcp_tool
    return f"MCP Tool: {tool_name} called on server: {server_name} with arguments: {arguments}"
