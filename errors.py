def myfunction(y):
    # creates an error
    x = "string"
    try:
        z = x + y
        return z
    except TypeError:
        print("variables are not same type so operation can not be completed")


def main():
    print(myfunction(5))


if __name__ == "__main__":
    main()