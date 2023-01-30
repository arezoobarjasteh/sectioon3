import random
word=["classroom","pencil","banana","home","python"]
import random
opportunity=10
RANDOM=random.choice(word)

print("play ro shoro kon :)")
select=[]
for i in range(len(RANDOM)):
    select.append(RANDOM[i])
    print(" _ ",end=' ')

a = []

for j in range(len(RANDOM)):
    a.append(" - ")

selected=[]
while True:

    guess=input("\n pealse type the guess : ")
    guess=guess.lower()

    if guess not in select :
        opportunity-=1
        selected.append(guess)
        print("\n wrong answer :",opportunity,"your selected word:")
        for n in range(len(selected)):
            print( selected[n], ",", end='')
        print("\n")


    for i in range(len(RANDOM)):

        if guess in select[i]:
            a[i]=str(guess)

    for j in range(len(a)):
        print(a[j],end='')
    if a == select:
        print("\t you win :)")
        break
    if opportunity==0:
        print("You did not win!")
        break