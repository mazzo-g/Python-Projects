msg = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. "
       "You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]
memory = 0.0


def read_calc():
    global memory

    print(msg[0])
    user_input = input().split()

    op = user_input[1]

    x = user_input[0]
    if x == "M":
        x = str(memory)

    y = user_input[2]
    if y == "M":
        y = str(memory)

    calc = (op, x, y)
    return calc


def sanitize(arg):
    if arg[1].isalpha() or arg[2].isalpha():
        print(msg[1])
        return False
    if not str(arg[0]).endswith(("+", "-", "*", "/")):
        print(msg[2])
        return False
    else:
        return True


def operation(calc):
    check(calc[1], calc[2], calc[0])
    op_result = 0
    if calc[0] == "+":
        op_result = float(calc[1]) + float(calc[2])
    elif calc[0] == "-":
        op_result = float(calc[1]) - float(calc[2])
    elif calc[0] == "*":
        op_result = float(calc[1]) * float(calc[2])
    elif calc[0] == "/":
        if float(calc[2]) != 0.0:
            op_result = float(calc[1]) / float(calc[2])
        else:
            print(msg[3])
            return "notTrue"

    return op_result


def result():
    calc = read_calc()
    while not sanitize(calc):
        calc = read_calc()
    inner_result = operation(calc)
    while inner_result == "notTrue":
        calc = read_calc()
        while not sanitize(calc):
            calc = read_calc()
        inner_result = operation(calc)
    return inner_result


def save(outer_result):
    global memory
    print(msg[4])
    user_input = input()
    if user_input == "y":
        memory_is_tight(outer_result)


def memory_is_tight(v):
    global memory
    if not is_one_digit(v):
        memory = v
    else:
        index = 10
        while True:
            print(msg[index])
            user_input = input()
            if user_input != "y":
                break
            if index >= 12:
                memory = v
                break
            index = index + 1


def keepup():
    print(msg[5])
    user_input = input()
    if user_input == "y":
        main()
    else:
        quit()


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v).is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    global msg
    inner_msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        inner_msg = inner_msg + msg[6]

    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        inner_msg = inner_msg + msg[7]

    if (float(v1) == 0 or float(v2) == 0) \
            and (v3 == "*" or v3 == "+" or v3 == "-"):
        inner_msg = inner_msg + msg[8]

    if inner_msg != "":
        inner_msg = msg[9] + inner_msg

    print(inner_msg)


def main():
    global memory
    outer_result = result()
    print(outer_result)
    save(outer_result)
    keepup()


main()
