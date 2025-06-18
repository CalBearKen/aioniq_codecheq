"""
CodeCheq

A library for analyzing code security using Large Language Models (LLMs).
"""

from .analyzer import CodeAnalyzer
from .models.analysis_result import AnalysisResult, Issue, Location, Severity
from .prompt import PromptTemplate, create_custom_prompt, get_default_prompt

__version__ = "0.1.0"
__all__ = [
    "CodeAnalyzer",
    "AnalysisResult",
    "Issue",
    "Location",
    "Severity",
    "PromptTemplate",
    "create_custom_prompt",
    "get_default_prompt",
] 