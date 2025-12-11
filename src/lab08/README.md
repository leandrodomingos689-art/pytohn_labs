# ЛР8 – ООП в Python: @dataclass Student, методы и сериализация
## A. Реализовать класс Student (models.py)
```python

from dataclasses import dataclass
import datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        Data validation after initialization (after __init__).
        Date of birth format and gpa range validations.
        Date format must be in ISO format (YYYY-MM-DD). Ex: 2025-12-01.
        Gpa must be between 0.0 and 5.0.
        """
        # Add proper validation of date format and gpa range (YYYY-MM-DD)
        try:
            # datetime.strptime(self.birthdate, "%Y/%m/%d")
            # String birthdate -> Python object ISO Fortmat for DateAndTime
            birth_date_obj = datetime.date.fromisoformat(self.birthdate)
        except ValueError:
            # (Ideally, there should be raise ValueError(...) here.)
            # print("warning: birthdate format might be invalid")
            raise ValueError(
                f"Invalid date format for 'birthdate': {self.birthdate}. Expected YYYY-MM-DD."
            )
        if datetime.date.today() < birth_date_obj:
            raise ValueError(
                "Invalid date range. Date of birth cannot be later than today's date."
            )
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa must be between 0.0 and 5.0")

    def age(self) -> int:
        """
        Calculating Age.
        """
        today = datetime.date.today()  # Gets DateAndTIme from the computer's System.
        birth_date_obj = datetime.date.fromisoformat(self.birthdate)
        years_difference = today.year - birth_date_obj.year  # Student's age.
        if (today.month, today.day) < (birth_date_obj.month, birth_date_obj.day):
            years_difference -= 1  # if the birthday hasn't arrived yet.
        return years_difference

    def to_dict(self) -> dict:
        """
        Serializes the Student object into a dictionary.
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod  # Allows you to create a new instance of Student from an existing dictionary.
    def from_dict(cls, d: dict):
        """
        Deserializes a dictionary into a Student object.
        Uses cls() which calls __init__ and subsequently __post_init__ for validation.
        """
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        """
        Returns the Student class data in string format, understandable to the user.
        """
        return (
            f"Student: {self.fio}\n"
            f" Group: {self.group}\n"
            f" Age: {self.age()} years old\n"
            f" GPA: {self.gpa:.2f}"
        )

```

# B. Реализовать модуль serialize.py
```python
import json
from lab08.models import Student


def students_to_json(students: list[Student], path: str):
    """
    Serializes datas into a JSON file.
    """
    # Creates the serialization to write the serialized data to the JSON file.
    data_to_JSON = [s.to_dict() for s in students]
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data_to_JSON, f, ensure_ascii=False, indent=2)
        print(f"Data successfully saved to '{path}'.")
    except ValueError as e:
        print(f"Error writing to file {path}: {e}")


def students_from_json(path) -> list[Student]:
    """
    Disserializes datas from a JSON file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data_from_json = json.load(f)
        if not isinstance(data_from_json, list):
            raise TypeError(
                "Expected JSON list/array, but got a diferent type"
            )
        students = []  # Creates a new empty list
        for item in data_from_json:
            try:
                student = Student.from_dict(
                    item
                )  # Disserialize the items in "data_from_json"
                students.append(student)  # Save to the list.
            except:
                raise ValueError(f"Error processing student data from JSON: {item}")
        return students
    except:
        raise ValueError("Error: File Not Found!!!")


# --------Runing funcions--------#
if __name__ == "__main__":
    students_list = [
        Student("Sebastião Leandro João Domingos", "2004-06-19", "БИВТ-6", 4.1),
        Student("Marcela Leandro João Domingos", "1999-09-30", "A-50", 4.3),
        Student("Domingas Leandro João", "1998-10-20", "M-6", 4.2),
    ]
    students_to_json(students_list, "data/lab08/students_output.json")
    loaded_students = students_from_json("data/lab08/students_input.json")
    print(f"Disserialized data (str):\n {loaded_students}")

```
# Result - Serialize and Disserialized
![](../../img/lab08/serialise.png)

# Json_output

![](../../img/lab08/output.json.png)

# Json_input
![](../../img/lab08/input.json.png)
