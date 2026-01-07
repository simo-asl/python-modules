def ft_recursive(day, rec):
    print("Day", rec)
    if rec == day:
        print("Harvest time!")
        return
    ft_recursive(day, rec + 1)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    ft_recursive(day, 1)
