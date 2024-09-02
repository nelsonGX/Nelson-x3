from anthropic import Anthropic

from lib.load_config import claude_key

client = Anthropic(api_key=claude_key)

async def generate(history):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=history
    )
    print(message)

    return message.content[0].text