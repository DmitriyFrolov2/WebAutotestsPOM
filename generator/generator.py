import random
import os
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 60),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

    )


def generate_file():
    """Генерирует файл и возвращает ТОЛЬКО имя файла"""
    file_name = f"{random.randint(0, 99)}.txt"
    path = os.path.join(os.getcwd(), "downloads", file_name)
    with open(path, 'w+') as file:
        file.write(f'Hello World{random.randint(0, 99)}')
    return file_name  # Только имя, без пути

