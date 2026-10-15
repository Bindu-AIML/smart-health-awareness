# SDG 3: Good Health and Well-Being
# Smart Health Awareness and Early Disease Prevention System

from datetime import datetime

def health_awareness():
    print("\n--- HEALTH AWARENESS ---")
    print("1. Wash your hands regularly.")
    print("2. Eat balanced and nutritious food.")
    print("3. Exercise regularly.")
    print("4. Get enough sleep.")
    print("5. Visit a doctor for regular health check-ups.")
    print("6. Follow recommended vaccination schedules.")

def disease_prevention():
    print("\n--- DISEASE PREVENTION ---")
    print("1. Maintain personal hygiene.")
    print("2. Drink safe and clean water.")
    print("3. Eat fresh and healthy food.")
    print("4. Avoid close contact when you are sick.")
    print("5. Consult a healthcare professional if you feel unwell.")

def healthy_lifestyle():
    print("\n--- HEALTHY LIFESTYLE TIPS ---")
    print("1. Drink water regularly.")
    print("2. Include fruits and vegetables in your meals.")
    print("3. Stay physically active.")
    print("4. Maintain a regular sleep schedule.")
    print("5. Take care of your mental well-being.")

def wellness_tracker():
    print("\n--- DAILY WELLNESS TRACKER ---")

    try:
        water = float(input("Enter water consumed (in litres): "))
        sleep = float(input("Enter sleep duration (in hours): "))
        exercise = int(input("Enter exercise duration (in minutes): "))

        if water < 0 or sleep < 0 or sleep > 24 or exercise < 0:
            print("Please enter valid, non-negative values.")
            return

        print("\n--- YOUR WELLNESS REPORT ---")
        print("Date:", datetime.now().strftime("%d-%m-%Y"))
        print("Water intake:", water, "litres")
        print("Sleep duration:", sleep, "hours")
        print("Exercise duration:", exercise, "minutes")

        print("\nGeneral Suggestions:")

        if water < 1:
            print("- Remember to drink water regularly.")
        else:
            print("- Continue staying hydrated according to your needs.")

        if sleep < 7:
            print("- Consider whether you are getting enough sleep.")
        else:
            print("- Maintain a regular sleep routine.")

        if exercise < 20:
            print("- Try including some suitable physical activity.")
        else:
            print("- Keep maintaining regular physical activity.")

        print("\nNote: These suggestions are general, not medical advice.")

    except ValueError:
        print("Invalid input. Please enter numbers.")

def main():
    while True:
        print("\n====================================")
        print(" SDG 3: GOOD HEALTH AND WELL-BEING")
        print("====================================")
        print("1. Health Awareness")
        print("2. Disease Prevention")
        print("3. Healthy Lifestyle Tips")
        print("4. Daily Wellness Tracker")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            health_awareness()

        elif choice == "2":
            disease_prevention()

        elif choice == "3":
            healthy_lifestyle()

        elif choice == "4":
            wellness_tracker()

        elif choice == "5":
            print("Thank you for using our Health Awareness System!")
            print("Stay healthy and take care!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")

if __name__ == "__main__":
    main()
