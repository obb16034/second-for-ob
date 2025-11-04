weather = input("오늘 날씨는? (비/맑음): ")

if weather == "비":
    print("🌂 우산을 챙기세요!")
else:
    print("😎 신나는 하루 되세요!")






print("=== 🌅 아침형 인간 테스트 ===\n")

q1 = input("Q1. 아침 일찍 일어나는 게 힘들지 않다? (예/아니오): ")

if q1 == "예":
    print("✨ 당신은 아침형 인간!")
    print("아침 햇살과 함께 시작하는 하루를 좋아하시는군요!")
else:
    print("🌙 당신은 저녁형 인간!")
    print("밤에 더 집중이 잘되는 타입이네요!")







print("=== ✈️ 여행 스타일 테스트 ===\n")

answer = input("여행지에서 당신의 선택은? (계획/자유/휴식): ")

if answer == "계획":
    print("📋 계획형 여행자!")
    print("일정표를 짜는 재미로 여행을 준비하시는군요!")
elif answer == "자유":
    print("🎒 자유형 여행자!")
    print("발길 닿는 대로 떠나는 여행을 즐기시네요!")
else:
    print("🏖️ 휴식형 여행자!")
    print("호텔에서 쉬면서 재충전하는 걸 좋아하시는군요!")






print("=== 👑 리더십 테스트 ===\n")

score = 0

# 질문 1
q1 = input("Q1. 팀 프로젝트에서 리더를 맡은 적이 있나요? (예/아니오): ")
if q1 == "예":
    score = score + 10
    
# 질문 2
q2 = input("Q2. 친구들이 의견을 물어볼 때가 많나요? (예/아니오): ")
if q2 == "예":
    score = score + 10
    
# 질문 3
q3 = input("Q3. 결정을 빠르게 내리는 편인가요? (예/아니오): ")
if q3 == "예":
    score = score + 10

print(f"\n당신의 점수는 {score}점!")

if score >= 25:
    print("🌟 타고난 리더!")
elif score >= 15:
    print("💫 잠재적 리더!")
else:
    print("🌱 참모형 인재!")






print("=" * 40)
print("🐾  당신의 동물상은? 테스트  🐾")
print("=" * 40)
print()

score = 0

# 질문 1
print("Q1. 친구들과 있을 때 나는?")
print("1) 분위기를 주도한다")
print("2) 조용히 듣는다")
answer1 = input("선택 (1/2): ")

if answer1 == "1":
    score += 10
    
# 질문 2
print("\nQ2. 새로운 사람을 만날 때 나는?")
print("1) 먼저 말을 건다")
print("2) 상대방이 말을 걸어주길 기다린다")
answer2 = input("선택 (1/2): ")

if answer2 == "1":
    score += 10
    
# 질문 3
print("\nQ3. 주말에 하고 싶은 것은?")
print("1) 친구들과 신나게 놀기")
print("2) 집에서 편하게 쉬기")
answer3 = input("선택 (1/2): ")

if answer3 == "1":
    score += 10

# 결과 발표
print("\n" + "=" * 40)
print("📊 결과 발표!")
print("=" * 40)

if score >= 25:
    print("\n🦁 당신은 사자상!")
    print("당당하고 리더십이 있는 당신!")
    print("친구들 사이에서 중심이 되는 스타일이에요.")
elif score >= 15:
    print("\n🐶 당신은 강아지상!")
    print("활발하고 친근한 당신!")
    print("누구와도 금방 친해지는 매력이 있어요.")
else:
    print("\n🐱 당신은 고양이상!")
    print("차분하고 신중한 당신!")
    print("조용하지만 깊은 매력이 있어요.")

print("\n" + "=" * 40)


#보너스

# 마지막에 추가해보기
# name = input("이름을 입력하세요: ")
# print(f"\n{name}님은 {동물상}입니다!")