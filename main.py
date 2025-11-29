#1-misol
result = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(result)

#2-misol
s = "salom"

result = [char * 2 for char in s]
print(result)

#3-misol
def grade_marks(marks):
    result = []
    for m in marks:
        if m >= 90:
            result.append("A")
        elif m >= 70:
            result.append("B")
        elif m >= 50:
            result.append("C")
        else:
            result.append("D")
    return result

print(grade_marks((95, 67, 40, 82)))

#4-misol
def classify_names(names):
    result = []
    for name in names:
        if len(name) < 3:
            result.append("juda qisqa")
        elif 3 <= len(name) <= 5:
            result.append("normal")
        else:
            result.append("uzun")
    return result

print(classify_names(["Ali", "Doniyor", "Ziyod", "Noz"]))



