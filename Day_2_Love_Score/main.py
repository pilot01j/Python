# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
Love_Score=0
#Write your code below this line 👇
both_names = name1+name2
lower_case_names = both_names.lower()
T =lower_case_names.count("t")
R =lower_case_names.count("r")
U =lower_case_names.count("u")
E =lower_case_names.count("e")
num1=T+R+U+E
L =lower_case_names.count("l")
O =lower_case_names.count("o")
V =lower_case_names.count("v")
num2=L+O+V+E
Love_Score=num1*10+num2
if Love_Score<10 or Love_Score>90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score>40 and Love_Score<50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")