test_num = "6076470818000080"


def reverse_it(list):
    return list[::-1]


def validate(num: str):
    num_list = list(test_num)
    last_num = num_list[len(num_list) - 1]
    new_list = reverse_it(num_list)
    new_list.remove(last_num)
    for index in range(len(num)):
        int_version = int(num[index])

    print(new_list)


print(validate(test_num))
