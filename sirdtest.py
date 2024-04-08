data = [5,5,5,10,10]
known=[]
final=[]
num1=0
num2=0
def run_length_encode(data):
    for i in data:
        if i not in known:
            known.append(i)
            num1=i
        if i in known:
            for hg in known:
                if hg==i:
                    ghh=i
            
        final.append(f"({num1}, {num2})")
        return final
print(run_length_encode(data))