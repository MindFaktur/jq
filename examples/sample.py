import pyjq


class PyjqExamples:

    dict_value = {'name': 'vishwanath', 'details': {'address': 'iti', 'city': ['hubli','dharwad']}}

    def using_first_function(self):
        """
        print's first value of a list
        :return:
        """
        try:
            print('--------------' + '\n Print first value of an array')
            print(pyjq.first('{name, city: .city[]}', self.dict_value))
        except Exception as e:
            print(f"error occured at {e}")

    def using_one_function(self):
        """
        Prints the value if only one value matches the given string, else returns error
        :return:
        """
        try:
            print('--------------' + '\n print one value if only one value is returned')
            print(pyjq.one('.city[] | select(test("b"))', self.dict_value))
        except Exception as e:
            print(f"error occured at {e}")

    def using_all_function(self):
        """
        print's the whole list
        :return:
        """
        try:
            print('--------------' + '\n from the list')
            print(pyjq.all('{name, city:.city[]}', self.dict_value))
        except Exception as e:
            print(f"error occured at {e}")

        try:
            print('--------------' + '\n select a specific from the list')
            print(pyjq.all('{name, city:.city[]} | select(.city==$city)', self.dict_value, vars=({'city': 'hubli'})))
        except Exception as e:
            print(f"error occured at {e}")

        try:
            print('--------------' + '\n select the whole list')
            print(pyjq.all('{name, details:.details[]} | select(.details==$details)' , self.dict_value, vars=({'details':['hubli','dharwad']})))
        except Exception as e:
            print(f"error occured at {e}")


if __name__ == "__main__":
    PyjqExamples().using_first_function()
    PyjqExamples().using_one_function()
    PyjqExamples().using_all_function()
