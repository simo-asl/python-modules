def ft_recursive(day, rec):
    if day == rec:
        print("Day", rec)
        return
    print("Day", rec)
    ft_recursive(day, rec + 1)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    rec = 1
    ft_recursive(day, rec)


ft_count_harvest_recursive()