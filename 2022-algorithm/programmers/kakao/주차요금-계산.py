import math


def dateToMinutes(time):
    hh, mm = map(int, time.split(':'))
    return hh*60 + mm


def solution(fees, records):
    answer = []
    dic = dict()
    basic_time, basic_fee, unit_time, unit_fee = fees
    # 데이터 정제 - 딕셔너리
    for record in records:
        time, car, type = record.split()
        if car in dic:
            dic[car].append(dateToMinutes(time))
        else:
            dic[car] = [dateToMinutes(time)]

    # 마지막 출차가 없을 시 23:59
    for item in dic.values():
        if len(item) % 2 != 0:
            item.append(dateToMinutes("23:59"))

    # 차량번호가 작은 순서대로
    record_list = list(dic.items())
    record_list.sort()

    for record in record_list:
        time_calc = 0
        # 누적 주차 시간 계산
        for i, time in enumerate(record[1]):
            if i % 2 == 0:
                time_calc -= time
            else:
                time_calc += time

        # 주차 요금 계산
        amount = basic_fee + \
            math.ceil(((time_calc - basic_time) / unit_time)) * unit_fee

        # 누적 주차 시간이 기본시간 이하일 시, 기본요금 부과
        if amount <= basic_fee:
            amount = basic_fee

        answer.append(amount)
    return answer


fees = [120, 0, 60, 591]
records = ["16:00 3961 IN", "16:00 0202 IN",
           "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
answer = solution(fees, records)
print(answer)
