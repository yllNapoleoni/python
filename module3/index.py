# # set methods
#
#
# my_set={1,2,3}
#
# my_set.add(4)
# my_set.remove(3)
# my_set.discard(1)
# my_set.clear()
#
# print (my_set)
#
# set_length=len(my_set)
# print("the length of the set:", set_length)
from numpy.ma.extras import unique

# using sets - removing duplicates
#
# my_list=[1,2,2,2,3,3,4,5]
#
# unique_set=set(my_list)
#
# unique_list=list(unique_set)
#
# print(unique_list)

# in and not in
#
# loyalty_members={"alice","ferals","charlie"}
#
# customer="alcie"
#
# is_member=customer not in loyalty_members
#
# print(is_member)
#
# age=18
#
# if age>=19
#     print("you can vote")
# else:
#     print("you cant vote")

# temp=28
#
# if temp>30
#     print("its a hot day")
# elif 20<=temp<=30:
#     print("its a good day")
# else:
#     print("its a cold day")

student_gpa=4.5
student_score=75

if student_gpa>=3.5:
    if 50<=student_score<=65:
        print(f"student with gpa {student_gpa} and test score {student_score} may be eligible for a partial scholarship")
    elif student_score>65:
        print(f"student with gpa {student_gpa} and test score {student_score} may be eligible for a full scholarship")
    else:
        print(f"student with gpa {student_gpa} and test score {student_score} is not eligible for a  scholarship")
else:
    print(f"students with gpa {student_gpa} and test score of{student_score} is not eligible for scholarship")

