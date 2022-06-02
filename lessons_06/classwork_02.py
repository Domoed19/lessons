import csv

with open("dictionary.csv", "r") as file:
   reader = csv.reader(file)

   for row in reader:
       my_dict[row[0]] = row [1]

    #my_dict = {row[0]:row[1] for row on reader}

def pervod_s_angl_na_rus (slovo):
    return my_dict[slovo]


def pervod_s_rus_na_angl(slovo):
    for key, value in my_dict.items():
        if value == slovo:
            return key
print (pervod_s_angl_na_rus("sun"))
print (pervod_s_rus_na_angl("солнце"))
