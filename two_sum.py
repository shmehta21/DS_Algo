

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    : O(n^^2) complexity
    """
    result = []
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            #print(f'{i},{j}')
            if i != j and nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
            else:
                j += 1
        if result:
            break
        i += 1
    return result

def two_sum_eff(nums, target):
   '''
   O(n) complexity 
   '''
   num_to_index={}
   for i, num in enumerate(nums):
       if target - num in num_to_index:
         return [i, num_to_index[target-num]]

       num_to_index[num] = i
   return []
           

if __name__ == '__main__':
    nums = [2,7,9,11]
    target = 9
    result = two_sum_eff(nums, target)
    print(result)
