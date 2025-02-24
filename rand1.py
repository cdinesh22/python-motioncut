import random
import string
nouns = ["Dinesh","Tanu","Chandu","Poorna","Lokesh","Charan","Suma","Siri","Geetha","Anu","Manju"]
adjectives=["Shiny","Fast","Silly","Wild","Cool","Happy","Brave","Clever","Fierce","Swift","Bold","Lively"]
def generate_username(include_numbers=True,include_special_chars=True,length=None):
    adj=random.choice(adjectives)
    noun=random.choice(nouns)
    username=adj+noun
    if include_numbers:
        username += str(random.randint(10,99))
    if include_special_chars:
        username += random.choice(string.punctuation)    
    if length and len(username) > length:
        username = username[:length]
    return username
def save_username_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
def main():
    print("Welcome to the Random Username Generator!")
    while True:
        try:
            num_usernames=int(input("How many usernames would you like to generate? "))
            include_numbers=input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_special_chars=input("Include special characters? (yes/no): ").strip().lower() == "yes"
            length = input("Set a maximum length for the username (press Enter to skip): ")
            length = int(length) if length.isdigit() else None
            print("\nGenerated Usernames:")
            for _ in range(num_usernames):
                username = generate_username(include_numbers,include_special_chars,length)
                print(username)
                save_username_to_file(username)
            print("\nUsernames saved to 'usernames.txt'.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        again = input("\nDo You Want To Generate more usernames?(yes/no): ").strip().lower()
        if again!= "yes":
            print("THANKYOU!")
            break
main()
