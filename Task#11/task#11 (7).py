def isupperorlower(letter):
    upper_case = 0
    lower_case = 0
    for i in letter:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
    print('No. of uppecase letter', upper_case)
    print('No. of lower case letters ', lower_case)


isupperorlower("Hello You")  # type in double_Quotation
