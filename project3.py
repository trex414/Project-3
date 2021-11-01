# CS 177 – project3.py
# Trey Rosenfeldt, Ian Lopez
# Write a program that will read data from files and push the data into lists.
# use matplotlib Library to plot the lists and answer the quiestions

import matplotlib.pyplot as pyplot

# task 1
def readStudentsData(filename):
# open file and read it and close it
    studentsList = []
    myFile = open(filename)
    content = myFile.readlines()
    myFile.close
# make a for loop that makes the file list into multiple lists in a list
    for i in content:
        studentsList.append(i.strip('\n').split(','))
# return the list in list
    return studentsList

def readRegistrationData(filename):
# open file and read it and close it
    registrationList = []
    outputList = []
    myFile = open(filename)
    content = myFile.readlines()
    myFile.close
# make a for loop that makes the file list into multiple lists in a list
    for i in content:
        registrationList.append(i.strip('\n').split(','))
    for index in registrationList:
        outputList.append([index[0],index[1],int(index[2])])
# return the list in list
    return outputList

def readCoursesData(filename):
# open file and read it and close it
    coursesList = []
    myFile = open(filename)
    content = myFile.readlines()
    myFile.close
# make a for loop that makes the file list into multiple lists in a list
    for i in content:
        coursesList.append(i.strip('\n').split(','))
# return the list in list
    return coursesList


# task 2
def countStudents(studentsList, gender, state):
    sum1 = 0
# make a nested loop that will look through the nested lists once for gender and state
    for index in studentsList:
        for i in range(3,len(index)):
# chaeck to see if gender and state equal the person
            if (index[2] == gender) and (index[3] == state):
# add one each time the if statment is correct
                sum1 += 1
# return the sum
    return sum1


# task 3
def studentsPassedCourse(studentsList, coursesList, registrationList, courseName):
# create two lists and a string variable
    courseName1 = ""
    studentsPassedCourseList = []
    studentsPassedCourseList1 = []
# make a for loop and a if statment that checks to see if the cours name and then assign the course number
    for index in coursesList:
        if index[1] == courseName:
            courseName1 = index[0]
# make a for loop that goes through registrationList
    for index in registrationList:
# get a if statement that checks if the people are in the class
        if index[1] == courseName1:
# if they have above or equal to a 50% then append it to a list
            if index[2] >= 50:
                studentsPassedCourseList.append(index[0])
# make a nested for loop that will go trhough studentsList and studentsPassedCourseList
    for index in studentsList:
        for i in range(len(studentsPassedCourseList)):
# find if the lists equal for the student number and then append it
            if index[0] == studentsPassedCourseList[i]:
                studentsPassedCourseList1.append(index[1])
# sort the list
    mySortedList = sorted(studentsPassedCourseList1)
# return the list
    return mySortedList

# task 4
def studentsTakingOneCourse(studentsList, registrationList, courseNum):
# create two lists and a number to itterate 
    courseList = []
    studentNameList = []
    count = 0
# make a for loop to go how many time the list is
    for index in registrationList:
# get a if statement that checks if the people are in the class
        if index[1] == courseNum:
            courseList.append(index[0])
# make a nested for loop that will go trhough studentsList and studentsPassedCourseList
    for index in studentsList:
        for i in range(len(courseList)):
# find if the lists equal for the student number and then append it
            if index[0] == courseList[i]:
                studentNameList.append(index[1])
                count += 1
# sort the list
    mySortedList = sorted(studentNameList)
# return the list
    return mySortedList, count

def studentsTakingTwoCourses(studentsList, registrationList, courseNum1, courseNum2):
# make 4 lists
    courseList1 = []
    courseList2 = []
    combinedCourseList = []
    studentNameList = []
    count = 0
# make a for loop that itterated for how long the list is
    for index in registrationList:
# get a if statement that checks if the people are in the class
        if (index[1] == courseNum1):
            courseList1.append(index[0])
# make a for loop that itterated for how long the list is
    for index in registrationList:
# get a if statement that checks if the people are in the class
        if index[1] == courseNum2:
            courseList2.append(index[0])
