'''
Created on 2023. 8. 16
@author: khchu
'''
# 리스트(배열)
a = [1,2,3]
b = [2,3,4]
c = [0, 0, 0]
c[0] = a[0] + b[0]
c[1] = a[1] + b[1]
c[2] = a[2] + b[2]
# 내장 함수(출력)
print(max(a))
print(min(a))
print(a + b)
print(c)

# 변수 선언
intType = 6
floatType = 6.5
stringType = "CKH" # 'CKH'
booleanType = False

# 데이터 타입 출력
print(type(intType))
print(type(floatType))
print(type(stringType))
print(type(booleanType))

# 강제 형변환
print(type((int)(floatType)))

# bool 체크
intType1 = 20
print((bool)(intType1))
intType2 = 0
print((bool)(intType2))
floatType1 = 1.5
print((bool)(floatType1))
floatType2 = 0.0
print((bool)(floatType2))
stringType1 = "CKH"
print((bool)(stringType1))
stringType2 = ""
print((bool)(stringType2))

