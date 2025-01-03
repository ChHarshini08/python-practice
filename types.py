courses=['History', 'Math', 'Eng', 'ComSci']
num=[1,2,3,4,5,6,7,8]
print(courses[0])
print(courses[-3])
print(courses[0:4])
courses.append('Art')
courses.insert(2,'AI')
courses.reverse()
print(courses)
courses.remove('Math')
courses.pop()
sorted_course = sorted(courses)
print(sorted_course)
print(sum(num))
print(courses.index('Eng'))
print('Art' in courses)

for index,course in enumerate(courses, start=1):
    print(index,course)