# make anested for loop that will go for how long both lists are
    for index in courseList1:
        for i in range(len(courseList2)):
# make a if statement that checks if they are in the same class
            if index == courseList2[i]:
                combinedCourseList.append(index)                
# make a nested for loop that will go trhough studentsList and studentsPassedCourseList
    for index in studentsList:
        for i in range(len(combinedCourseList)):
# find if the lists equal for the student number and then append it
            if index[0] == combinedCourseList[i]:
                studentNameList.append(index[1])
                count += 1             
# sort the list
    mySortedList = sorted(studentNameList)
# return the list
    return mySortedList, count

# task 5
def stateCourseStatistics(studentsList, registrationList, courseNum):
# create four lists
    list1 = []
    list2 = []
    list3 = []
    list4 = []
# create a for loop that itterates for how long the list goes for
    for index in registrationList:
        if index[1] == courseNum:
            list1.append(index[0])
# create a nested for loop that itterates for how long the lists go for
    for index in studentsList:
        for i in range(len(list1)):
# check to see if they are in the class and then append the state
            if index[0] == list1[i]:
                list2.append(index[3])
# create a for loop that itterates for how long the list goes for
    for index in list2:
# make a if statment to check if the state is in the list yet
        if index not in list3:
            list3.append(index)
# create a for loop that itterates for how long the list goes for so we can count each state
    for index in list3:
        list4.append([index, list2.count(index)])
# sort the states
    mySortedList = sorted(list4, key=lambda x:x[0])
# return the list
    return mySortedList 

#task 6
def plotPieChart(courseNum1, courseNum1Count, courseNum2, courseNum2Count, bothCoursesCount):
    cool = ("Both "+ courseNum1+ " and "+ courseNum2)
    labels = [cool, courseNum1, courseNum2]
    list1 = [bothCoursesCount, courseNum1Count, courseNum2Count]
    colors = ['tomato', 'lightgreen', 'gold']
    pyplot.pie(list1 , autopct="%1.1f%%", colors = colors, startangle = 90)
    pyplot.legend(labels = labels, loc = 'lower left')
    pyplot.savefig('plotPieChart.pdf')

def plotBarChart(statesCountList):
    list1 = []
    list2 = []
    for index in statesCountList:
        list1.append(index[0])
        list2.append(index[1])
    pyplot.bar(list1, list2, color = 'red')
    pyplot.title("State Statistics")
    pyplot.ylabel("# of students")
    pyplot.xticks(rotation=45)
    pyplot.savefig('plotBarChart.pdf')
    
def main():
# task 1
    studentsList = readStudentsData('studentsdata.txt')
    registrationList = readRegistrationData('registrationdata.txt')
    coursesList = readCoursesData('coursesdata.txt')
    print(studentsList)
    print(registrationList)
    print(coursesList)
# task 2
    print (countStudents(studentsList, 'Female', 'Indiana'))
    print (countStudents(studentsList, 'Male', 'Minnesota'))
# task 3
    passedList = studentsPassedCourse(studentsList, coursesList, registrationList, 'Python Programming Language')
    print(passedList)
# task 4
    oneList, oneCount = studentsTakingOneCourse(studentsList, registrationList, 'CS177')
    print(oneList)
    print(oneCount)
    twoList, twoCount = studentsTakingTwoCourses(studentsList, registrationList, 'CS177', 'CS180')
    print(twoList)
    print(twoCount)
# task 5
    statesCount = stateCourseStatistics(studentsList, registrationList, 'CS177')
    print(statesCount)
# task 6
    course1Count = studentsTakingOneCourse(studentsList, registrationList, 'CS177')[1]
    course2Count = studentsTakingOneCourse(studentsList, registrationList, 'CS180')[1]
    bothCoursesCount = studentsTakingTwoCourses(studentsList, registrationList, 'CS177', 'CS180')[1]
    plotPieChart('CS177', course1Count, 'CS180', course2Count, bothCoursesCount)
    statesCountList = stateCourseStatistics(studentsList, registrationList, 'CS177')
    plotBarChart(statesCountList)
if __name__ == "__main__":
    main()
