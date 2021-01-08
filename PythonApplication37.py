dictionary=dict()

dictionary["안녕"]='인사'
dictionary["밥"]='필수'

a=input("\'안녕\', \'밥\' 중 한 단어를 입력하시오. : ")

if a in dictionary:
    print(dictionary[a])