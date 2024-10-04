import math

def calculate_fee(time, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    # 기본 시간을 초과하지 않으면 기본 요금 반환
    if time <= base_time:
        return base_fee
    # 기본 시간을 초과하면 추가 요금 계산
    return base_fee + math.ceil((time - base_time) / unit_time) * unit_fee

def solution(fees, records):
    parking = {}  # 입차 시간을 기록하는 딕셔너리
    times = {}  # 각 차량의 총 주차 시간을 기록하는 딕셔너리

    # 각 차량의 입출차 기록 처리
    for record in records:
        time, car, status = record.split()  # 기록을 시각, 차량 번호, 상태로 분리
        h, m = map(int, time.split(':'))  # 시간을 시, 분으로 분리
        total_minutes = h * 60 + m  # 총 분으로 변환

        if status == 'IN':
            parking[car] = total_minutes  # 입차 시 입차 시간을 기록
        else:
            # 출차 시, 입차 시간과 비교해 주차 시간 계산 후 기록
            time_spent = total_minutes - parking.pop(car)
            times[car] = times.get(car, 0) + time_spent

    # 출차 기록이 없는 차량을 23:59에 출차 처리
    for car, in_time in parking.items():
        times[car] = times.get(car, 0) + (23 * 60 + 59 - in_time)

    # 차량 번호 순으로 요금 계산
    return [calculate_fee(times[car], fees) for car in sorted(times)]
