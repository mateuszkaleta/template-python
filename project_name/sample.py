from typing import Optional


def sample_logic(x: Optional[int] = None) -> int:
    """
    Sample function, returns x if x's defined, 0 otherwise
    """
    return x or 0
