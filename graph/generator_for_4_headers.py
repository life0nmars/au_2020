import random
headers = 'Resourse, Date, Stuff, Cool Girl\n'
month = {'01':31,'02':28,'03':31,'04':30, '05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
staff = ["Anya","Annushka", "Anna", "Anuta", "Anechka"]
class Randomizer:
    def __init__(self, resourse):
        self.resourse = resourse
        self.month = month
        self.staff = staff
    def random_date(self):
        lstmonth = ['01','02','03','04','05','06','07','08','09','10','11','12']
        rmonth = random.choice(lstmonth)
        amountOfDays = self.month[rmonth]
        days = []
        for i in range(1,amountOfDays + 1):
            days.append(i)
            i += 1
        return '{}-{}-{}'.format(random.choice(days),rmonth,2020)
    def random_resourse(self):
        return '{}'.format(random.choice(self.resourse))
    def random_stuff(self):
        return '{}'.format(random.randint(80,130))
    def random_staff(self):
        return '{}'.format(random.choice(self.staff))
    def all_in(self):
        return '{}, {}, {}, {}'.format(self.random_resourse(),self.random_date(),self.random_stuff(),self.random_staff())


def main(file_name):
    resourse = input('resourses:').split(',')
    act = Randomizer(resourse)
    i = 0
    old_data = headers
    while i < 100:
            new_data = old_data + act.all_in()
            old_data = new_data + '\n'
            i += 1
    f = open(file_name, "w")
    f.write(new_data)
    f.close()
    
if __name__ == '__main__':
    main("input.txt")
