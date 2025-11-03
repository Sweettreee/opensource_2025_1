# 학생 클래스 정의
class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_total(self):
        return self.english + self.c_language + self.python

    def calculate_average(self):
        return round(self.total / 3, 2)

    def calculate_grade(self):
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'

# 학생 리스트 및 관련 함수 정의
students = []

def input_student():
    for _ in range(5):  # 5명의 학생 입력
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_language = int(input("C언어 점수: "))
        python = int(input("파이썬 점수: "))
        students.append(Student(student_id, name, english, c_language, python))

def display_students():
    print("\n학생 정보 출력:")
    print(f"{'학번':<10}{'이름':<10}{'영어':<6}{'C언어':<6}{'파이썬':<6}{'총점':<6}{'평균':<6}{'등급':<6}")
    for student in students:
        print(f"{student.student_id:<10}{student.name:<10}{student.english:<6}{student.c_language:<6}"
              f"{student.python:<6}{student.total:<6}{student.average:<6}{student.grade:<6}")

def search_student(student_id):
    for student in students:
        if student.student_id == student_id:
            print(f"학번: {student.student_id}, 이름: {student.name}, 총점: {student.total}, 평균: {student.average}, 등급: {student.grade}")
            return
    print("해당 학번의 학생을 찾을 수 없습니다.")

def delete_student(student_id):
    global students
    students = [student for student in students if student.student_id != student_id]
    print(f"학번 {student_id} 학생 삭제 완료.")

def sort_students():
    global students
    students.sort(key=lambda x: x.total, reverse=True)
    print("학생 정렬 완료 (총점 기준 내림차순).")

def count_high_achievers():
    count = sum(1 for student in students if student.average >= 80)
    print(f"평균 점수가 80점 이상인 학생 수: {count}")

# 메인 프로그램 실행
def main():
    while True:
        print("\n성적 관리 프로그램")
        print("1. 학생 입력")
        print("2. 학생 출력")
        print("3. 학생 검색")
        print("4. 학생 삭제")
        print("5. 학생 정렬")
        print("6. 평균 80점 이상 학생 수 출력")
        print("7. 종료")

        choice = input("선택: ")
        
        if choice == '1':
            input_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            student_id = input("검색할 학번 입력: ")
            search_student(student_id)
        elif choice == '4':
            student_id = input("삭제할 학번 입력: ")
            delete_student(student_id)
        elif choice == '5':
            sort_students()
        elif choice == '6':
            count_high_achievers()
        elif choice == '7':
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()

// by perplexity
