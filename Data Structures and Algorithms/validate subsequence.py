#The question is to validate whether one array is a subsequence of the other array

#With this approach 1 the time is O(N) and the space is O(1)
#this first approach uses a while loop
def validateSequence(array,sequence):
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(array) and pointer2 < len(sequence):
        if array[pointer1] == sequence[pointer2]:
            pointer2 +=1
        pointer1 +=1
    return print("Valid subsequence")
validateSequence([5,1,22,25,6,-1,8,10,11,7],[1,6,-1,10])

#Approach 2
def validate_Sequence(array1,array2):
    pointer_2 = 0
    for value in array1:
        if pointer_2 == len(array2):
            break
        if array2[pointer_2] == value:
            pointer_2 +=1
    return print("array2 is a valid subsequence of array1")
validate_Sequence([5,1,22,25,6,-1,8,10,11,7],[1,6,-1,10])

