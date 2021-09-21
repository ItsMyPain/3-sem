class MoneyBox:
    storage = {}

    def add_coin(self, value):
        if self.storage.get(value):
            self.storage[value] += 1
        else:
            self.storage.setdefault(value, 1)

    # Получить текущее количество монеток в копилке
    def get_coins_number(self):
        return sum(v for k, v in self.storage.items())

    # Получить текущее общее достоинство всех монеток
    def get_coins_value(self):
        return sum(k * v for k, v in self.storage.items())

