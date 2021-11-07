class Departments:
    items = {}

    def __init__(self, title):
        self.title = title


    def __str__(self):
        return self.title


    def show_items(self):
        print(f"В отделении {self} сейчас находятся: ")
        for key, value in self.items.items():
            print(f"{key} - {len(value)} штук")


class DepartmentOfMystery(Departments):
    pass





