from dotenv import dotenv_values

"""
    this is small script to convert words to numbers.
"""

envs = dotenv_values('.env')


def eval(num1 :int, num2 :int =0) -> int:
    """
        this function checks if the given two nums shuld be added or multplied then the result is returned.
    """
    if num2 >= 100:
        return num1 * num2
    return num1 + num2


def words2nums(line :str) -> int:
    """
        this function taks a line as argument and splits it into a list of string then checks if the strings
        in the list have equalent numbers in envs dictionary. get it from the dict to construct the number
        described by the argument.
    """
    words = line.upper().split()
    number = 0
    num1 = 0
    num2 = 0
    for _ in range(0, len(words), 2):
        try:
            if '-' in words[_]:
                num1 = int(envs[words[_][:words[_].index('-')]]) 
                num11 = int(envs[words[_][words[_].index('-')+1:]])
                num1 = num1+num11 if num11<100 else num1*num11
            else:
                num1 = int(envs[words[_]])
            if '-' in words[_+1]:
                num2 = int(envs[words[_+1][:words[_+1].index('-')]])
                num22 = int(envs[words[_+1][words[_+1].index('-'):]])
                num2 = num2+num22 if num22<100 else num2*num22

            else:
                num2 = int(envs[words[_+1]])
        except IndexError:
            num2 = 0
        except Exception as e:
            print(f"error: {e}")
        number += eval(num1, num2)
    return number


if __name__ == '__main__':
    running = True

    print("This script runs in a while loop to stop it execution type: 'exit' in the prompt '>>>';\n example: >>>six \n 6\nend of the help line.")

    while running:
        entrys = input(">>>")
        if entrys == 'exit':
            running = False
            continue
        print(words2nums(entrys))
