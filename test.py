def double_letters(string):
    lis = list(string)
    count = 0
    if string == '':
        return False
    else:
        for i in range(len(lis)):
            if lis[count] == lis[count+1]:
                return True
                break
            if count == len(lis)-2:
                return False
                break
            count += 1

