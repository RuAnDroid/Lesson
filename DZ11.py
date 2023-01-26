import json
class OtherBox:
    def __init__(self,*args,**kwargs):
        self.base = {
            'name': 'Павел',
                     'surname': 'Anonim',
                     'age': 18,
                     'id': 1
        }

    def show_info(self):
        with open("data_file.json", 'w') as fw:
            json.dump(self.base, fw)

        with open("data_file.json", 'r') as fw:
            data = json.load(fw)

        print(data)



a = OtherBox()

a.show_info()