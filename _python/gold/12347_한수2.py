from bisect import bisect_right
import sys

input = sys.stdin.readline

def hansu(num) :

    hansu_cnt = 0
    if num < 100 :
        for i in range(1, num+1) :
            hansu_cnt += 1
    elif 100 <= num < 1000 :
        hansu_cnt += 99
        for i in range(111, num+1) :
            num_list = list(map(int,str(i)))
            if num_list[0]-num_list[1] == num_list[1]-num_list[2]:
                hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    elif 1e+3 <= num < 1e10:
        hansu_cnt += 144
        hansu_list = [1111, 1234, 1357, 2222, 2345, 2468, 3210, 3333, 3456, 3579, 4321, 4444, 4567, 5432, 5555, 5678, 6420, 6543, 6666, 6789, 7531, 7654, 7777, 8642, 8765, 8888, 9630, 9753, 9876, 9999, 11111, 12345, 13579, 22222, 23456, 33333, 34567, 43210, 44444, 45678, 54321, 55555, 56789, 65432, 66666, 76543, 77777, 87654, 86420, 88888, 97531, 98765, 99999, 111111, 123456, 222222, 234567, 333333, 345678, 444444, 456789, 543210, 555555, 654321, 666666, 765432, 777777, 876543, 888888, 987654, 999999, 1111111, 1234567, 2222222, 2345678, 3333333, 3456789, 4444444, 5555555, 6543210, 6666666, 7654321, 7777777, 8765432, 8888888, 9876543, 9999999, 11111111, 12345678, 22222222, 23456789, 33333333, 44444444, 55555555, 66666666, 76543210, 77777777, 87654321, 88888888, 98765432, 99999999, 111111111, 123456789, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 876543210, 888888888, 987654321, 999999999, 1111111111, 2222222222, 3333333333, 4444444444, 5555555555, 6666666666, 7777777777, 8888888888, 9876543210, 9999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e10<=num<1e11 :
        hansu_cnt += 267
        hansu_list = [11111111111, 22222222222, 33333333333, 44444444444, 55555555555, 66666666666, 77777777777, 88888888888, 99999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e11<=num<1e12 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_list = [111111111111, 222222222222, 333333333333, 444444444444, 555555555555, 666666666666, 777777777777, 888888888888, 999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e12<=num<1e13 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_list = [1111111111111, 2222222222222, 3333333333333, 4444444444444, 5555555555555, 6666666666666, 7777777777777, 8888888888888, 9999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e13<=num<1e14 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_list = [11111111111111, 22222222222222, 33333333333333, 44444444444444, 55555555555555, 66666666666666, 77777777777777, 88888888888888, 99999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e14<=num<1e15 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_list = [111111111111111, 222222222222222, 333333333333333, 444444444444444, 555555555555555, 666666666666666, 777777777777777, 888888888888888, 999999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e15<=num<1e16 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 18
        hansu_list = [1111111111111111, 2222222222222222, 3333333333333333, 4444444444444444, 5555555555555555, 6666666666666666, 7777777777777777, 8888888888888888, 9999999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    elif 1e16<=num<1e17 :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 27
        hansu_list = [11111111111111111, 22222222222222222, 33333333333333333, 44444444444444444, 55555555555555555, 66666666666666666, 77777777777777777, 88888888888888888, 99999999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    else :
        hansu_cnt += 267
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 9
        hansu_cnt += 36
        hansu_list = [111111111111111111, 222222222222222222, 333333333333333333, 444444444444444444, 555555555555555555, 666666666666666666, 777777777777777777, 888888888888888888, 999999999999999999]
        index = bisect_right(hansu_list, num)
        hansu_cnt += index
    return hansu_cnt


num = int(input())
print(hansu(num))
# 1000당 45개