from address import Address
from mailing import Mailing

mailing = Mailing("{address1}",
                  "{address2}",
                  5237,
                  "H7563O9867G")

address1 = Address(177056, "Москва", "Пушкина", 8, 56)

address2 = Address(177157, "Москва", "Маршала Жукова", 12, 79)

print(f'Отправление {track} из {from_address} - в {to_address}. Стоимость {cost} рублей.')