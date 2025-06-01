print("hello, please fill in the survey ! ") 
name = input('please enter your fulll name')
print("hi", name , "!") 
age = int(input("what is your age?"))
GPA = float(input("how much is your gpa??"))
FieldOfInterest = (input("in what field you are interested?"))
Graduated = (input("are you graduated? y\n"))

EligibleScolar = Graduated == "yes" and age < 25 and  GPA >=  3.5
EligibleIntership = Graduated =="yes" and age < 30 and GPA >= 2.5

if EligibleScolar :
    print("good luck" , name , "you are eligal to have a scolar ship !!!")

elif EligibleIntership :
    print("good luck" , name , "you are eligal to have an inter ship !!!")

else :
    print("sorry" , name , "you are not aloowed for any thing")