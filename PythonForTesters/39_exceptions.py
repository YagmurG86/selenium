# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except Exception as e:
#     print(e)
#     print("Exception: Only if Exception occured")
# else:
#     print("Else: Only if no Exceptaion was occured")
# finally:
#     print("Finally: Always, doesnt matter if Exception occured or not")


# ==================================================================

# Raise Excpetion

try:
    x = int(input())
    y = int(input())
    if y == 0:
        raise Exception("Nenner ist 0")
    print(x/y)
except Exception as e:
    print(e)
    print("Exception: Only if Exception occured")
else:
    print("Else: Only if no Exceptaion was occured")
finally:
    print("Finally: Always, doesnt matter if Exception occured or not")
