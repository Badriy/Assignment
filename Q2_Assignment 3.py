x = input("Enter ten integers separated by a space: ").split()

def index_of_smallest_element(list):
    smallest = 0
    for i in range(1,len(List)):
        if List[i] < List[smallest]:
            smallest = i

    return smallest   

try:
    List = [int(i) for i in x]
    if len(List) == 10:
        print(index_of_smallest_element(List))
    else:
        print("Error: Length of the list is not ten")

        
except:
    print("Error: only integers are alowed")