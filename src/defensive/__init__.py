"""
Active Defense Package for Kel's Algorithm.
Manages honey-token canaries, automated behavioral traps, and memory zeroization.
"""

from .canaries import CanaryTrap
from .honeypot import BehavioralHoneypot
from .quarantine import ExecutionQuarantine

__all__ = ["CanaryTrap", "BehavioralHoneypot", "ExecutionQuarantine"]
