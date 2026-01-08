def ft_recursive(day, rec):
    print("Day", rec)
    if rec == day:
        print("Harvest time!")
        return
    ft_recursive(day, rec + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if days < 1:
        return
    ft_recursive(days, 1)
