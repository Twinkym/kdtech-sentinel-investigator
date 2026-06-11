"""
Qwen Cloud integration service.

Provides connectivity and health checks against
the configured Qwen model.
"""

from openai import OpenAI
from src.core.config import QWEN_API_KEY, QWEN_MODEL


client = OpenAI(
    api_key=QWEN_API_KEY,
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)


def health_check() -> str:
    """
    Verify connectivity with Qwen Cloud.

    Returns:
        Model response string.
    """
    response = client.chat.completions.create(
        model=QWEN_MODEL,
        messages=[
            {
                "role": "user",
                "content": "Respond with only: KDTech Sentinel Online",
            }
        ],
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError("Qwen returned an empty response")
    return content


def ask_qwen(prompt: str) -> str:
    """
    Send a prompt to Qwen Cloud.

    Args:
        prompt: User prompt.

    Returns:
        Generated response.
    """
    response = client.chat.completions.create(
        model=QWEN_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError("Qwen returned an empty response")
    return content
