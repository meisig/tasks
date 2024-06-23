class Mark:
    def __init__(self, subject: str, value: int):
        self.subject = subject
        self.value = value

    def __repr__(self):
        return f"{self.subject}: {self.value}"


class Student:
    def __init__(self, name: str):
        self.name = name
        self.marks = []

    def add_mark(self, subject: str, value: int):
        self.marks.append(Mark(subject, value))

    def remove_mark(self, subject: str):
        self.marks = [mark for mark in self.marks if mark.subject != subject]

    def edit_mark(self, subject: str, new_value: int):
        for mark in self.marks:
            if mark.subject == subject:
                mark.value = new_value
                break

    def __repr__(self):
        return f"Student: {self.name}, Marks: {self.marks}"



student = Student("Черносенко Максим")


student.add_mark("Математика", 85)
student.add_mark("Алгоритми", 90)
print(student)


student.edit_mark("Математика", 95)
print(student)

student.remove_mark("Алгоритми")
print(student)