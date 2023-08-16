'''
Created on 2023. 8. 16
@author: khchu
'''
math = 78; english = 95; chemistry = 68; science = 62
total = math + english + chemistry + science
average = total/4
print("(평균)단순값: ", average)

# 리스트(배열): 인덱스 0부터
# subjectList = [78, 95, 68, 62]
# subjectList[0] = 82
# 리스트는 값의 재정의 가능

# 튜플
subjectTuple = (78, 95, 68, 62)
totalTuple = subjectTuple[0] + subjectTuple[1] + subjectTuple[2] + subjectTuple[3]
averageTuple = totalTuple / 4
print("(평균)튜플: ", averageTuple)
# subjectTuple[0] = 82
# error 튜플은 값의 재정의 금지

# 문자열 배열
weekdays = ["Monday", " Tuesday", "Wednesday", "Thursday", "Friday"]
# , "Saturday", "Sunday"

# 삽입(insert): 특정 값을 특정 위치에 넣을 수 있음
weekdays.insert(2, "TestString")
# 추가(append): 맨 뒤에 단지 추가
weekdays.append("Saturday")
print(weekdays)

# 딕셔너리
scoreDic = {
    "math": 78,
    "english": 95,
    "chemistry": 68,
    "science": 62,
}
print(scoreDic)
scoreDic["math"] = 82
print("딕셔너리: ", scoreDic)

# 리스트와 튜플을 다루는 주요 함수: len, copy, in
print(len(weekdays))

# 리스트: 2차원(껍데기는 튜플, 요소는 리스트)
data = ([1, 2], [3, 4, 5], [6, 7, 8, 9])
print("All: ", len(data))
print("1: ", len(data[0]))
print("2: ", len(data[1]))
print("3: ", len(data[2]))
print("2차원 배열의 하나의 요소: ", data[2][3])

# in
greets = ("morning", "afternoon", "evening")
print("afternoon" in greets)
print("noon" in greets[1])