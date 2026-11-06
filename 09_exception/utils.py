import re

# 만나이를 계산하는 함수 (오늘날짜를 구하는 방법은 모르니까 지정)
def calculate_global_age(year, month, day):
    current_year = 2026
    current_month = 11
    current_day = 6
    # 연도를 이용해서 나이를 계산
    age = current_year - year

    # 생일이 지나지 않은 경우 1살을 뺀다
    # - 월이 이번달보다 크면 생일이 지나지 않았다고 본다
    #   (month > current_month)
    # - 월이 이번달과 같으면 일을 비교해서 생일이 지나지 않았는지 판단한다
    #   (month == current_month and day > current_day)
    # if month > current_month or (month == current_month and day > current_day):
    if (month, day) > (current_month, current_day): #튜플(리스트) 비교
        age -= 1

    # 만나이는 음수가 불가능하니까 음수가 나오면 정상반환하지말고 예외로 처리
    if age < 0:
        raise Exception("미래의 날짜는 입력하실 수 없습니다")

    # 계산된 나이 반환
    return age

# 한국나이를 계산하는 함수
def calculate_korean_age(year):
    current_year = 2026
    age = current_year - year + 1
    if age < 1: #한국나이는 최소가 1살이니까
        raise Exception("미래의 날짜는 입력할 수 없습니다")
    return age

# 날짜 검사 함수
def seperate_date(date_str):
    # 정규표현식으로 선제검사 후 예외로 이동
    regexp = r"^(19[0-9]{2}|20[0-9]{2})-((02-(0[1-9]|1[0-9]|2[0-9]))|((0[469]|11)-(0[1-9]|1[0-9]|2[0-9]|30))|((0[13578]|1[02])-(0[1-9]|1[0-9]|2[0-9]|3[01])))$"
    result = re.fullmatch(regexp, birth)
    if result is None:  # 형식 불일치
        raise Exception("올바른 날짜 형식이 아닙니다")  # 메세지 추가
    year = int(birth[:4])
    month = int(birth[5:7])
    day = int(birth[8:])
    return year, month, day
