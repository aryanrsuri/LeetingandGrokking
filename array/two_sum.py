def two_sum(nums, target):
    #inp arr of integers nums and target int
    #retr indecies of the n1 + n2 = target
    nmap = {}
    for i, n in enumerate(nums):
        if target - n in nmap:
            return nmap[target - n] , i
        nmap[n] = i

print(two_sum([2,7,4], 9))
print("sxcsdf")