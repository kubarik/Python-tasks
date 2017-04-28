#str = '[1+1]+(2*2)-{3/3}';
#str = '(3+{1-1)}';
#str = '((5+3)*2+1)'
#str = '{[(3+1)+2]+}'
#str = '(({[(((1)-2)+3)-3]/3}-3)'
def checkio(expression):
    brackets = ['(', ')', '{', '}', '[', ']']
    L = len(brackets)
    result = []
    for x in list(expression):
        #возвращаем индекс
        for i in range(L):
            #открывающая
            if (((i % 2) == 0) and brackets[i] == x):
                result.append(i)
                break
            #закрывающая
            if (((i % 2) != 0) and brackets[i] == x):
                #проверяем, что она закрывает скобку того же типа
                Lr = len(result)
                if (Lr > 0 and brackets[result[Lr-1]] != brackets[i-1]):
                    return False
                elif (Lr > 0 and brackets[result[Lr-1]] == brackets[i-1]):
                    result.pop(Lr-1)
                else:
                    result.append(i)
                break
    if (len(result) > 0):
        return False
    
    return True
