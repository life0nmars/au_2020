from datetime import datetime
import matplotlib as plt
import matplotlib.pyplot as plt
def open_file(file_name):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return data

def prepearing_of_data(data):
    keys = data.pop(0).strip("\n").split(", ")
    sorted_data = []
    for elem in data:
       sorted_data.append(elem.rstrip("\n").split(", "))
    return sorted_data, keys

def make_the_dict(keys, sorted_data):
    lordOfDicts = []
    for lst in sorted_data:
      lordOfDicts.append(dict(zip(keys, lst)))
    return lordOfDicts

def filter_dicts(lordOfDicts, key, value):
    return list(filter(lambda elem: elem[key] == value, lordOfDicts))

def sort_data(data, sort_key):
    return sorted(data, key=lambda k: datetime.strptime(k[sort_key], '%d-%m-%Y'))

def get_x_and_y(data, title, key_x = "Date", key_y = "Stuff"):
    x = []
    y = []
    for i in data:
        x.append(i[key_x])
        y.append(int(i[key_y]))
    plt.plot(x, y,'b', x, y,"y*")
    plt.title(title)
    plt.grid(True)
    plt.ylim([min(y) - 1,max(y) + 1])
    plt.xlabel(key_x)
    plt.ylabel(key_y)
    plt.show()

def main(name):
    data = open_file(name)
    data, headers = prepearing_of_data(data)
    lstOfDicts = make_the_dict(headers, data)
    title = input("Number of the resourse:")
    dictionary = filter_dicts(lstOfDicts, headers[0], title)
    data = sort_data(dictionary, headers[1])
    print(headers)
    get_x_and_y(data, title, headers[1], headers[2])
#Подразумевается, что в файле сначала пишется ресурс, потом дата, потом количество произведенных товаров.
#Если порядок не такой, надо будет изменить индексы списка headers.
if __name__ == '__main__':
    main('input.txt')
