import anthropic


def create_anthropic_client():
    """Create and return an Anthropic client."""
    return anthropic.Anthropic(
        # API key defaults to os.environ.get("ANTHROPIC_API_KEY")
    )


def print_welcome_message():
    """Print the welcome message for the chatbot."""
    print("Welcome to the Anthropic MCP Chatbot!")
    print("Type your messages and I'll respond using the Zapier MCP server.")
    print("Say 'bye' to exit.\n")


def get_user_input():
    """Get and return user input, handling exit conditions."""
    user_input = input("►►►►► You: ").strip()
    
    if user_input.lower() == "bye":
        print("Goodbye!")
        return None
    
    return user_input if user_input else ""


def create_mcp_message(client, user_input):
    """Send a message to Anthropic with MCP server configuration."""
    return client.beta.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": user_input}],
        mcp_servers=[
            {
                "type": "url",
                "url": "https://mcp.zapier.com/api/mcp/mcp",
                "name": "zapier",
                "authorization_token": "<YOUR_AUTHORIZATION_TOKEN>",
            }
        ],
        betas=["mcp-client-2025-04-04"],
    )


def print_text_response(content_block):
    """Print a text response content block."""
    print("📝 Text Response:")
    print(f"{content_block.text}\n")


def print_tool_call(content_block):
    """Print a tool call content block."""
    print("🔧 Tool Call:")
    print(f"   Tool: {content_block.name}")
    print(f"   Server: {content_block.server_name}")
    print(f"   ID: {content_block.id}")
    if hasattr(content_block, 'input') and content_block.input:
        print("   Arguments:")
        for key, value in content_block.input.items():
            print(f"     {key}: {value}")
    print()


def print_tool_result(content_block):
    """Print a tool result content block."""
    print("📋 Tool Result:")
    print(f"   Tool Use ID: {content_block.tool_use_id}")
    print(f"   Is Error: {content_block.is_error}")
    if content_block.content:
        print("   Result Content:")
        for result_item in content_block.content:
            if hasattr(result_item, 'type') and result_item.type == 'text':
                print(f"     {result_item.text}")
            else:
                print(f"     {result_item}")
    print()


def print_unknown_content_block(content_block, index):
    """Print an unknown content block."""
    if hasattr(content_block, 'type'):
        print(f"❓ Unknown Content Block (type: {content_block.type}):")
    else:
        print(f"❓ Content Block {index + 1}:")
    print(f"   {content_block}")
    print()


def format_and_print_response(response):
    """Format and print all content blocks in the response."""
    for i, content_block in enumerate(response.content):
        if hasattr(content_block, 'type'):
            if content_block.type == 'text':
                print_text_response(content_block)
            elif content_block.type == 'mcp_tool_use':
                print_tool_call(content_block)
            elif content_block.type == 'mcp_tool_result':
                print_tool_result(content_block)
            else:
                print_unknown_content_block(content_block, i)
        else:
            print_unknown_content_block(content_block, i)


def process_user_message(client, user_input):
    """Process a user message and handle the response."""
    try:
        response = create_mcp_message(client, user_input)
        format_and_print_response(response)
    except Exception as e:
        print(f"Error: {e}\n")


def main():
    """Main chatbot loop."""
    client = create_anthropic_client()
    print_welcome_message()
    
    while True:
        user_input = get_user_input()
        
        # Check if user wants to exit
        if user_input is None:
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        process_user_message(client, user_input)

if __name__ == "__main__":
    main()
