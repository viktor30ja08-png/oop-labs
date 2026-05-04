class EducationalInstitution:

    def __init__(self, name: str, accreditation_level: int, student_count: int, foundation_year: int, is_public: bool):
        self.name = name
        self.accreditation_level = accreditation_level
        self.student_count = student_count
        self.foundation_year = foundation_year
        self.is_public = is_public

    def __repr__(self):

        public_status = "Державний" if self.is_public else "Приватний"
        return (f"Навчальний заклад: '{self.name}' | Акредитація: {self.accreditation_level} | "
                f"Студентів: {self.student_count} | Засновано: {self.foundation_year} | Тип: {public_status}")

    def __eq__(self, other):

        if not isinstance(other, EducationalInstitution):
            return False
        return (self.name == other.name and
                self.accreditation_level == other.accreditation_level and
                self.student_count == other.student_count and
                self.foundation_year == other.foundation_year and
                self.is_public == other.is_public)


def sort_institutions(institutions: list):

    return sorted(institutions, key=lambda inst: (inst.accreditation_level, -inst.student_count))


def find_institution(institutions: list, target_institution: EducationalInstitution):

    try:
        index = institutions.index(target_institution)
        return index, institutions[index]
    except ValueError:
        return -1, None


def main():
    try:

        institutions = [
            EducationalInstitution("ЛНУ ім. Франка", 4, 22000, 1661, True),
            EducationalInstitution(
                "КПІ ім. Ігоря Сікорського", 4, 25000, 1898, True),
            EducationalInstitution("Коледж Інформатики", 2, 1200, 1995, False),
            EducationalInstitution("КНУ ім. Шевченка", 4, 26000, 1834, True),
            EducationalInstitution("Приватний Ліцей", 1, 300, 2010, False)
        ]

        print("--- ПОЧАТКОВИЙ МАСИВ ---")
        for inst in institutions:
            print(inst)

        sorted_institutions = sort_institutions(institutions)

        print("\n--- ВІДСОРТОВАНИЙ МАСИВ ---")
        for inst in sorted_institutions:
            print(inst)

        print("\n--- ПОШУК ОБ'ЄКТА ---")

        target_to_find = EducationalInstitution(
            "КПІ ім. Ігоря Сікорського", 4, 25000, 1898, True)
        print(f"Шукаємо: {target_to_find}")

        idx, found_obj = find_institution(sorted_institutions, target_to_find)

        if idx != -1:
            print(f" Об'єкт знайдено! Індекс у відсортованому масиві: {idx}")
        else:
            print(" Об'єкт не знайдено.")

    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    main()
