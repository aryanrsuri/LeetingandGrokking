def contains_duplicate(nums) -> bool:
    # this code is interesting because this is a binary return based on wether or noth there are duplicated
    # a set() will be == to nums if no duplicates otherwise false
    return set(nums) != nums

def cd_nset(nums):
    mp = {}
    for k in nums:
        if k in mp:
            return True
        mp[k] = 1
    return False


t1 = [1,2,3,1]
t2 = [1,2,3,4]
t3 = [1,1,1,3,3,4,3,2,4,2]
print(cd_nset(t1))
print(cd_nset(t2))
print(cd_nset(t3))