import random

def guess_the_number():
    print("Witaj w grze 'Guess the Number'!")
    print("Komputer wylosuje liczbę od 1 do 100, a Ty musisz ją odgadnąć.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            player_guess = int(input("Podaj swoją liczbę: "))
            attempts += 1
            
            if player_guess < number_to_guess:
                print("Za mało! Spróbuj jeszcze raz.")
            elif player_guess > number_to_guess:
                print("Za dużo! Spróbuj jeszcze raz.")
            else:
                print(f"Gratulacje! Odgadłeś liczbę {number_to_guess} w {attempts} próbach.")
                guessed = True
        except ValueError:
            print("Proszę podać prawidłową liczbę.")
            
if __name__ == "__main__":
    guess_the_number()
