
#파트1
# 안녕하세요 10번 출력! 이렇게 하면... 너무 길어요! 😱
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
# ... (10번 반복)

#for반복문으로 간략하게
for i in range(10):
    print("안녕하세요")


#range 이해하기
# 기본: 0부터 4까지 (5개)
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4

# 시작과 끝: 1부터 5까지
for i in range(1, 6):
    print(i)
# 출력: 1, 2, 3, 4, 5

# 건너뛰기: 2씩 건너뛰기
for i in range(0, 10, 2):
    print(i)
# 출력: 0, 2, 4, 6, 8

#함께해보기
# 카운트다운!
print("🚀 발사 카운트다운!")
for i in range(5, 0, -1):
    print(i)
print("발사! 🚀")


#파트2
print("=== 1부터 10까지 ===")
for i in range(1, 11):
    print(i)

print("=== 한 줄로 출력 ===")
for i in range(1, 11):
    print(i, end=" ")
print()  # 줄바꿈
# 출력: 1 2 3 4 5 6 7 8 9 10

print("=== 1부터 10까지 홀수만 ===")
for i in range(1, 11, 2):
    print(i, end=" ")
print()
# 출력: 1 3 5 7 9

# 숫자와 함께 이모지 출력
for i in range(1, 6):
    print(f"{i}번째 ⭐")

# 출력:
# 1번째 ⭐
# 2번째 ⭐
# 3번째 ⭐
# 4번째 ⭐
# 5번째 ⭐


#파트3: 구구단
print("=== 2단 구구단 ===")
for i in range(1, 10):
    print(f"2 × {i} = {2 * i}")

#예쁘게
print("=" * 20)
print("    🧮 2단 구구단 🧮")
print("=" * 20)

for i in range(1, 10):
    result = 2 * i
    print(f"  2 × {i} = {result}")
    
print("=" * 20)

#원하는 단 선택하기
dan = int(input("몇 단을 출력할까요? "))

print("=" * 25)
print(f"    🧮 {dan}단 구구단 🧮")
print("=" * 25)

for i in range(1, 10):
    result = dan * i
    print(f"  {dan} × {i} = {result}")
    
print("=" * 25)


# 랜덤 구구단 퀴즈
import random

dan = random.randint(2, 9)
num = random.randint(1, 9)

print(f"🎯 문제: {dan} × {num} = ?")
answer = int(input("정답을 입력하세요: "))

if answer == dan * num:
    print("🎉 정답입니다!")
else:
    print(f"❌ 아쉽네요. 정답은 {dan * num}입니다.")


#파트4: 별표 일직선
# 별 5개
for i in range(5):
    print("★", end="")
print()
# 출력: ★★★★★

#개수 선택하기
num = int(input("별을 몇 개 출력할까요? "))

for i in range(num):
    print("★", end="")
print()

# 패턴 1: 별과 하트
for i in range(5):
    print("★♥", end="")
print()
# 출력: ★♥★♥★♥★♥★♥

# 패턴 2: 숫자와 별
for i in range(1, 6):
    print(f"{i}★", end="")
print()
# 출력: 1★2★3★4★5★

# 패턴 3: 번갈아 나타나기
for i in range(10):
    if i % 2 == 0:
        print("★", end="")
    else:
        print("♥", end="")
print()
# 출력: ★♥★♥★♥★♥★♥

# 학생 이름으로 장식하기
name = input("이름을 입력하세요: ")
stars = int(input("별 개수: "))

for i in range(stars):
    print("★", end="")
print()

print(f"  {name}님 환영합니다!")

for i in range(stars):
    print("★", end="")
print()


#파트5: 별표 삼각형 만들기
print("=== 별 삼각형 ===")

for i in range(1, 6):
    for j in range(i):
        print("★", end="")
    print()  # 줄바꿈

#크기조절
height = int(input("삼각형 높이: "))

print("\n=== 별 삼각형 ===")
for i in range(1, height + 1):
    for j in range(i):
        print("★", end="")
    print()

#다양한 삼각형
print("=== 거꾸로 삼각형 ===")
for i in range(5, 0, -1):
    for j in range(i):
        print("★", end="")
    print()

# 출력:
# ★★★★★
# ★★★★
# ★★★
# ★★
# ★

