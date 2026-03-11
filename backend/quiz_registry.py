"""Compatibility wrapper for the quiz registry module path used by tests."""

from .services.quiz_registry import QUIZ_REGISTRY, get_quiz

__all__ = ["QUIZ_REGISTRY", "get_quiz"]