def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in dic.keys():
            return i, dic[c]
        dic[nums[i]] = i
    return None

if __name__  == "__main__":
    import numpy as np
    for i in range(5):
        a = np.random.randint(0, 100, size= 10)
        print "origin:", a
        b = twoSum(a, 50)
        print "returns:", b

