# -*- coding: utf-8 -*-
#prog.py

# ----- Enter grades -----
def insert(student, order):
    Snum = input(f"{order+1}번째 학번: ")
    name = input(f"{order+1}번째 이름: ")
    eng = int(input(f"{order+1}번째 영어: "))
    c = int(input(f"{order+1}번째 C-언어: "))
    py = int(input(f"{order+1}번째 파이썬: "))
    
    score = cal_total(eng, c, py)
    avg = cal_avg(score)
    grade = cal_grade(avg)
    
    student[Snum] = [Snum, name, eng, c, py, score, avg, grade]
    print("--------------------------")
    return student  

# ----- Total score calculation -----
def cal_total(eng, c, py):
    return eng + c + py

# ----- Average calculation -----
def cal_avg(score):
    return score / 3.0

# ----- Grade calculation -----
def cal_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return grade

# ----- Rank calculation -----
def cal_rank(student):
    avg_scores = [s[6] for s in student.values()]
    
    ranks = []
    
    for avg in avg_scores:
        rank = 1
        for other_avg in avg_scores:
            if other_avg > avg:
                rank += 1
        ranks.append(rank)
    
    return ranks

# ----- Result output -----
def print_(student, ranks):
    print("\t\t\t\t\t\t\t\t성적관리 프로그램\n\n")
    print("=========================================================================================================\n")
    print("\t학번\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\n\n")
    print("=========================================================================================================")
    for s, rank in zip(student.values(), ranks):
        Snum, name, eng, c, py, score, avg, grade = s
        print(f"\t{Snum:<10}{name:<10}{eng:<5}{c:<8}{py:<8}{score:<5}{avg:<5}{grade:<5}{rank:<5}")
    print("=========================================================================================================")


# ----- Delete a student -----
def delete(student, Snum):
    if Snum in student:
        del student[Snum]
        print(f"{Snum} 학번 학생 정보가 삭제되었습니다.")
    else:
        print("해당 학번의 학생 정보가 없습니다.")
    return student

# ----- Search a student by student number or name -----
def search(student, keyword):
    results = []
    for s in student.values():
        if keyword in s:
            results.append(s)
    if results:
        for result in results:
            print(result)
    else:
        print("검색 결과가 없습니다.")

# ----- Sort by total score -----
def sort_by_total(student):
    sorted_students = sorted(student.values(), key=lambda x: x[5], reverse=True)
    return sorted_students

# ----- Count students scoring above 80 -----
def count_above_80(student):
    count = sum(1 for s in student.values() if s[5] >= 240) # 총점이 240 이상인 경우를 카운트 (80점 이상인 경우)
    print(f"총점 80점 이상인 학생 수: {count}")

def menu():
    print("\n----- 성적 관리 프로그램 메뉴 -----")
    print("1. 학생 정보 입력")
    print("2. 학생 정보 삭제")
    print("3. 학생 정보 탐색")
    print("4. 총점으로 학생 목록 정렬")
    print("5. 총점 80점 이상 학생 수 카운트")
    print("6. 프로그램 종료")
    choice = input("실행할 메뉴를 선택하세요: ")
    return choice

def main():
    student = dict()
    while True:
        choice = menu()
        if choice == '1':
            order = len(student)
            student = insert(student, order)
        elif choice == '2':
            Snum = input("삭제할 학생의 학번을 입력하세요: ")
            student = delete(student, Snum)
        elif choice == '3':
            keyword = input("탐색할 학번 또는 이름을 입력하세요: ")
            search(student, keyword)
        elif choice == '4':
            sorted_students = sort_by_total(student)
            print("총점 순으로 정렬된 학생 목록:")
            for s in sorted_students:
                print(s)
        elif choice == '5':
            count_above_80(student)
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == '__main__':
    main()