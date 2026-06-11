"""
Test for evidence Analyzer.
"""

from src.agents.evidence_analyzer import EvidenceAnalyzer

analyzer = EvidenceAnalyzer()


def test_evidence_analyzer():
    """
    Verify evidence analysis generation.
    """


result = analyzer.analyze("37 failed login attempts from 203.0.113.50")

assert len(result) > 0
