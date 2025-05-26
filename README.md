# Integrate MCP Servers Directly: No Client Needed

This repository contains the example code for the YouTube video: [Integrate MCP Servers Directly: No Client Needed](https://youtu.be/OC_5Ra7wNGg).

## Resources and Links

Please add the resources and links from the YouTube video description here.

This is a brief description of the project.

## Code Description

The `main.py` script implements a chatbot that interacts with an Anthropic model via a Zapier MCP (Managed Component Platform) server. Here's a summary of its functionality:

- **Anthropic Client Initialization**: It starts by creating an Anthropic API client.
- **User Interaction**: It presents a welcome message and then enters a loop to continuously receive text input from the user.
- **Message Processing**: User messages are sent to an Anthropic model. The API call is configured to route requests through a specified Zapier MCP server. This allows the Anthropic model to potentially use tools or capabilities provided by Zapier.
- **Response Handling**: The script is designed to handle different types of content in the model's response:
    - **Text**: Plain text responses from the model.
    - **Tool Calls (mcp_tool_use)**: Requests from the model to use a specific tool, indicating the tool name, server, and input arguments.
    - **Tool Results (mcp_tool_result)**: The outcomes of tool executions.
- **Output Formatting**: The script formats and prints these varied content blocks, providing a clear view of the interaction, including any tool usage.
- **Exit Condition**: The chatbot session ends when the user types 'bye'.

This script serves as an example of how to integrate Anthropic models with external services or tools using their Managed Component Platform.
