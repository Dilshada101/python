# KBC Exercise
questions=[
    ["which language was used to create fb?","Python","french","PhP","none",3],
    ["what is the capital of India?","kabul","Sringar","Shimla","Delhi",4],
    ["who built Taj Mahal?","Mumtaz","Shah Jahan","Akbar","Altamash",2],
    ["what is the capital of Afghanistan?","Kabul","delhi","new York","Dhaka",1],
    ["who is the CEO of google?","Amarah","Muskan","Zuha","me",4 ],
    ["what is the full form of ATP?","Adinose Tri PHosphate","Adinose triple Phosphate","aditriphosphate","none",1],
    ["who is the father of Politics?","einstein","aryabhatta","Aristotle","shreyas Iyer",3],
    ["who is the best cricter in the world?","Babar Azam","Glen Maxewell","PHILLIPS","Virat Kohli",4],
    ["which is the best car in the world?","toyota","BMW","ignis","Dodge",2],
    ["which is my favorite car?","Thar","BMW M4","Porche","all",4]
]
levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\n Question for Rs.{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    reply=int(input("Enter your answer(1-4) or 0 to quit:"))
    if (reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, you have won RS.{levels[i]}")
        if(i==4):
            money=5000
        elif(i==9):
            money=10000
    else:
        print("wrong answer")
        break
print(f"Your take home money is{money}")