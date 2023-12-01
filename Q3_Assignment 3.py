def eliminate_duplicates(list1):
    list_ = list(set(list1))
    return list_


def main():
   
    numbers = input("Enter ten numbers: ")
    input_numbers = list(map(int, numbers.split()))

    distinct_numbers = eliminate_duplicates(input_numbers)


    print("The distinct numbers are:", end=" ")
    for number in distinct_numbers:
        print(number, end=" ")

main()