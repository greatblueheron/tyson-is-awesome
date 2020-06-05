import sys
import getpass

# vigenere encrypt and decrypt code from
# https://code.sololearn.com/cUoAwxEFYsL3/#py


def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph


def encrypt_vigenere(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


def decrypt_vigenere(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += alph[new.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


def encrypt(key, message_to_encrypt, file_to_write_the_encrypted_version_to):
    # 1. load the text file into a string
    file_to_read = open(message_to_encrypt, 'r')
    read_in_text = file_to_read.read()

    # 1.5 copy the key a bunch of times so that it is as long as the text
    if len(key) <= len(read_in_text):
        big_key = key * (len(read_in_text) // len(key)) + key[:len(read_in_text) % len(key)]
    else:
        big_key = key

    # 2. encrypt it
    encrypted_version = encrypt_vigenere(text=read_in_text, big_key=big_key)

    # 3. write the encrypted version to disk
    file_to_write_to = open(file_to_write_the_encrypted_version_to, 'w')
    file_to_write_to.write(encrypted_version)
    file_to_write_to.close()

    return


def decrypt(key, message_to_decrypt, file_to_write_the_decrypted_version_to):
    # 1. load the text file into a string
    file_to_read = open(message_to_decrypt, 'r')
    read_in_text = file_to_read.read()

    # 1.5 copy the key a bunch of times so that it is as long as the text
    if len(key) <= len(read_in_text):
        big_key = key * (len(read_in_text) // len(key)) + key[:len(read_in_text) % len(key)]
    else:
        big_key = key

    # 2. decrypt it
    decrypted_version = decrypt_vigenere(text=read_in_text, big_key=big_key)

    # 3. write the decrypted version to disk
    file_to_write_to = open(file_to_write_the_decrypted_version_to, 'w')
    file_to_write_to.write(decrypted_version)
    file_to_write_to.close()

    return


def main():
    # command line should have three args;
    # either e message.txt scrambled or
    # d scrambled message.txt
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    first_argument = sys.argv[1]
    second_argument = sys.argv[2]
    third_argument = sys.argv[3]

    if len(sys.argv) != 4:
        print('Wrong number of arguments! Use either e message.txt scrambled or d scrambled message.txt')

    key = getpass.getpass()

    if first_argument == 'e':
        encrypt(key, second_argument, third_argument)

    if first_argument == 'd':
        decrypt(key, second_argument, third_argument)

    if first_argument not in ['e', 'd']:
        print('first argument has to be e or d')


if __name__ == "__main__":
    sys.exit(main())
