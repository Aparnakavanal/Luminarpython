def valphno(fun):
    def innerFun(phn):
        if len(phn)<10:
            raise Exception("invalid")
        else:
            return fun(phn)
    return innerFun

@valphno
def val(phn):
    return "valid"+phn
print(val("5846254125"))


