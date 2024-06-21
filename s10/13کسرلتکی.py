def latex(start : int, n : int):
  result = ""
  if n == 1:
    result = str(start)
  else:
    result = str(start) + '+\\frac{'+ latex(2*start, n-1) + '}{' + latex(2*start + 1, n-1) + '}'
  return result


n = int(input())
start = 1
print(latex(start, n))






def latky( n:int, a = 1):
    if n == 1:
        return f"{a}"
    else:
        return f"{a}+\\frac{{{latky(n-1,2*a)}}}{{{latky(n-1,2*a+1)}}}"
print(latky(int(input())))






from math import log2, floor
n = int(input())


def latex(x):
    base_power = floor(log2(x))
    d = x - 2**base_power
    new_x1 = 2**(base_power+1) + 2*d
    new_x2 = new_x1+1
    if base_power == n-1:
        return x
    else:
        return str(x)+"+\\frac{"+str(latex(new_x1))+"}{"+str(latex(new_x2))+"}"


print(latex(1))


