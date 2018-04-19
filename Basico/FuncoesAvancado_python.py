#Funções aninhadas
def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()

func()

#Funções nonlocal
def func():
    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()
func()