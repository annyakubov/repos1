import random

# список слів для вибору
word_list = ["apple", "banana", "orange", "pear", "watermelon"]

# вибираємо випадкове слово зі списку
chosen_word = random.choice(word_list)

# робимо список з зірочками для кожної літери слова
hidden_word = list("*" * len(chosen_word))

# кількість спроб
num_guesses = int(input("Введіть кількість спроб: "))

# цикл для угадування слова
while num_guesses > 0:
    # виводимо на екран заховане слово
    print(" ".join(hidden_word))

    # запитуємо користувача наступну літеру або слово
    guess = input("Введіть літеру або слово: ").lower()

    # якщо користувач повторив слово, виводимо відповідне повідомлення
    if guess == chosen_word:
        print("Вітаю, ви вгадали слово!")
        break

    # якщо користувач ввів літеру
    elif len(guess) == 1:
        # перевіряємо чи ця літера є у слові
        if guess in chosen_word:
            # замінюємо всі зірочки на цю літеру в списку зі словом
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    hidden_word[i] = guess
            print("".join(hidden_word))
        else:
            print("Такої літери немає.")
            num_guesses -= 1

    # якщо користувач ввів більше однієї літери
    else:
        print("Введіть тільки одну літеру або всі слово.")
        num_guesses -= 1

    # перевіряємо, чи вгадано всі букви
    if "".join(hidden_word) == chosen_word:
        print("Вітаю, ви вгадали слово!")
        break

    # якщо спроб більше не залишилося, кінець гри
    if num_guesses == 0:
        print("На жаль, ви програли. Слово було", chosen_word)
