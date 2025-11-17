from address import Address
from mailing import Mailing

mailing = Mailing({177056, "Москва", "Пушкина", 8, 56},
                  {177157, "Москва", "Маршала Жукова", 12, 79},
                  5237,
                  "H7563O9867G")

print(f"Отправление {track} из {Address} - в {Address}. Стоимость {cost} рублей.")