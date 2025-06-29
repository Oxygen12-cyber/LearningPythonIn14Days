# fully functional Interactive calculator
import __main__

def main():
    var1 = int(input('your first var: '))
    var2 = int(input('your second var: '))
    operation = input('operation?: ')

    print(f'The solution is {solve(var1, var2, operation)}')

def solve(value1, value2, operator):
    if '+' in operator:
        answer = value1 + value2
        return answer
    if "-" in operator:
        answer = value1 - value2
        return answer
    if ('x' in operator) or ("*" in operator):
        answer = value1 * value2
        return answer
    if "/" in operator:
        answer = value1 // value2
        return answer
    if "sqr" in operator:
        answer = value1 ** value2
        return answer
    
if __name__ == __main__:        
    main()