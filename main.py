students_db = [
    {"id": 1, "name": "Алексей", "grades": [5, 4, 5, 3]},
    {"id": 2, "name": "Мария", "grades": [4, 5, 4]},
    {"id": 3, "name": "Иван", "grades": []},
    {"id": 4, "name": "Ольга", "grades": [3, 2, 3, "4"]},
]


def get_average_grade(student):
    # Считает средний балл студента
    total = 0
    count = 0
    for num in student["grades"]:
        if type(num) == int:
            total += num
            count += 1
    if count == 0:
        return 0
    return total / count

def find_student_by_id(student_id):
    # Ищет студента по ID
    for student in students_db:
        if str(student["id"]) == str(student_id).strip():
            return student
    return None

def add_new_student(name, grades_str):
    try:
        if name and name.strip():
            grades = [int(g.strip()) for g in grades_str.split(",")]
            new_id = max((s["id"] for s in students_db), default=0) + 1
            new_student = {"id": new_id, "name": name, "grades": grades}
            students_db.append(new_student)
            print(f" Студент {name} успешно добавлен с ID {new_id}!")

        elif not name:
            raise SyntaxError('Недопустимое значение')

    except SyntaxError:
        print("Пустая строка!")

    except ValueError:
        print("Введите числа!")



def print_report():
    # Выводит красивый отчет по всем студентам
    print("\n--- ОТЧЕТ УСПЕВАЕМОСТИ ---")
    for student in students_db:
        avg = get_average_grade(student)
        print(f"[{student['id']}] {student['name']} | Средний балл: {avg:.2f}")

def delete_student(student_id):
    student = find_student_by_id(student_id)

    if student:
        students_db.remove(student)
    else:
        print("Student not found")


def main():
    while True:
        print("\n Меню:")
        print("1. Показать отчет")
        print("2. Найти студента по ID")
        print("3. Добавить студента")
        print("4. Удаление")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_report()
        elif choice == "2":
            sid = input("Введите ID студента: ")
            student = find_student_by_id(sid)
            if student:
                print(f"Найдено: {student['name']}, Оценки: {student['grades']}")
            else:
                print("Студент не найден")
        elif choice == "3":
            name = input("Имя студента: ")
            grades = input("Оценки через запятую (например: 4,5,3): ")
            add_new_student(name, grades)
        elif choice == "4":
            student_id = input("...")
            delete_student(student_id)
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()
