class Clients:
    def __init__(self, client_name, client_balance):
        self.client_name = client_name
        self.client_babance = client_balance

    def set_balance(self, client_balance):
        if client_balance > 0 and isinstance(client_balance, int):
            self.client_babance = client_balance

    def get_about_client(self):
        return str(f'Клиент {self.client_name}. Баланс: {self.client_babance} руб.')