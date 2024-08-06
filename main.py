import requests
import html
import random

#Functions

def get_questions(amount: int, category: int) -> list:  #Returns a list
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

def shuffel_choices(choices : list) -> list:
    random.shuffle(choices)
    return choices

def print_choices(choices: list) -> None:
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}.{html.unescape(choice)}")

def get_user_choice() -> int:
    while True:
        user_choice = int(input("Enter the number of your choice: ")) 
        if user_choice in range(1,5):
            return user_choice -1
        else:
            print("Your choice does not match one of the options")




def main(amount: int, category: int ) -> None:
    question_pool = get_questions(amount, category)    
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
        choices = question["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffel_choice = shuffel_choices(choices)
        print(choices)
        user_choice_index = get_user_choice()
        user_choice_text = shuffel_choice[user_choice_index]
        correct_choice = html.unescape(question["correct_answer"])
        score = 0
        if user_choice_text == correct_choice:
            print("Correct!")
            score = score +1
        else:
            print(f"Sorry, the correct answer is: {correct_choice}")
    print(f"You scored: {score}  out of  {amount}")        

#call main
if __name__ == "__main__":

    amount = 10
    category = 11
    main(amount, category)                