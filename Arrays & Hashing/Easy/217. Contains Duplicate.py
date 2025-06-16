from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Check if nums contains a duplicate.

    Example:
        >>> containsDuplicate([1, 2, 3, 1])
        True

        >>> containsDuplicate([1, 2, 3, 4])
        False
    """
    return len(set(nums)) != len(nums)


