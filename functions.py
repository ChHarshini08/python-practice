def hello_func():
   print('Hello All!!')
hello_func()


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses=['Math', 'Art']
info ={'Name': 'John', 'Age': '22'}

student_info(*courses, **info)


month_days = [0,31,30,31,28,30,31,30,30,31,31,30,30]
def is_leap(year):
     return year%4==0 and (year%100!=0 or year%400==0)
def days_in_month(year, month):
     if not 1<= month <=12:
         return 'Invalid'
     if month == 2 and is_leap(year):
         return 29
     return month_days[month]
print(is_leap(2017))

 

















