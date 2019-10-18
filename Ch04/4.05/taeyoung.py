from functools import reduce


def can_every_body_eat(menu):
    possible_menu_table = [menu_table[menu_idx] for menu_idx in menu]
    possible_menus = reduce(lambda a, b: a | b, possible_menu_table, 0)

    return True if possible_menus == int('1111', 2) else False

def select_menu(menu, food):
    if food == M:
        if can_every_body_eat(menu):
            return len(menu)
        return float('inf')
    ret = select_menu(menu, food + 1)
    menu.append(food)
    ret = min(ret, select_menu(menu, food + 1))
    menu.pop()
    return ret


menu_table = ['0011','1001','1010','1000','0110','0101']
menu_table = list(map(lambda m: int(m, 2), menu_table))
M = len(menu_table)

print(select_menu([], 0))