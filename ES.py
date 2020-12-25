start=input('Are you ready to play (yes/no):')
score=0
Total_question=5
if start.upper() !='YES':
    
    print('Goodbye, Have a nice day')
else:
    First=input('1. Where is the headquarter of ISRO? ')
    if First.lower()=='bengaluru':
        score+=1
        print('correct')
    else:
        print('Incorrect')

    Second=input('2. Which is the largest coffee growing country in the world? ')
    if Second.lower()=='brazil':
        score+=1
        print('correct')
    else:
        print('Incorrect')


    Third=input('3. Which is the longest river in the world? ')
    if Third.lower()=='nile':
        score+=1
        print('correct')
    else:
        print('Incorrect')

    Fourth=input('4. Who is the CEO of Google? ')
    if Fourth.lower()=='sunder pichai':
        score+=1
        print('correct')
    else:
        print('Incorrect')

    Fifth=input('5. How many district are in India now? ')
    if int(Fifth)==718:
        score+=1
        print('correct')
    else:
        print('Incorrect')
    print('Thank you for playing, you got', score, "question correct.")
    percent=(score/Total_question)*100
    print('Percentage:', str(percent) + '%')
