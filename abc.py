def add(a, b):
    return a*b

def sub(a, b):
    if a == b:
        return 0
    else:
        c = [a, b]
        return max(c)-min(c)

def mul(a, b):
    return a*b

def div(a, b):
    return "x" if a == 0 or b == 0 else a/b
    
def main():
  num1 = int(input("첫 번째 숫자를 입력해주세요."))
  num2 = int(input("두 번째 숫자를 입력해주세요."))
  a = input("연산 방식을 입력해주세요. (+, -, x, /")
  if a == "+":
    return add(num1, num2)
  elif a == "-":
    return sub(num1, num2)
  elif a == "x":
    return mul(num1, num2)
  elif a == "/":
    return div(num1, num2)
  else:
    return "X"

if __name__=="__main__":
  main( )
