def outer_function_string(t: str):
    var_string = t
    print("string variable id at outer function: ", id(var_string))
    def nested_function_0():
        print(id(var_string))
        var_string = "another_string"
        print(id(var_string))
    # ==> error
    def nested_function_1():
        print("string variable not re-assigned: ", id(var_string))
    def nested_function_2():
        var_string = "another string"
        print("string variable re-assigned: ", id(var_string))

    # nested_function_0()
    # --> error
    nested_function_1()
    nested_function_2()

def outer_function_list(a_list: list):
    var_list = a_list
    print("list variable id at outer function: ", id(var_list))
    def nested_function_0():
        var_list.append(4)
        print("list variable id after append: ", id(var_list))
    def nested_function_1():
        var_list[0] = 4
        print("list variable after changing one element value: ", var_list)
        print("list varialbe id after changing one element value: ", id(var_list))
    def nested_function_2():
        var_list = [1, 2, 3]
        print("list varialbe id after re-assigning: ", id(var_list))

    nested_function_0()
    nested_function_1()
    nested_function_2()

outer_function_string("hello world")
outer_function_list([1, 2, 3])

print("conclusion: list appending and changing element value does not change the id. but re-assigning the whole variable does.")