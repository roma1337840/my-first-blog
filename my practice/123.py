def func(a,b):
    return a*b

print(func(144,12))

def say_halo():
    print("halo")

say_halo()
say_halo()


def say_hello():
    print("pudge")


def say_goodbye():
    print("rudge")

say_hello()
say_goodbye()


def main():
    say_hello()
    say_goodbye()

def say_hello():
    print("1213")

def say_goodbye():
    print("324")
main()
def say_wazzup(name):
    print(f"wazzup, {name}")

say_wazzup("Yatoro")
say_wazzup("Satanic")
say_wazzup("Nightfall")

def say_hello(): print("Hello")

def say_goodbye(): print("Good Bye")

message = say_hello
message()
message = say_goodbye
message()

message = lambda: print("323")
message()  # hello

sum = lambda a,b: a+b
print(sum(343,767))
print(sum(21,7))

def do_operation(a,b, operation):
    result = operation(a,b)
    print(f"result = {result}")

do_operation(5,4, lambda a,b: a + b)
do_operation(5,4, lambda a,b: a * b)

def select_operation(choice):
    if choice ==1:
        return lambda a, b: a+b
    elif choice ==2:
        return lambda a, b: a-b
    else:
        return lambda a, b: a * b
