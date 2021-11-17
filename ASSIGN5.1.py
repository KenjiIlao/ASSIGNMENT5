#steps
#1. RUN THE PYTHON FILE
#2.ENTER YOUR GRADE PERCENETAGE
#3. ENTER AND SEE THE RESULTS



def Grading():
    Grade = float(input("Enter the grade percentage:"))
    RoundedGrade = round (Grade)
    return RoundedGrade
  
Grade = Grading()

if Grade >= 97 and Grade <= 100:
    print ("Description: Excellent/SOBRANG TALINO")
    print ("Grade/Mark: 1.0")

elif Grade >= 94 and Grade <= 96:
    print ("Description: Excellent/MATALINO")
    print ("Grade/Mark: 1.25")

elif Grade >= 88 and Grade <= 90:
    print ("Description: Very Good/TALINO")
    print ("Grade/Mark: 1.75")

elif Grade >= 85 and Grade <= 87:
    print ("Description: Good/malapit na maging very good")
    print ("Grade/Mark: 2.0")

elif Grade >= 82 and Grade <= 84:
    print ("Description: Good")
    print ("Grade/Mark: 2.25")

elif Grade >= 79 and Grade <= 81:
    print ("Description: Satisfactory/tuloy-tuloy lang")
    print ("Grade/Mark: 2.25")

if Grade >= 76 and Grade <= 78:
    print ("Description: Satisfactory/Laban lang")
    print ("Grade/Mark: 2.75")

if Grade == 75:
    print ("Description: Passing/Pasang Awa")
    print ("Grade/Mark: 3.0")

else:
    Grade >= 65 and Grade <= 74
    print ("Description: Failure/Bawi Next Year")
    print ("Grade/Mark: 5.0")
    

