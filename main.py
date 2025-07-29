import random
import os

def get_user_info():

    user_data = {}

    questions = [
        {"key": "name", "prompt": "What is your name? "},
        {"key": "age", "prompt": "What is your age? "},
        {"key": "gender", "prompt": "What is your gender? "},
        {"key": "fav_food", "prompt": "What is your favorite food? "},
        {"key": "fav_color", "prompt": "What is your favorite color? "},
        {"key": "shs", "prompt": "What is the name of the SHS you attended? "}, # Corrected prompt for clarity
        {"key": "city", "prompt": "What is the name of the city you live in? "},
    ]

    random.shuffle(questions)

    for question in questions:

        if question["key"] == "age":
            while True:
                try:
                    age_input = input(question["prompt"]).strip()
                    if age_input.isdigit():
                        user_data[question["key"]] = age_input
                        break
                    else:
                        print("Invalid input. Please enter a number for your age.")
                except ValueError:
                    print("Invalid input. Please enter a number for your age.")
        else:
            user_data[question["key"]] = input(question["prompt"]).strip()

    return user_data

def gen_summary(user_data):

    name = user_data.get("name", "there")
    age = user_data.get("age", "an unknown age")
    gender = user_data.get("gender", "an unknown gender")
    fav_food = user_data.get("fav_food", "no specific favorite food")
    fav_color = user_data.get("fav_color", "no specific favorite color")
    shs = user_data.get("shs", "no particular SHS")
    city = user_data.get("city", "no specific city")

    summary = (
        f"Hello {name}! You are {age} years old and identify as {gender}. "
        f"You love eating {fav_food}, and your favorite color is {fav_color}. "
        f"You attended {shs}, and currently live in {city}. "
        
        "Thanks for sharing your details!"
    )

    return summary

def save_summary(filename, content):

    try:
        with open(filename, "w") as f:
            f.write(content)
            print(f"Summary saved to {filename}")
    except IOError as e:
        print(f"Error while saving summary to {filename}: {e}")

def main():
    while True:
        print("\n--- Simple Personal Assistant ---")
        user_info = get_user_info()
        summary = gen_summary(user_info)
        print("\n--- Your Summary: ---")
        print(summary)

        while True:
            save_option = input("\nDo you wish to save this summary to a file? (yes/no) ").lower().strip()
            if save_option in ["yes", "y"]:

                filename = f"{user_info.get('name', 'summary').replace(' ', '_').replace('.', '')}.txt"

                while True:
                    try:
                        rating = int(input("Please rate the assistant (1 to 5 stars): "))
                        if 1 <= rating <= 5:
                            break
                        else:
                            print("Please enter a number between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                full_content_to_save = f"{summary}\n\nAssistant Rating: {rating} out of 5 stars."
                save_summary(filename, full_content_to_save)
                break
            elif save_option in ["no", "n"]:
                print("Summary not saved.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        while True:
            restart_option = input("\nDo you want to restart the process? (yes/no): ").lower().strip()
            if restart_option in ["yes", "y"]:
                break
            elif restart_option in ["no", "n"]:
                print("Thank you for using the Simple Personal Assistant. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
