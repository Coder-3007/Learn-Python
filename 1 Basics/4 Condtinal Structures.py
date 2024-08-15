# We learn about conditional logic in Python


def main():
    x, y = 10, 100
    # x, y = 1000, 100
    # x, y = 10, 10

    # conditional flow uses if, elif, else

    # if x < y:
    #     result = "x is less than y"
    # print(result)
        
    
     # if x is greater than y then

    # if x < y:
    #     result = "x is less than y"
    # else:
    #     result = "x is greater than y"
    # print(result)


    # # for elif

    # if x < y:
    #     result = "x is less than y"
    # elif x == y:
    #     result = "x is the same as y"
    # else:
    #     result = "x is greater than y"
    # print(result)

    # conditional statements let you use "a if C else b"


    # result = "x is less then y" if x < y else "x is greater or equal to y"
    # print(result)


    # match-case makes it easy to compare multiple values

    # value = "one"
    # value = "three"
    value = "42"

    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        # for more than one
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print(result)

if __name__ == "__main__":
    main(),