gh=input('Message? ')
output=[]
hg=0
for e in gh:
  if hg%3==0:
    output.append(e)
  hg=hg+1
ghh=''.join(output)
print(ghh)