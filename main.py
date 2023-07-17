def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max = 0
    
    for i in keyboards:
        for j in drives:
            if i + j > max and i + j <= b:
                max = i + j
                
            
    if max != 0:
        return max
    else:
        return -1
    
def main():
    print(getMoneySpent([60,50, 110], [70, 80, 45], 105))

if __name__ == '__main__':
    main()