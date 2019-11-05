# bubble sort algorithm implementation

def bubblesort(dataset):
    # TODO:start with the lenth of the array and decrement with one
    for i in range(len(dataset)-1,0,-1):
        # TODO: go through each elements in the list
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j],dataset[j+1] = dataset[j+1],temp
        print(dataset)          
    print("DONE!\n-----------------------------------------")

def main():
    dataset = [6,20,8,19,56,23,87,41,49,53]
    bubblesort(dataset)
    print('Result: ',dataset)
    

if  __name__ == "__main__":
    main()