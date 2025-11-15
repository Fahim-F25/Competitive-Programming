if __name__ == '__main__':
    n = int(input())
    stList = []
    score_list = []
    for _ in range(n):
        name = input()
        score = float(input())
        stList.append([name, score])
        score_list.append(score)

    # print(stList)
    score_set = list(set(score_list))
    score_set.sort()
    # print(score_set)



    second_lowest = score_set[1]
    # print(second_lowest)

    name_list = []
    for name,score in stList:
        if score == second_lowest:
            name_list.append(name)

    name_list.sort()
    # print(name_list)

    for i in name_list:
        print(i)



    