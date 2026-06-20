class QuantumBreachError(Exception):
    """Raised when mathematical parameters fail integrity checks."""
    pass

class TrapTriggeredException(Exception):
    """Raised to instantly interrupt the thread when a canary is touched."""
    pass
  
