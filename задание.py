workouts = [
    {"name": "Running", "burn_rate": 11, "type": "Cardio"},
    {"name": "Plank", "burn_rate": 5, "type": "Strength"}
]
categories = {"cardio", "strength"}  

def analyze_workout(w: dict, mins: int) -> tuple:
    total = w["burn_rate"] * mins  
    intensity = "High" if total > 150 else "Normal"
    return total, intensity
search = input("Категория (Cardio/Strength): ").strip().lower()
duration = int(input("Продолжительность (мин): "))

for w in workouts:
    if w["type"].lower() == search:
        calories, level = analyze_workout(w, duration)
        stars = "★" * (calories // 50) + "☆" * (5 - calories // 50)
        print(f"Активность: {w['name'].upper()[:10]} | {level} | {stars} ({calories} ккал)")