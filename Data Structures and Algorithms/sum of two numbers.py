#write a code to find two numbers from an array such that the sum of those two numbers is equal to the targetSum provided
#the inputs should be (array,targetSum)

#This approach has a time complexity of O(N^2) and space complexity of O(1)..therefore not the best approach
# def sumNums(array,target_sum):
#     for i in range(len(array)-1):
#         first_num=array[i]
#         for j in range(i + 1, len(array)):
#             second_num=array[j]
#             if first_num + second_num == target_sum:
#                  return [first_num, second_num]
#
#
#     return print('not working')
# sumNums([2,3,5,7,4,1,9],8)
#end of solution 1

#approach 2,,the time compexity is O(N), the space complexity is O(N) and not O(1) and this is because we created a hash table
# def sumNums(array,targetSum):
#     nums = {}
#     for num in array:
#         if targetSum-num in nums:
#             return print([num, targetSum-num])
#
#         else: nums[num] = True
#
#
#     return []
#
#
# sumNums([-4,3,5,8,11,1,-1,6],10)#end of approach 2

#approach 3:this approach has a time complexity of O(Nlog(N)) and a space complexity of O(1)
#step one, use the sort() method to arrange array in ascending order
def sumUpNums(array,sumTwoNums):
    array.sort()
    left=0
    right=len(array)-1
    while left < right:
        currentSum=array[left] + array[right]
        if currentSum == sumTwoNums:
            return print([array[left], array[right]])
        elif currentSum < sumTwoNums:
            left = left+1
        elif currentSum > sumTwoNums:
            right= right-1
    return []


sumUpNums([-4,3,5,8,11,1,-1,6],10)




