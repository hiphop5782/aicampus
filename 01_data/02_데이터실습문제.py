"""
# 문제 1. 편의점 물건 구매

편의점에서 다음 물건을 구매했습니다.
- 삼각김밥: 1,500원 × 2개
- 컵라면: 1,800원 × 1개
- 음료수: 2,000원 × 3개

요구사항: 각 상품의 가격과 수량을 변수에 저장하고, 총 결제 금액을 계산하세요.
"""

# 입력
gimbob_price = 1500
gimbob_count = 2
noodle_price = 1800
noodle_count = 1
drink_price = 2000
drink_count = 3

# 연산
gimbob_total = gimbob_price * gimbob_count
noodle_total = noodle_price * noodle_count
drink_total = drink_price * drink_count
total = gimbob_total + noodle_total + drink_total

# 출력
print(total)
