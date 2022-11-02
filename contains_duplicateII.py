def cdII(nums, k ):
    mp = {}
    for i,n in enumerate(nums):
        if n in mp:
            if abs(i - mp[n]) <= k:
                return True
        mp[n] = i
    return False
