print("selamat Datang di GPA kalkolator") 
point= {"A+":4.0, "A":4.0,"A-":3.67,"B+":3.33,"B":3.0,
        "B-":2.67,"C+":2.33,"C":2.0,"D+":1.33,"D":1.0,}
num_courses = 0
total_point=0
done= False
while not done:
    grade=(input("masukkan grade:"))
    if grade == "":
        done= True
    elif grade not in point:
        print("unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses +=1
        total_point+= point[grade]
    if num_courses > 0:
        print(" your GPA is {0: 3}".format(total_point/num_courses)) 
            