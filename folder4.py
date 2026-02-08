import json
import os

print("\n------ Welcome to Py high School ------\n") 

def basic_info():

    print("\n---INFORMATION---")
    print("Please complete the following information carefully\n")

    while True:
        name = input("Name: ")
        while not name.replace(" ","").isalpha():
            print("\n*Only letters allowed! ")
            name = input("Name: ")

        last_name = input("Last name: ")
        while not last_name.isalpha():
            print("\n*Only letters allowed! ")
            last_name = input("Last name: ")

        print("\n(Only ages 14 to 19 are allowed!) ")
        age_input = input("Age: ")

        if not age_input.isdigit():
            print("\n*Age must be a number!")
            continue

        age = int(age_input)
        if age < 14 or age > 19:
            print("\n*You are not allowed to register in this age!")
            return
    
        country = input("country you currently live in: ")
        while not country.isalpha():
            print("\n*Only enetr your country name!")
            country = input("country you currently live in: ")

        city = input("City you live in: ")
        while not city.replace(" ","").isalpha():
            print("\n*Only enetr your city name!")
            city = input("City you live in: ")

        addr = input("Home address (Approximate): ")
        while addr.strip() == "":
            print("\n*Address can't be empty!")
            addr = input("Home address (Approximate): ")

        lang = input("Native language: ")
        while not lang.replace(" ","").isalpha():
            print("\n*Only letter please!")
            lang = input("Native language: ")

        return name, last_name, age, country, city, addr, lang


def score_info():
    scores = []
    print("\n-----SCORE-----")
    print("Please enter your scores at school ")

    for subject in ["Math", "Physics", "Chemistry", "Geometry", "English"]:
        while True:
            score_input = input(f"{subject} score: ")

            if not score_input.isdigit():
                print("*Only numbers allowed!")
                continue

            score = int(score_input)
            if score < 0 or score > 20:
                print("\n *Score must be between 0 and 20!")
                continue

            scores.append(score)
            break
    return scores

def skills():

    print("\n-----SKILL-----")
    all_skills = []

    main_skills = {
        "1": "Programming",
        "2": "Art",
        "3": "Sports",
        "4": "Other"
    }

    sub_skills = {
        "Programming": ["Python", "Web", "Game Dev", "Other"],
        "Art": ["Drawing", "Painting", "Music", "Other"],
        "Sports": ["Football", "Basketball", "Cycling", "Other"],
        "Other": ["No specific skill"]
    }

    while True:

        print("\nChoose your main skill:")
        for k, v in main_skills.items():
            print(k, "-", v)

        choice = input("Your choice: ")
        if choice not in main_skills:
            print("*Invalid choice!")
            continue

        main_skill = main_skills[choice]
        options = sub_skills[main_skill]

        print("\nSub skills:")
        for i, s in enumerate(options, start=1):
            print(i, "-", s)

        sub_choice = input("Select sub skill: ")
        if not sub_choice.isdigit() or not (1 <= int(sub_choice) <= len(options)):
            print("*Invalid choice!")
            continue

        sub_skill = options[int(sub_choice)-1]

        all_skills.append((main_skill, sub_skill))

        again = input("\nDo you have another skill? (Y/N): ").lower()
        if again != "y":
            break

    return all_skills

def personality_test():

    print("\n---PERSONALITY---")
    questions = [
        "Do you prefer to work alone?",
        "Do you actively participate in team projects?",
        "Do you usually take the lead in group work?",
        "Are you comfortable making decisions for others?",
        "Do you feel motivated about your future?",
        "Do you usually wake up with a sense of purpose?",
        "Do you have big long-term goals?",
        "Are you willing to work hard for big goals?",
        "Do you plan your weekly tasks?",
        "Do you schedule your work before starting?"
    ]

    score = 0
    answers = []

    for q in questions:
        while True:
            ans = input(q+ "Y/N: ").lower()
            if ans in ["y","n"]:
                break
            print("*Only (Y/N)!")
        
        answers.append(ans)

        if ans == "y":
            score += 1
    
    return score, answers 


def save_student(student_data):

    file_name = "student.json"

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(student_data)

    with open(file_name, "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4)


def run_registration():
    info = basic_info()
    if info is None:
        print("Registration stopped!")
        return
    
    name, last_name, age, country, city, addr, lang = info

    scores = score_info()
    skill_list = skills()
    p_score, p_answers =  personality_test()

    avg= sum(scores) / len(scores)

    no_low_score = all(s >= 10 for s in scores)
    enough_avg = avg >= 14
    enough_skills = len(skill_list) >2
    good_personality = p_score >= 5

    accepted = all([
        no_low_score,
        enough_avg,
        enough_skills,
        good_personality
    ])

    status = "Accepted" if accepted else "Rejected"

    student = {
            "name": name,
            "last_name": last_name,
            "age": age,
            "country": country,
            "city": city,
            "address": addr,
            "language": lang,
            "scores": scores,
            "skills": skill_list,
            "personality_score": p_score,
            "personality_answers": p_answers,
            "status" : status
        }
    
    save_student(student)

    print("Registration result: ", status)

def show_students():

    if not os.path.exists("student.json"):
        print("No data file!")
        return
    
    with open("student.json", "r", encoding="UTF-8") as f :
        data = json.load(f)

    for i, st in enumerate(data, start=1):
        print("\n#", i)
        print(st["name"], st["last_name"])
        print("Age: ", st["age"])
        print("Status: ", st["status"])

def delete_student():

    if not os.path.exists("student.json"):
        print("No data file!")
        return
    
    with open("student.json", "r", encoding="UTF-8") as f:
        data = json.load(f)

    for i, st in enumerate(data, start=1):
        print(i, "-", st["name"], st["last_name"])

    idx_input = input("Number to delete: ")
    if not idx_input.isdigit():
        print("*Invalid number!")
        return
    
    idx = int(idx_input) -1

    if 0 <= idx < len(data):
        data.pop(idx)

        with open("student.json", "w", encoding="UTF-8") as f:
            json.dump(data, f , indent=4)
        
        print("Deleted")
    else:
        print("Invalid number")


def main_menu():
    while True:
        print("\n------MENU------")
        print("1- New registration")
        print("2- Show students")
        print("3- delete student")
        print("4- Exit")

        choice = input("Choose: ")

        if choice == "1":
            run_registration()
        elif choice == "2":
            show_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("GoodBye (:")
            break
        else:
            print("*Invalid Choice!")

main_menu() 