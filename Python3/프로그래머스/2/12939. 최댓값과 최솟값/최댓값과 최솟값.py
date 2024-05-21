def solution(s):
    nums = [int(num) for num in s.split(' ')]
    nums.sort()
    answer = str(nums[0]) + ' ' + str(nums[-1])
    return answer