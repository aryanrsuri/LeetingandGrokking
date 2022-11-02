def contains_duplicate(nums) -> bool:
    l = []
    for i in nums:
        if i in l:
            return True
    return False
