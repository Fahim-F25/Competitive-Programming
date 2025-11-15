def is_leap(year):
    leap = False
    isLeap = True
    
    # Write your logic here
    if(year%400==0):
        # print("leap year")
        return isLeap
    elif(year%4==0 and year%100!=0):
        # print("leap year")
        return isLeap
    # else:
    #     print("Not leap year");

    
    return leap

year = int(input())
print(is_leap(year))