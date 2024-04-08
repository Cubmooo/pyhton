guess=input("what is your guess: ")
password="password"
output=""
hg=0
gh=""
if guess==password:
    print("Correct")
elif 8>len(guess) or len(guess)>8:
    print("Wrong length the correct length is "+str(len(password)))
else:
    for i in guess:
        hg=hg+1
        if i == password[hg-1:hg]:
            gh=gh+i
        else:
            gh=gh+"_"
    output=output+i
print(gh)