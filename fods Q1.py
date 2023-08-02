import numpy as np

# Define the student_scores array (32 students with 4 subjects each)
student_scores = np.array([
    [80, 90, 85, 75], [70, 88, 95, 82], [90, 92, 78, 88], [85, 78, 80, 92],
    [78, 85, 88, 75], [92, 89, 90, 84], [88, 80, 85, 92], [75, 85, 90, 88],
    [82, 80, 78, 75], [90, 95, 92, 88], [88, 82, 90, 84], [80, 75, 85, 88],
    [78, 82, 85, 75], [92, 90, 88, 84], [85, 78, 80, 92], [75, 88, 90, 88],
    [90, 80, 78, 75], [89, 92, 95, 88], [88, 80, 85, 82], [75, 85, 90, 92],
    [82, 78, 80, 75], [85, 89, 90, 84], [90, 80, 85, 92], [88, 75, 85, 88],
    [78, 80, 78, 75], [92, 95, 92, 88], [85, 88, 80, 84], [75, 85, 90, 88],
    [82, 78, 80, 92], [85, 90, 88, 75], [90, 92, 85, 88], [88, 80, 85, 84]
])

# Calculate the average score for each subject
subject_average_scores = np.mean(student_scores, axis=0)

# Determine the subject with the highest average score
highest_avg_subject_index = np.argmax(subject_average_scores)

# Map the index back to the subject names
subjects = ["Math", "Science", "English", "History"]
subject_with_highest_avg_score = subjects[highest_avg_subject_index]

# Print the results
print("Average scores for each subject:", subject_average_scores)
print("Subject with the highest average score:", subject_with_highest_avg_score)
