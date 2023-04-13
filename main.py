print("Advanced Physics Multiple Choice Quiz")
questions = [
    {
    "question": "What is the equation for calculating the area of a circle?",
    "options": ["A = πr²", "A = 2πr", "A = πd", "A = 4πr²"],
    "answer": "1"
    },
    {
        "question": "What is the equation for calculating the maximum height of a projectile under constant acceleration due to gravity?",
        "options": ["h = v₀² / 2g", "h = v₀t - (1/2)gt²", "h = (v₀²sin(2θ)) / g", "h = (v₀t)² - (1/2)gt²"],
        "answer": "2"
    },
    {
        "question": "What is the equation for the force of friction between two objects in contact?",
        "options": ["F = μN", "F = μW", "F = μF", "F = μP"],
        "answer": "1"
    },
    {
        "question": "What is the equation for calculating the speed of a wave?",
        "options": ["v = λf", "v = f / λ", "v = λ / f", "v = fΛ"],
        "answer": "1"
    },
    {
    "question": "What is the equation for calculating the electrostatic potential energy between two point charges?",
    "options": ["U = k(q1 + q2)/r", "U = (1/4πε₀)q1q2/r", "U = k(q1q2)/r²", "U = (1/4πε₀)(q1 + q2)/r²"],
    "answer": "3"
    },
    {
    "question": "What is the equation for calculating the magnetic field produced by a long straight wire carrying a current I at a distance r from the wire?",
    "options": ["B = (μ₀I)/(2πr)", "B = (μ₀I)/(4πr)", "B = (μ₀I²)/(2πr)", "B = (μ₀I²)/(4πr)"],
    "answer": "1"
    },
    {
    "question": "What is the equation for calculating the angular frequency of a mass-spring system?",
    "options": ["ω = √(k/m)", "ω = (1/2π)√(k/m)", "ω = (2π)√(k/m)", "ω = √(m/k)"],
    "answer": "2"
    },
    {
    "question": "What is the equation for calculating the work done by a variable force F(x) on an object moving from x1 to x2?",
    "options": ["W = ∫F(x)dx from x1 to x2", "W = F(x2) - F(x1)", "W = F(x1) + F(x2)", "W = F(x1)x1 + F(x2)x2"],
    "answer": "1"
    },
    {
    "question": "What is the equation for calculating the period of a simple pendulum of length L and mass m?",
    "options": ["T = 2π√(L/g)", "T = 2π√(g/L)", "T = 2π√(m/L)", "T = 2π√(L/mg)"],
    "answer": "1"
    },
    {
    "question": "What is the equation for calculating the energy of a photon with frequency f?",
    "options": ["E = hf", "E = h/f", "E = f/h", "E = h²f"],
    "answer": "1"
    }
    ]

correct = 0

for question in questions:
    print(question["question"])
    print("Options:")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter the correct option number: ")
    if answer == question["answer"][0]:
        correct += 1
        print("Correct")
    else:
        print("Incorrect")

percentage = (correct / len(questions)) * 100
if percentage > 80:
    grade = "A"
elif percentage > 60:
    grade = "B"
else: grade = "Fail"
print(f"Your score is {correct} out of {len(questions)} ({percentage:.2f}%) {grade}")
