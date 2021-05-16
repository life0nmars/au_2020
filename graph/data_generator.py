import random
import sys

headers = ['Resourse','Date','Staff','Stuff\n']
staff = ["Anya","Annushka", "Anna", "Anuta", "Anechka"]

class Randomizer:
    def __init__(self, resourse):
        self.resourse = resourse
        self.staff = staff


    def dictOfMonths(self):
        day_31 = dict.fromkeys(['01','03','05','07','08','10','12'],31)
        day_30 = dict.fromkeys(['04','06','09','11'],30)
        month = {'02':28}
        month.update(day_31)
        month.update(day_30)
        return month


    def random_date(self):
        lstmonth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        rmonth = random.choice(lstmonth)
        month = self.dictOfMonths()
        amountOfDays = month[rmonth]
        days = []
        for i in range(1, amountOfDays + 1):
            days.append(i)
            i += 1
        return '{}-{}-{}'.format(random.choice(days), rmonth, 2020)


    def random_resourse(self):
        return '{}'.format(random.choice(self.resourse))


    def random_stuff(self):
        return '{}'.format(random.randint(80, 130))


    def random_staff(self):
        return '{}'.format(random.choice(self.staff))


    def all_in(self):
        return '{}, {}, {}, {}'.format(self.random_resourse(), self.random_date(), self.random_stuff(),
                                       self.random_staff())


def main(file_name):
    resourse = sys.argv[1].split(',')
    print(sys.argv[1])
    act = Randomizer(resourse)
    i = 0
    old_data = ','.join(headers)
    while i < 100:
        new_data = old_data + act.all_in()
        old_data = new_data + '\n'
        i += 1
    f = open(file_name, "w")
    f.write(new_data)
    f.close()


if __name__ == '__main__':
    main(r"input.txt")
