import random
words = [
    {"spanish": "el", "english": "the (masculine)"},
    {"spanish": "la", "english": "the (feminine)"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": ["that/which"]},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": ["in/on"]},
    {"spanish": "un", "english": ["a/an (masculine)"]},
    {"spanish": "una", "english": ["a/an (feminine)"]},
    {"spanish": "es", "english": "is (he/she/it)"},
    {"spanish": "no", "english": "no"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "por", "english": ["by/for"]},
    {"spanish": "con", "english": "with"},
    {"spanish": "para", "english": ["for/to"]},
    {"spanish": "como", "english": ["like/as"]},
    {"spanish": "yo", "english": "I"},
    {"spanish": "tú", "english": "you (informal singular)"},
    {"spanish": "él", "english": "he"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "nosotros", "english": "we (masculine/mixed)"},
    {"spanish": "nosotras", "english": "we (feminine)"},
    {"spanish": "vosotros", "english": "you all (informal masculine/mixed, Spain)"},
    {"spanish": "vosotras", "english": "you all (informal feminine, Spain)"},
    {"spanish": "ellos", "english": "they (masculine/mixed)"},
    {"spanish": "ellas", "english": "they (feminine)"},
    {"spanish": "usted", "english": "you (formal singular)"},
    {"spanish": "ustedes", "english": "you all (formal/informal in Latin America)"},
    {"spanish": "ser", "english": "to be (essential)"},
    {"spanish": "estar", "english": "to be (state/location)"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "hacer", "english": ["to do/make"]},
    {"spanish": "poder", "english": ["to be able to/can"]},
    {"spanish": "decir", "english": "to say"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "saber", "english": "to know (information)"},
    {"spanish": "querer", "english": ["to want/love"]},
    {"spanish": "llegar", "english": "to arrive"},
    {"spanish": "pasar", "english": ["to pass/happen"]},
    {"spanish": "deber", "english": ["should/must"]},
    {"spanish": "poner", "english": ["to put/place"]},
    {"spanish": "parecer", "english": "to seem"},
    {"spanish": "quedar", "english": ["to stay/remain"]},
    {"spanish": "creer", "english": "to believe"},
    {"spanish": "hablar", "english": "to speak"},
    {"spanish": "llevar", "english": ["to carry/take"]},
    {"spanish": "dejar", "english": "to leave (something)"},
    {"spanish": "seguir", "english": ["to follow/continue"]},
    {"spanish": "encontrar", "english": "to find"},
    {"spanish": "llamar", "english": "to call"},
    {"spanish": "venir", "english": "to come"},
    {"spanish": "pensar", "english": "to think"},
    {"spanish": "salir", "english": "to leave"},
    {"spanish": "volver", "english": "to return"},
    {"spanish": "tomar", "english": "to take"},
    {"spanish": "conocer", "english": "to know (someone)"},
    {"spanish": "vivir", "english": "to live"},
    {"spanish": "sentir", "english": "to feel"},
    {"spanish": "trabajar", "english": "to work"},
    {"spanish": "escribir", "english": "to write"},
    {"spanish": "leer", "english": "to read"},
    {"spanish": "comer", "english": "to eat"},
    {"spanish": "abrir", "english": "to open"},
    {"spanish": "jugar", "english": "to play"},
    {"spanish": "entender", "english": "to understand"},
    {"spanish": "pedir", "english": "to ask for"},
    {"spanish": "necesitar", "english": "to need"},
    {"spanish": "esperar", "english": ["to wait/hope"]},
    {"spanish": "usar", "english": "to use"},
    {"spanish": "pagar", "english": "to pay"},
    {"spanish": "cambiar", "english": "to change"},
    {"spanish": "mirar", "english": ["to watch/look at"]},
    {"spanish": "ayudar", "english": "to help"},
    {"spanish": "empezar", "english": ["to begin/start"]},
    {"spanish": "caminar", "english": "to walk"},
    {"spanish": "comprar", "english": "to buy"},
    {"spanish": "estudiar", "english": "to study"},
    {"spanish": "gustar", "english": "to like"},
    {"spanish": "abrir", "english": "to open"},
    {"spanish": "viajar", "english": "to travel"},
    {"spanish": "enseñar", "english": "to teach"},
    {"spanish": "recibir", "english": "to receive"},
    {"spanish": "bailar", "english": "to dance"},
    {"spanish": "correr", "english": "to run"},
    {"spanish": "vender", "english": "to sell"},
    {"spanish": "beber", "english": "to drink"},
    {"spanish": "llegar", "english": "to arrive"},
    {"spanish": "llevar", "english": "to wear"},
    {"spanish": "dormir", "english": "to sleep"},
    {"spanish": "pensar", "english": "to think"},
    {"spanish": "andar", "english": "to walk"},
    {"spanish": "perder", "english": "to lose"},
    {"spanish": "ganar", "english": "to win"},
    {"spanish": "buscar", "english": ["to search/look for"]}

]

def quiz_user(words):
    random.shuffle(words)
    score = 0 

    for word in words:
        print(f"What is the english translation of '{word['spanish']}?")
        user_answer = input("Your Answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'. \n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")
        


def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)


if __name__ == "__main__":
    main()  
    