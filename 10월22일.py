#print, input 복습
print('Hey!')
name = 'Tharonne'
print(name)
ask = input('What are you????')
print('hey!')
print(ask)
print('good to see you!')

#f-string
#1
first_name = 'Walters'
last_name = 'Frockins'
print(f'Hello, son of {last_name}. your name is {first_name}?')
#2
동물 = '기니피그'
소리 = '뾰보보봅뵤뵤뵥'
print(f'짐승을 소개해보겠습니다! 우선 {동물}는 {소리} 하고 웁니다!')
#3
음식 = '떡볶이'
토핑 = '치즈짱많이'
print(f'오늘은 반드시 {음식} 먹을거야! {토핑} 올려서!!!')

#input 활용
#1
날씨 = input('날씨:')
기분 = input('기분:')
할_일 = input('할 일:')
print(f'오늘은 {날씨}. 그 결과 기분이 {기분}. 내가 할 일은 {할_일} 이다.')
#2
메뉴 = input('어서오세요: ')
추가구성 = input('추가 구성은요?: ')
print(f'{메뉴}집에 가서 {메뉴}를 주문했다.')
print(f'내가 주문한 {메뉴}에는 {추가구성}이(가) 들어갔다.')

#import random
import random
#대변수(집합)와 소변수를 만들어보자
#1
성씨 = ['김', '이', '최', '마', '박']
이름들 = ['수린', '전미', '채수', '도영', '이자', '다경']
성 = random.choice(성씨)
이름 = random.choice(이름들)
print(f'신규등록자: {성}{이름}')
#2
초밥들 = ['참치', '연어', '장어', '광어', '계란']
양념들 = ['간장', '고추장', '와사비', '레몬즙', '된장', '스리라차']
초밥 = random.choice(초밥들)
양념 = random.choice(양념들)
print(f'초밥을 조립하겠습니다. 시작! {초밥}초밥')
print(f'마무리로 양념할게요. 마무리! {양념}')
print(f'이렇게 해서 {초밥}{양념}초밥이 완성되었습니다.')

재료들 = ['양상추', '고기패티', '치즈', '토마토']
소스들 = ['케첩', '마요네즈', '머스타드', '스리라차']
재료 = random.choice(재료들)
소스 = random.choice(소스들)
print(f'햄버거 먹을래? 재료는 {재료}야!')
print(f'여기다가 {소스}소스를 부으면 완성!')
print(f'이렇게 해서 {재료}{소스}버거가 완성되었다!')

#random.randint
#1
키 = random.randint(155,190)
몸무게 = random.randint(45,100)
운동신경 = random.randint(1,10)
print(f'캐릭터 생성: 키 {키}cm 몸무게 {몸무게}kg 운동신경 {운동신경}점')
print('다시 선택하겠습니까?')
#2
체력 = random.randint(1,100)
매력 = random.randint(1,100)
마력 = random.randint(1,100)
지구력 = random.randint(1,100)
지혜 = random.randint(1,100)
print(f'당신은 이 세계의 주인공입니다. 시간이 없으니 대충 고르겠습니다. \n당신의 체력은{체력}')
print(f'매력은 {매력}정도 하고, 마력은{마력}, 지구력은{지구력}, 지혜를{지혜} 요정도로 해줄게요.')
print('맘에 안들어도 너무 원망은 마세요?')