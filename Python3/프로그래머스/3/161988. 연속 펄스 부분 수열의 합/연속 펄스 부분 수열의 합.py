def solution(sequence):

    def max_subarray_sum(arr):
        max_sum = arr[0]
        current_sum = arr[0]
        
        for i in range(1, len(arr)):
            # arr[i] : 여기부터 다시 시작 
            # current_sum + arr[i] : 이어서 진행
            current_sum = max(arr[i], current_sum + arr[i]) 
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    # 펄스 수열을 생성하여 변형된 두 배열 만들기
    pulse1 = [sequence[i] * (1 if i % 2 == 0 else -1) for i in range(len(sequence))]
    pulse2 = [sequence[i] * (-1 if i % 2 == 0 else 1) for i in range(len(sequence))]
    
    # 두 가지 펄스 배열의 최대 부분 합 중 최댓값 반환
    return max(max_subarray_sum(pulse1), max_subarray_sum(pulse2))
