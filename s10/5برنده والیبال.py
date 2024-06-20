n = int(input())

for _ in range(n):
    q=0
    c=0
    count = int(input())
    score= input()
    for s in score:
        if s=="Q":
            q+=1
        else:
            c+=1
        if q==25:
            print("Quera")
            break
        elif c==25:
            print("CodeCup")
            break