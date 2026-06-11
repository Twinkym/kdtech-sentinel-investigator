"""
Tests for Qwen service.
"""

from src.services.qwen_service import health_check


def test_qwen_connection():
    """
    Verify Qwen Cloud connectivity.
    """
    response = health_check()

    assert response is not None
    assert len(response) > 0
