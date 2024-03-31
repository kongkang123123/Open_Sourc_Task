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
    
    # Create a list to store ranks
    ranks = []
    
    # Assign ranks
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
        # Adjust column widths and right align as needed
        print(f"\t{Snum:<10}{name:<10}{eng:<5}{c:<8}{py:<8}{score:<5}{avg:<5}{grade:<5}{rank:<5}")
    print("=========================================================================================================")

# ----- Main function -----
def main():
    student = dict()
    for i in range(5):
        student = insert(student, i)
      
    ranks = cal_rank(student)
    print_(student, ranks)
    
if __name__ == '__main__':
    main()