# import time

# def typing_test(user_input):
#     prompt_text = "The quick brown fox jumps over the lazy dog."

#     start_time = time.time()

#     # Calculate words per minute (WPM) and accuracy
#     prompt_words = prompt_text.split()
#     user_words = user_input.split()

#     correct_words = sum(w1 == w2 for w1, w2 in zip(prompt_words, user_words))
#     accuracy = (correct_words / len(prompt_words)) * 100

#     elapsed_time = time.time() - start_time

#     # Check if elapsed_time is zero to avoid ZeroDivisionError
#     if elapsed_time == 0:
#         words_per_minute = 0
#     else:
#         words_per_minute = (len(user_words) / elapsed_time) * 60 * 60

#     return words_per_minute, accuracy


import time

def typing_test(user_input):
    prompt_text = "The quick brown fox jumps over the lazy dog."

    start_time = time.perf_counter()

    # Calculate words per minute and accuracy
    prompt_words = prompt_text.split()
    user_words = user_input.split()

    # Ensure that the number of words in user input does not exceed the number of words in the prompt
    user_words = user_words[:len(prompt_words)]

    correct_words = sum(w1 == w2 for w1, w2 in zip(prompt_words, user_words))
    accuracy = (correct_words / len(prompt_words)) * 100

    elapsed_time = time.perf_counter() - start_time

    # Check if elapsed_time is zero to avoid ZeroDivisionError
    if elapsed_time == 0:
        words_per_minute = 0
    else:
        words_per_minute = (len(user_words) / elapsed_time) * 60 

    # Print statements for debugging
    print("Prompt words:", prompt_words)
    print("User words:", user_words)
    print("Correct words:", correct_words)
    print("Accuracy:", accuracy)
    print("Elapsed time:", elapsed_time)
    print("Words per minute:", words_per_minute)

    return words_per_minute, accuracy
