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

    def add_record(self, records) :
        # print(f"Запись от {records.date} с комментарием '{records.comment}' доабавлена!")     
        self.records.append([records.amount, records.comment, records.date])

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = Calculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе", date="08.11.2019"))
cash_calculator.add_record(Record(amount=145, comment="булка", date="08.11.2019"))
cash_calculator.add_record(Record(amount=145, comment="пятерочка", date="08.11.2019"))
cash_calculator.add_record(Record(amount=145, comment="магазин", date="09.11.2019"))
print(cash_calculator.records)
# и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
# print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб