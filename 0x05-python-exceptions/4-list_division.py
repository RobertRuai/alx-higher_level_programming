#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = [0] * list_length
    for i in range(list_length):
        try:
            res[i] = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            res[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            res[i] = 0
        except IndexError:
            print("out of range")
            res[i] = 0
        finally:
            pass
    return res
