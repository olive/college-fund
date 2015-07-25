



# 1*.1.1) Rewrite the following function so that instead of printing strings,
#         the strings are returned. Each print statement should correspond to
#         a newline character '\n' in the functiono's output.
def bar_print(a, b, c):
    if a == b:
        print("1")
    elif b == c:
        print("2")
    if a == c:
        print("3")
        return
    else:
        print("4")
    print("5")

def bar_string(a, b, c):
    return ""

# Example rewrite:

def foo_print(a, b):
    if a == b:
        print("1")
        return
    else:
        print("2")

    if a == 1:
        print("3")

    print("4")

def foo_string(a, b):
    result = ""

    if a == b:
        result += "1\n"
        return result
    else:
        result += "2\n"

    if a == 1:
        result += "3\n"
    result += "4\n"
    return result

def test_equals(s, answ):
    lines = s.split('\n')[:-1]
    if lines == answ:
        print("PASS")
    else:
        print("FAIL")

def main():
    test_equals(bar_string(1,1,2), ["1","4","5"])
    test_equals(bar_string(2,1,1), ["2","4","5"])
    test_equals(bar_string(1,2,1), ["3"])

    # 1*.1.2) Write another call to test_equals that prints PASS using func.
    # 1*.1.3) The second argument to test_equals must be distinct from the
    #         above three.


    # 1*.1.4) Write 3 distinct calls to test_equals that pass for foo_string
    #         instead of bar_string

if __name__ == '__main__':
    main()
