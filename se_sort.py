def s_sort(nums):
    for i in range(5):      #value less than 1....and 1 less b'caz after iteration we get one unsorted..
        min_pos = i
        for j in range(i,6):
            if nums[j] < nums[min_pos]:
                min_pos = j
        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp
nums = [2,3,1,5,9,11]
s_sort(nums)
print(nums)
