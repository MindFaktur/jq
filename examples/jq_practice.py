import pyjq
import json

class WriteToFile:

    @staticmethod
    def write_dict():
        f = open("practice_int.txt", 'w')
        dict_value = {'name': 'vishwanath', 'details': {'address': 'iti', 'city': ['hubli','dharwad']}}
        f.write(str(dict_value))
        f.close()


class JqReader:

    @staticmethod
    def read_int():
        WriteToFile.write_dict()
        f = open("practice_int.txt", 'r')
        data = f.read()
        print(f.read().title())
        print(pyjq.all('', data))


if __name__ == "__main__":
    JqReader.read_int()




