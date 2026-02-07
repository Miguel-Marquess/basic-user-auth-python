def menu(info_menu):
    c = 1
    for i in info_menu:
        print(f"{c} - {i}")
        c+=1
    return input("Digite sua opção:\n >>> ")