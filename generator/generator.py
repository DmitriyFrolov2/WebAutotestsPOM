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
        mobile=faker_ru.msisdn(),

    )


def generate_file():
    file_name = f"{random.randint(0, 99)}.txt"

    downloads_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(downloads_dir, exist_ok=True)  # создаем папку, если её нет

    path = os.path.join(downloads_dir, file_name)

    with open(path, 'w+') as file:
        file.write("Hello World")

    return file_name, path


def generate_subject():
    subjects = {
        1: 'Hindi',
        2: 'English',
        3: 'Maths',
        4: 'Physics',
        5: 'Chemistry',
        6: 'Biology',
        7: 'Computer Science',
        8: 'Commerce',
        9: 'Accounting',
        10: 'Economics',
        11: 'Arts',
        12: 'Social Studies',
        13: 'History',
        14: 'Civics'
    }

    subjects_list = list(subjects.values())
    random_subject = random.choice(subjects_list)
    return random_subject
