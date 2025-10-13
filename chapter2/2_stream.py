import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client("bedrock-runtime")

response = client.converse_stream(
    modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "いろは歌を詠んで"
        }]
    }]
)

# ストリーミングレスポンスを取得して逐次表示
for event in response.get('stream', []):
    if 'contentBlockDelta' in event:
        chunk = event['contentBlockDelta']['delta']['text']
        print(chunk, end='')