print("=== 오른쪽 정렬 ===")
for i in range(1, 6):
    # 공백 출력
    for j in range(5 - i):
        print(" ", end="")
    # 별 출력
    for j in range(i):
        print("★", end="")
    print()

# 출력:
#     ★
#    ★★
#   ★★★
#  ★★★★
# ★★★★★

print("=== 속이 빈 삼각형 ===")
for i in range(1, 6):
    for j in range(i):
        if j == 0 or j == i - 1 or i == 5:
            print("★", end="")
        else:
            print(" ", end="")
    print()

# 출력:
# ★
# ★★
# ★ ★
# ★  ★
# ★★★★★

#파트6: 숫자피라미드 만들기
print("=== 숫자 피라미드 ===")

for i in range(1, 6):
    # 공백
    for j in range(5 - i):
        print(" ", end="")
    # 숫자
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 출력:
#     1
#    12
#   123
#  1234
# 12345


print("=== 같은 숫자 피라미드 ===")

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i):
        print(i, end="")
    print()

# 출력:
#     1
#    22
#   333
#  4444
# 55555


print("=== 대칭 숫자 피라미드 ===")

for i in range(1, 6):
    # 공백
    for j in range(5 - i):
        print(" ", end="")
    # 증가하는 숫자
    for j in range(1, i + 1):
        print(j, end="")
    # 감소하는 숫자
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# 출력:
#     1
#    121
#   12321
#  1234321
# 123454321


print("=== 다이아몬드 ===")

# 위쪽 절반
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# 아래쪽 절반
for i in range(4, 0, -1):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


#파트7: 크리스마스트리 패턴 만들기
print("🎄" * 10)
print()

# 별 (꼭대기)
print("      ⭐")
print()

# 트리 몸통 (3단계)
# 1단계
for i in range(1, 4):
    for j in range(6 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("🌲", end="")
    print()

print()

# 2단계
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("🌲", end="")
    print()

print()

# 3단계
for i in range(1, 6):
    for j in range(6 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("🌲", end="")
    print()

# 나무 기둥
for i in range(2):
    print("     |||")

print()
print("🎄" * 10)

#간단한 버전(초보자용)
print("=== 크리스마스 트리 ===\n")

# 별
print("    ⭐")

# 트리
for i in range(1, 6):
    # 공백
    for j in range(5 - i):
        print(" ", end="")
    # 나뭇잎
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 기둥
print("    |||")
print("    |||")

print("\n🎅 Merry Christmas! 🎅")


#화려한 버전(심화)
print("=" * 30)
print("   🎄 CHRISTMAS TREE 🎄")
print("=" * 30)
print()

# 별
print("         ⭐")

# 트리 (장식 추가)
decorations = ["🔴", "🔵", "⚪", "🟡"]
dec_index = 0

for i in range(1, 8):
    # 공백
    for j in range(8 - i):
        print(" ", end="")
    
    # 나뭇잎과 장식
    for j in range(2 * i - 1):
        if j % 3 == 0:  # 3칸마다 장식
            print(decorations[dec_index % 4], end="")
            dec_index += 1
        else:
            print("🌲", end="")
    print()

# 기둥
for i in range(3):
    print("       🟫🟫🟫")

# 선물
print()
print("    🎁  🎁  🎁  🎁")

print()
print("=" * 30)
print("   ❄️ HAPPY HOLIDAYS! ❄️")
print("=" * 30)


#최종 프로젝트
name = input("누구에게 선물할 트리인가요? ")
height = int(input("트리 높이 (3-10): "))

print(f"\n🎄 {name}님께 드리는 크리스마스 트리 🎄\n")

# 별
spaces = height - 1
for i in range(spaces):
    print(" ", end="")
print("⭐\n")

# 트리
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("🌲", end="")
    print()

# 기둥
for i in range(2):
    for j in range(height - 2):
        print(" ", end="")
    print("|||")

print(f"\n🎅 {name}님, 메리 크리스마스! 🎁")



# 1. 무지개 계단
colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
for i in range(6):
    print(colors[i] * (i + 1))

# 2. 체스판 패턴
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()

# 3. 파도 패턴
for i in range(5):
    print("~" * i + "🌊" + "~" * (5 - i))