import time

def starting_point():
    print("Hello Walter, glad to have you here, now enjoy this!")
    print("I've created clues for you.")
    print("I do enjoy my time with you, by the way. Now let's start!\n")

def display_clue(clue_num, clue_word):
    print(f"Clue {clue_num}: {clue_word}")
    time.sleep(2)

def get_answer(key):
    user_resp = input("Hey Walter, ¿sabes la respuesta? ❤️ : ").lower()
    return user_resp == key.lower()

def end_point():
    print("\n¡Congratulations! ¡Felicidades Amor!")
    print("Happy Valentine's Day! ❤️ Do you want to be mine forever? ;)")

def main():
    clues_responses = [
        ("When we first connected, what was the name of the app?", "hinge"),
        ("Our first kiss happened outside a restaurant. What is the name of the restaurant?", "southlake"),
        ("For our second date, we enjoyed Japanese food. Name the Japanese restaurant.", "coco coichibanya"),
        ("I have a special word for you. What is the word I always call you?", "crazy"),
    ]

    starting_point()

    for i, (clue, answer) in enumerate(clues_responses, start=1):
        display_clue(i, clue)

        while True:
            if get_answer(answer):
                print("¡Perfecto! We will continue. Ready???")
                time.sleep(1)
                break
            else:
                print("So close, but not quite.")

    print("\nLo último!")
    display_clue(len(clues_responses) + 1, "The hidden treasure is at ")
    end_point()

if __name__ == "__main__":
    main()
