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