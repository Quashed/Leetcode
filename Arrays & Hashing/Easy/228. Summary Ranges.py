from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    """
    Given a unique sorted array of numbers return the smallest sorted list of ranges that covers all numbers.

    Example:
        >>> nums = [0,1,2,4,5,7]
        ["0->2","4->5","7"]

        >>> [0,2,3,4,6,8,9]
        ["0","2->4","6","8->9"]
    """

    results = []

    if not nums:
        return results

    start, end = nums[0], None

    for i in range(1, len(nums)):
        if nums[i] == start + 1:
            end = nums[i]
        elif nums[i] and nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end or end is None:
                results.append(str(start))
            else:
                results.append(f"{start}->{end}")
                start = nums[i]

    if start == nums[-1]:
        results.append(str(start))
    else:
        result.append(f"{start}->{nums[-1]}")
    
    return results

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([[0,2,3,4,6,8,9]]))