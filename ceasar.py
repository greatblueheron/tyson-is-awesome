import sys


def encrypt_some_string(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr(ord(char)+s)

    return result


def encrypt(message_to_encrypt, file_to_write_the_encrypted_version_to):
    # 1. load the text file into a string
    file_to_read = open(message_to_encrypt, 'r')
    read_in_text = file_to_read.read()

    # 2. encrypt it
    encrypted_version = encrypt_some_string(text=read_in_text, s=5)

    # 3. write the encrypted version to disk
    file_to_write_to = open(file_to_write_the_encrypted_version_to, 'w')
    file_to_write_to.write(encrypted_version)
    file_to_write_to.close()

    return


def decrypt(message_to_decrypt, file_to_write_the_decrypted_version_to):
    # 1. load the text file into a string
    file_to_read = open(message_to_decrypt, 'r')
    read_in_text = file_to_read.read()

    # 2. decrypt it
    decrypted_version = encrypt_some_string(text=read_in_text, s=-5)

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

    if first_argument == 'e':
        encrypt(second_argument, third_argument)

    if first_argument == 'd':
        decrypt(second_argument, third_argument)

    if first_argument not in ['e', 'd']:
        print('first argument has to be e or d')


if __name__ == "__main__":
    sys.exit(main())
