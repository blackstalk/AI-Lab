import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env automatically

message = client.messages.create(
    model="claude-haiku-4-5",  # cheapest model — keeps CI costs minimal
    max_tokens=64,
    messages=[
        {"role": "user", "content": "Say 'Hello from CI!' and nothing else."}
    ],
)

print(message.content[0].text)
