
# question 1
def encrypt_caesar_cipher(plaintext : str, key: int) -> str:
    ciphertext = list(plaintext)
    for i in range(0,len(ciphertext)):
        ciphertext[i] = chr(((ord(ciphertext[i])-65+key) % 26) + 65)
    ciphertext_str = ''.join(ciphertext)
    # print(ciphertext_str)
    return ciphertext_str

def decrypt_caesar_cipher(ciphertext : str, key: int) -> str:
    plaintext = list(ciphertext)
    for i in range(0,len(plaintext)):
        plaintext[i] = chr(((ord(plaintext[i])-65-key) % 26) + 65)
    plaintext_str = ''.join(plaintext)
    # print(plaintext_str)
    return plaintext_str

def bruteforce_caesar_cipher(ciphertext : str):
    plaintext_str = ""
    # check all the keys
    for key in range(0,26):

        # decrypt
        plaintext_str = decrypt_caesar_cipher(ciphertext, key)

        # print the key and plaintext
        print(f'{key}: {plaintext_str}')
        
def en_decrypt_caesar(plaintext : str, key : int):
    print(f"Plaintext:\t\t {plaintext}")
    cipher = encrypt_caesar_cipher(plaintext, key)
    print(f"Ciphertext:\t\t {cipher}")
    res = decrypt_caesar_cipher(cipher, key)
    print(f"Back to Plaintext:\t {res}")

# end question 1
# question 2
class g:
    subtable = {
        'A' : '$',
        'B' : '@',
        'C' : '!',
        'D' : '~',
        'E' : '9',
        'F' : '2',
        'G' : '4',
        'H' : '1',
        'I' : '&',
        'J' : '^',
        'K' : '%',
        'L' : '{',
        'M' : '}',
        'N' : '|',
        'O' : ':',
        'P' : '>',
        'Q' : '<',
        'R' : '/',
        'S' : '?',
        'T' : '*',
        'U' : '7',
        'V' : '6',
        'W' : '5',
        'X' : '3',
        'Y' : '0',
        'Z' : 'A', 
    }

def encrypt_random(plaintext : str) -> str:
    ciphertext_list = list(plaintext)
    for i in range(0, len(ciphertext_list)):
        ciphertext_list[i] = g.subtable.get(ciphertext_list[i])
    return ''.join(ciphertext_list)
    
def decrypt_random(ciphertext : str) -> str:
    plaintext_list = list(ciphertext)
    for i in range(0, len(plaintext_list)):
        plaintext_list[i] = [k for k, value in g.subtable.items() if value == plaintext_list[i]][0]
    return ''.join(plaintext_list)

def en_decrypt_random(plaintext : str):
    print(f"Plaintext: {plaintext}")
    cipher = encrypt_random(plaintext)
    print(f"Ciphertext: {cipher}")
    res = decrypt_random(cipher)
    print(f"Back to Plaintext: {res}")


# MAIN FUNCTION
def main():
    # question 1 
    print("Question 1a:")
    en_decrypt_caesar("SSOEATBENEDUMHALLOHARASTREET", 5)
    # cipher = XXTJFYGJSJIZRMFQQTMFWFXYWJJY
    
    print("")
    print("Question 1b")
    bruteforce_caesar_cipher("WPXAIDEXII")   
    # key = 15  
    # plaintext = HAILTOPITT

    print("")
    print("Checking answer for 1b")
    en_decrypt_caesar("HAILTOPITT", 15)

    # question 2
    print("")
    print("Question 2")
    en_decrypt_random("PITTSBURGH")


    
if __name__ == "__main__":
    main()