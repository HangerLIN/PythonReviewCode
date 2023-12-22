import functools

sno = ['HS9801', 'HS9802', 'HS9803', 'HS9804', 'HS9805']
scores = [65, 98, 85, 85, 53]
grade = dict(zip(sno, scores))
max(grade)
print(max(grade, key=grade.get))
print(max(grade.values())
      )
sno, maxscore = max(grade.items(), key=lambda item: item[1])
print(sno, maxscore)

list1 = [1, 2, 3, 4, 5, 6]


def func(a, b):
    return a + b


result = functools.reduce(func, list1)
print(result)
