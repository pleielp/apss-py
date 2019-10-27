

def solution(foods, friends):
    M = len(foods)

    def can_everybody_eat(menu):
        for friend in friends:
            is_eat = False
            for f in menu:
                if friend[f]:
                    is_eat = True
                    break
            if not is_eat:
                return False
        return True

    def selectMenu(menu, food):
        if food == M:
            if can_everybody_eat(menu):
                return len(menu)
            return M+1
        ret = selectMenu(menu, food+1)
        menu.append(food)
        ret = min(ret, selectMenu(menu, food+1))
        menu.pop()
        return ret

    return selectMenu([], 0)


if __name__ == "__main__":
    foods = ["noddle", "pizza", "rice", "chicken", "spaghetti", "cola"]
    friends = [[False, True, True, True, False, False],
               [False, False, False, False, True, True],
               [True, False, True, False, True, False],
               [True, True, False, False, False, True]]
    print(solution(foods, friends))
