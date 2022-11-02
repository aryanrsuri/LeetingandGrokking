def three_sum(nums):
    # given array
    # retr [arr i , arr j, arr k] where ijk are unique and sum == 0

    d = {}
    pt1, pt2 = 0, len(nums) // 2
    
    