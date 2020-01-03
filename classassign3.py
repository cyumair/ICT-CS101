course = {} # creating a empty dictionary
##print('Press 1 to add record\n2 to view records\n3 to search records \n4 to delete records')
##user = int(input('Enter corresponding number to perform desired task'))
while True:
    code = eval(input('Enter the course code '))
    name = input('Enter the course name ')
    c_hours = eval(input('Enter the course credit hours '))
    c_book = input('enter the course book name')
    course[code] = [name, c_hours, c_book]
    check = input('Press 1 to add more records ')
    if check != '1':
        break

print('Code\t\tName\t\tCreditHours\t\tCourseBook')
for i in course.keys():
    lst = course[i]
    print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2])


#search
ask = eval(input('Enter the course code you want to search for '))
found = False
lst = []
for i in course.keys():
    if i == ask:
        lst = course[i]
        found = True
        break
if found:
    print('your searched code found')
    print('Code\t\tName\t\tCreditHours\t\tCourseBook')
    print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2])
else:
    print('Your searched code not found')


#delete
ask = eval(input('Enter the course code you want to delete '))
deleted = False
for i in course.keys():
    if i == ask:
        deleted = True
        course.pop(i)
        print('Course that has key ', i, ' has been deleted')
        break

if deleted:
    print('Code\t\tName\t\tCreditHours\t\tCourseBook')
    for i in course.keys():
        lst = course[i]
        print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2])
else:
    print('The Code you entered doesnt match any course')