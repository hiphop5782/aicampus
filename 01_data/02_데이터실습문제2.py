"""
# 문제 2. 거스름돈 계산
빵집에서 3,500원짜리 빵 2개와 4,200원짜리 케이크 1개를 구매했습니다.
20,000원을 지불했습니다.
요구사항: 총 구매 금액과 거스름돈을 각각 계산하여 출력하세요.
"""

# 입력 (프로그램에 넣는 값)
bread_price = 3500
bread_count = 2
cake_price = 4200
cake_count = 1
pay = 20000

# 연산 (출력값을 만드는 과정)
bread_total = bread_price * bread_count
cake_total = cake_price * cake_count
total = bread_total + cake_total
change = pay - total

# 출력 (프로그램에서 나오는 값)
print("총 금액 :", total, "원")
print("거스름돈 :", change, "원")