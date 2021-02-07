class Personal:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_about_personal(self):
        return str(f'Сотрудник {self.name}, г. {self.city}')

class Status(Personal):
    type = "Status"
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def get_status(self):
        return str(f'Сотрудник {self.name} из г. {self.city}, статус {self.status}')

