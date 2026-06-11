"""
Qwen Cloud integration service.

Provides connectivity and health checks against
the configured Qwen model.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


api_key = os.getenv("QWEN_API_KEY")

if api_key is None:
    raise ValueError("QWEN_API_KEY environment variable not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)


def health_check() -> str:
    """
    Verify connectivity with Qwen Cloud.

    Returns:
        Model response string.
    """
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                "role": "user",
                "content": "Respond with only: KDTech Sentinel Onliine",
            }
        ],
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError("Qwen returned an empty response")
    return content
