grade_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
              {'school_class': '4б', 'scores': [5, 4, 5, 5, 3]},
              {'school_class': '4в', 'scores': [3, 3, 2, 5, 1]},
              {'school_class': '4г', 'scores': [2, 3, 4, 1, 4]}]
school_class_mean = []
for class_scores in grade_list:
    mean = sum(class_scores['scores']) / len(class_scores['scores'])
    school_class_mean.append(mean)
    print(class_scores['school_class'], mean)
print(sum(school_class_mean) / len(school_class_mean))
