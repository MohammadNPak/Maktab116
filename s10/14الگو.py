x = input()  #1?101?
n = x.count("?")
l = len(x)


def select(x):
    try:
        i = x.index("?")
    except:
        print(x)
        return(x)

    out1 = x[:i]+"1"+x[i+1:]
    out2 = x[:i]+"0"+x[i+1:]
    select(out1)
    select(out2)

select(x)
    
    
