from dataclasses import dataclass


@dataclass
class Person():
    full_name: str
    firstname: str
    lastname: str
    age: int
    salary: int
    department: str
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

@dataclass
class Color:
    color_name: list = None