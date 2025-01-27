import redis
import boto3
from botocore.exceptions import ClientError
from invoke import call_model


# model = "llama-3-1-70b"
# model = "mistral-large"
model = "anthropic-haiku"

system_prompts = [
    {
        "text": """lorem ipsum"""
    }
]


tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "tool_name",
                "description": "lorem ipsum",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "tool_variable": {
                                "type": "string",
                                "description": "lorem ipsum"
                            },
                        },
                        "required": ["tool_variable"]
                    }
                }
            }
        }
    ]
}

messages = []

def generate_conversation(system_prompts, messages, tool_config, session_id):
    """Generates conversation and handles tool use requests."""
    response = call_model(model, messages, system_prompts, tool_config)

    output_message = response["output"]["message"]

    print(response)

    return output_message


def main(session_id):

    # Generate response with tool support.
    output_message = generate_conversation(
        system_prompts,
        messages,
        tool_config,
        session_id,
    )

    # Print model response.
    print("Model:", output_message["content"][0]["text"])



if __name__ == "__main__":
    main()
