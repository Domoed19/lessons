"""Используя условие первой задачи из урока, проверить то же самое только для коней.
"""
def is_f_b_e_o(x1, y1, x2, y2):
    if abs(x1 - x2) + abs(y1 - y2) == 3 and x1 != x2 and y1 != y2:
        return True
    return False

def main():
    x1 = int(input("enter x1"))
    y1 = int(input("enter y1"))
    x2 = int(input("enter x2"))
    y2 = int(input("enter y2"))

    if is_f_b_e_o (x1, y1, x2, y2):
        print ("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
