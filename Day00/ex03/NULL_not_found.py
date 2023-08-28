def NULL_not_found(object: any) -> int:
    types = type(object).__name__
    if types == "NoneType":
        print(f"Nothing : {object}  <class '{types}'>")
    elif types == "float" and object != object or object == 0.0:
        print(f"Cheese : {object} <class '{types}'>")
    elif types == "int" and object == 0:
        print(f"Zero : {object}  <class '{types}'>")
    elif types == "str" and object == "":
        print(f"Empty : {object}  <class '{types}'>")
    elif types == "bool" and object is False:
        print(f"Fake : {object}  <class '{types}'>")
    else:
        print("Type not found")
        return 1
    return 0
