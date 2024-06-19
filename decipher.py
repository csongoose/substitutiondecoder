def displayMsg(ciphered, deciphered, starred):
    print('Original text:')
    print(ciphered)
    print('\nDeciphered text:')
    print(deciphered)
    print('\nStarred text:')
    print(starred)


def decipher(filename_to_be_deciphered, deciphered_filename):
    with open(filename_to_be_deciphered, 'r') as f:
        encrypted_text = f.read()

    char_mapping = {}

    while True:

        deciphered_text = ''.join(
            idx if idx not in char_mapping else char_mapping[idx] for idx in encrypted_text.lower()
        )

        starred_text = ''.join(
            char_mapping[idx] if idx in char_mapping else '*' if idx.isalpha() else idx
            for idx in encrypted_text.lower())

        displayMsg(encrypted_text, deciphered_text, starred_text)

        userinput = input('\n Enter a substitution pair in format a=b, or type exit to exit').strip()

        if userinput.lower() == 'exit':
            break

        try:
            sub_pair = userinput.split('=')
            cyphered_char, deciphered_char = sub_pair[0].strip(), sub_pair[1].strip()
            char_mapping[cyphered_char] = deciphered_char
        except (ValueError, IndexError):
            print("Invalid input.")

    with open(deciphered_filename, 'w') as f:
        f.write(deciphered_text)

    print('Deciphered file saved as:' + deciphered_filename)

    return 0
