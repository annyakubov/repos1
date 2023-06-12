import random

# список можливих слів
words = ["apple", "banana", "cherry", "orange", "lemon", "pear", "kiwi", "mango", "pineapple", "watermelon"]

# вибір випадкового слова зі списку та ініціалізація змінних
chosen_word = random.choice(words)
word_length = len(chosen_word)
attempts = 10
used_letters = []
hidden_word = ["*" for _ in range(word_length)]

# друк слова зірочками на початку гри
output = " ".join(hidden_word)
print(output)

# головний цикл гри
while True:
    print("Залишилось спроб:", attempts)
    user_input = input("Введіть літеру або слово: ").lower()

    # перевірка чи користувач ввів вже відгадане слово
    if user_input == chosen_word:
        print("Вітаю, ви вгадали слово")
        break
    elif len(user_input) > 1:
        print("Це не вірне слово")
        attempts -= 1
    else:
        letter = user_input
        # перевірка чи введена літера вже була використана
        if letter in used_letters:
            print("Ви вже вводили цю літеру, спробуйте ще")
            continue

        used_letters.append(letter)

        # перевірка чи введена літера є в слові
        if letter in chosen_word:
            print("Так, ця літера є в слові")
            for index, char in enumerate(chosen_word):
                if char == letter:
                    hidden_word[index] = letter

            # перевірка чи всі літери відгадані
            if "*" not in hidden_word:
                print("Вітаю, ви вгадали слово")
                break
        else:
            print("На жаль, цієї літери немає в слові")
            attempts -= 1

        # перевизначення значення для друку
        output = "".join(hidden_word)

        # перевірка чи залишились спроби
        if attempts == 0:
            print("Ви програли. Загадане слово було:", chosen_word)
            break

    # друк прихованого слова
    print(output)