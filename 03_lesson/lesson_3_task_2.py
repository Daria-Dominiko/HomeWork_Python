from smartphone import Smartphone

catalog = [
    Smartphone("samsung", "XX10", "+79293451524"),
    Smartphone("huawei", "HG34", "+79456458723"),
    Smartphone("xiaomi", "Uh354", "79776457843"),
    Smartphone("oppo", "super45", "+79457651863"),
    Smartphone("vivo","smart07", "+79197397625")
]

for smartphone in catalog:
    print(f"{smartphone.brand_phone} - {smartphone.model_phone} - {smartphone.number}")