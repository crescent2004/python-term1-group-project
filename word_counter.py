def word_counter():
    print("\n--- WORD COUNTER ---")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("No input provided!")
        return

    words = sentence.split()
    char_count = len(sentence.replace(" ", ""))
    longest_word = max(words, key=len)

    print("\nResults:")
    print(f"Number of words: {len(words)}")
    print(f"Number of characters (no spaces): {char_count}")
    print(f"Longest word: {longest_word}")


word_counter()
