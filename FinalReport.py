#!/usr/bin/env python
# coding: utf-8

# In[ ]:


names = ['ali', 'aysel' , 'deniz', 'efe']
surnames = ['toprak', 'cicek', 'bahar', 'gunes']

stud_name = input('Please enter your name ')
stud_surname = input('Please enter your surname ')
num_enter = 0
num_enter+=1
while num_enter<=3:
    if(num_enter>3):
        print("Please try again later")
        break
    elif(stud_name in names and stud_surname in surnames):
        print('Welcome ',stud_name + '', stud_surname)
    elif(stud_name not in names and stud_surname not in surnames):
        print('No Found this name, sorry')
        break
    

courses = []
course1= input ('Please choose a course')
course2= input ('Please choose a course')
course3= input ('Please choose a course')
course4= input ('Please choose a course')
course5= input ('Please choose a course')
courses.append(course1)
courses.append(course2)
courses.append(course3)
courses.append(course4)
courses.append(course5)
print(courses)

if (3<= len.courses<=5):
    print('Gongratulations')
else:
    print('You failed in class')
    

marks = []
chosen_course_mid = input('please enter marks of midterm chosen courses')
chosen_course_fin = input('please enter marks of final chosen courses')
chosen_course_pro = input('please enter marks of project chosen courses')

results = {"Midterm":chosen_course_mid, "Final":chosen_course_fin, "Final":chosen_course_pro}
print(results)
final_result= chosen_course_mid*0.3 + chosen_course_fin*0.5 + chosen_course_pro*0.2

if (final_result>90 ):
    print('Your Final Result: AA')
elif (70<final_result<=90 ):   
     print('Your Final Result: BB')
elif (50<final_result<=70):
     print('Your Final Result:CC')
elif (50<final_result<=70):
     print('Your Final Result: DD')
else:
    print('Your Final Result: FF, You Failed')

  


# In[ ]:





# In[ ]:




