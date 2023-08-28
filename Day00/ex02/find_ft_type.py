def all_thing_is_obj(object: any) -> int:
    printable = type(object).__name__
    printable_upper = printable[0].upper() + printable[1:]
    print_class = "<class '" + printable + "'>"
    if printable == "str":
        print(f"Brian is in the kitchen : {print_class}")
    elif printable in ["list", "tuple", "set", "dict"]:
        print(f"{printable_upper} : {print_class}")
    else:
        print("Type Not Found")
    return 42
