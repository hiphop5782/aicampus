"""
# 리스트 실습

파일명 : `04_성적분석.py`

5명의 시험성적을 입력받은 뒤 반복문과 조건문을 사용하여 다음을 구현하세요.

1. 합격(60점 이상) 학생의 점수만 출력하세요
2. 성적 우수자(90점 이상) 학생의 점수만 출력하세요
3. 합격 인원수와 성적 우수자의 인원수를 각각 구하여 출력하세요
4. 처음 입력한 학생의 등수를 구하여 출력하세요
"""

# 입력 받자!
scores = []

for i in range(5): #5번
    number = int(input("점수 입력 : "))
    scores.append(number)

# 1
print("<60점 이상 합격자의 점수>")
for score in scores:
    if score >= 60:
        print("점수", score)

# 2
print("<90점 이상 우수자의 점수>")
for score in scores:
    if score >= 90:
        print("점수", score)

# 3
print("<60점 이상 합격자의 인원수>")
count60 = 0
for score in scores:
    if score >= 60:
        count60 += 1

print(f"{count60}명")

# 4
print("<90점 이상 우수자의 인원수")
count90 = 0
for score in scores:
    if score >= 90:
        count90 += 1
print(f"{count90}명")



