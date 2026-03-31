# Student Performance Prediction (Without any library)

print("Enter Student Details:")

study_hours = float(input("Study Hours per day: "))
attendance = float(input("Attendance (%): "))
sleep_hours = float(input("Sleep Hours: "))
previous_score = float(input("Previous Score: "))

# Simple formula (manually designed logic)
predicted_score = (
    (study_hours * 5) +
    (attendance * 0.3) +
    (sleep_hours * 2) +
    (previous_score * 0.5)
) / 2

print("\nPredicted Final Score:", round(predicted_score, 2))

# Recommendation System
if predicted_score < 60:
    print("Recommendation: Increase study hours and focus more.")
elif 60 <= predicted_score < 75:
    print("Recommendation: Keep practicing and stay consistent.")
else:
    print("Recommendation: Excellent! Keep it up and try advanced topics.")