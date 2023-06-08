import datetime as dt
        
class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.date = date
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.format = "%d.%m.%Y"

    def add_record(self, records) :
        """
        Функция записи данных
        amount - стоимость / калории
        comment - комментарий
        (date) - дата (сегодня)
        """     
        self.records.append([records.amount, records.comment, records.date])


    def get_today(self):
        return dt.datetime.today().date()
    
    def get_today_stats(self):
        """
        Функция возвращает сумму калорий / денег
        потраченных за сегодняшний день
        today = дата на сегодня
        """
        today = self.get_today()
        return sum([i[0] 
                for i in self.records 
                if dt.datetime.strptime(i[2], self.format).date() == today])

    def get_week_stats(self):
        """
        Функция возвращает сумму калорий / денег
        потраченных за последнюю неделю
        today = дата сегодня
        first date = дата семь дней назад
        """
        today = self.get_today()
        first_date = today - dt.timedelta(days=7)
        return sum([i[0]
                for i in self.records if first_date
                < dt.datetime.strptime(i[2], self.format).date()
                <= today])


class CashCalculator(Calculator):
    def get_today_cash_remained():
        pass


class CaloriesCalculator(Calculator):
    def get_calories_remained():
        pass


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = Calculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=100, comment="кофе", date="08.06.2023"))
cash_calculator.add_record(Record(amount=111, comment="булка", date="08.06.2023"))
cash_calculator.add_record(Record(amount=111, comment="пятерочка", date="08.06.2023"))
cash_calculator.add_record(Record(amount=120, comment="магазин", date="02.06.2023"))
cash_calculator.add_record(Record(amount=120, comment="магазин", date="30.05.2023"))
cash_calculator.add_record(Record(amount=120, comment="магазин", date="09.06.2023"))
cash_calculator.add_record(Record(amount=120, comment="магазин", date="09.06.2023"))
print(cash_calculator.records)
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
# и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
# print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб