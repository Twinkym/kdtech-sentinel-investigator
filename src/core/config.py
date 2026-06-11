"""
Application configuration
"""

import os

from dotenv import load_dotenv


load_dotenv()

QWEN_API_KEY = os.getenv("QWEN_API_KEY")

if QWEN_API_KEY is None:
    raise ValueError("QWEN_API_KEY environment variable not found")

QWEN_MODEL = "qwen-plus"
