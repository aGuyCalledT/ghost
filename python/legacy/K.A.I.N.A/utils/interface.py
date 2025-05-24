def con_in(options="any", accept_list=False):
    is_int = True
    for x in range(0, len(options)):
        if type(options[x]) is not int:
            is_int = False
            break
    if is_int is False:
        for x in range(0, len(options)):
            options[x] = str(options[x])

    while True:
        con_input = input(">").lower()
        if con_input == "help":
            print(f"Possible replies are {options}")
            if is_int:
                print("reply must be int")
            if accept_list:
                print("You can list multiple elements using <,>")
        elif options == "any":
            return con_input
        elif is_int and accept_list is False:
            try:
                if int(con_input) in options:
                    return int(con_input)
                    break
                else:
                    print(f"reply ({con_input}) is not an option")
            except ValueError:
                print(f"reply must be int")
        elif is_int is False:
            if con_input in options:
                return con_input
            else:
                print(f"reply ({con_input}) is not an option")
        elif accept_list:
            list_string = con_input.strip("][").replace(" ", "").split(",")
            if is_int:
                for x in range(0, len(list_string)):
                    if list_string[x].isdigit():
                        list_string[x] = int(list_string[x])
                    else:
                        print(f"all elements need to be int")
                        
            correct_list_elements = 0
            for x in range(0, len(list_string)):
                if list_string[x] not in options:
                    print(f"reply contains invalid value {list_string[x]}")
                else:
                    correct_list_elements += 1
            if correct_list_elements == len(list_string):
                return list_string
        elif con_input in options:
            return con_input
            break
