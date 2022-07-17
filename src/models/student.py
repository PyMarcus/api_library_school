from datetime import date
from typing import Optional

from MySQLdb.times import Date
from pydantic import BaseModel


class Student(BaseModel):
    nome: str
    email: str
    data_nascimento: str
