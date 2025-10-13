import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client("bedrock-runtime")

# Converse APIを実行
response = client.converse(
    modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "こんにちは"
        }]
    }]
)

print(response["output"]["message"]["content"][0]["text"])