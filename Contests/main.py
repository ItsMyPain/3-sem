class GasStation:
    val = 0
    cap = 0

    def __init__(self, c):
        self.cap = c

    # Конструктор, принимающий один параметр - ёмкость резервуара колонки
    # Резервуар создаётся пустой

    # Залить в резервуар колонки n литров топлива
    # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
    def fill(self, n):
        if self.val + n <= self.cap:
            self.val += n
        else:
            raise Exception

    # Заправиться, забрав при этом из резервура n литров топлива
    # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
    def tank(self, n):
        if self.val - n >= 0:
            self.val -= n
        else:
            raise Exception

    # Запросить остаток топлива в резервуаре
    def get_limit(self):
        return self.val
