

def oddnums(list):


    def odd(each_num):

        if  each_num % 2 == 0:
            return False

        else:
            return True

    new_list = []

    for each_num in list:

        if odd(each_num)== True:

            new_list.append(each_num)

    return new_list

print(oddnums([1,2,3,4,5,6]))
