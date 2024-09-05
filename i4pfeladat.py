import os
alfabet = "abcdefghijklmnopqrstuvwxyz "
def rejtjelez(uzenet, kulcs):
    alfabet = "abcdefghijklmnopqrstuvwxyz "
    rejtejelezett_uzenet = ""

    for i in range(len(uzenet)):
        uzenet_index = alfabet.index(uzenet[i])
        kulcs_index = alfabet.index(kulcs[i % len(kulcs)])
        rejtjelezett_index = (uzenet_index + kulcs_index) % 27
        rejtejelezett_uzenet += alfabet[rejtjelezett_index]

    return rejtejelezett_uzenet

uzenet="helloworld"
kulcs="abcdefgijkl"
result=rejtjelez(uzenet, kulcs)
print(result)

def visszafejtes(rejtejelezett_uzenet, kulcs):
    alfabet = "abcdefghijklmnopqrstuvwxyz "
    visszafejtett_uzenet = ""

    for i in range(len(rejtejelezett_uzenet)):
        rejtjelezett_index = alfabet.index(rejtejelezett_uzenet[i])
        kulcs_index = alfabet.index(kulcs[i % len(kulcs)])
        visszafejtett_index = (rejtjelezett_index - kulcs_index) % 27
        visszafejtett_uzenet += alfabet[visszafejtett_index]

    return visszafejtett_uzenet

#példa
uzenet = "early"
kulcs = "abcdefgijklmnopqrstuvwxyz "
rejtejelezett = rejtjelez(uzenet, kulcs)
print(rejtejelezett)  
visszafejtett = visszafejtes(rejtejelezett, kulcs)
print(visszafejtett)  


class VigenereCracker:
    
    def __init__(self, ciphertext1, ciphertext2, file_path):
        self.ciphertext1 = self.filter_text(ciphertext1)
        self.ciphertext2 = self.filter_text(ciphertext2)
        self.size = min(len(self.ciphertext1), len(self.ciphertext2))
        self.words = []
        self.keys1 = []
        self.keys2 = []
        self.candidate_keys = []

        print(f"Ciphertext 1: {self.ciphertext1}")
        print(f"Ciphertext 2: {self.ciphertext2}")

        if self.size <= 0:
            raise ValueError("Invalid ciphertext")


        self.set_words(file_path)
        self.find_possible_keys(self.ciphertext1, self.keys1)
        self.find_possible_keys(self.ciphertext2, self.keys2)
        self.find_matching_keys()
        self.decrypt_ciphertext()

    def filter_text(self, text):
        return ''.join(c for c in text if c.isalpha() or c.isspace()).upper()

    def set_words(self, file_path):
        if not os.path.isfile(file_path):
            print("File not found.")
            return

        with open("/Users/gerolevente/Documents/wordlist.txt", 'r') as file:
            for line in file:
                word = self.filter_text(line.strip())
                if len(word) >= self.size:
                    self.words.append(word)

        if self.words:
            print("Added list of words")
        else:
            print("No words found")

    def find_possible_keys(self, ciphertext, keys):
        for word in self.words:
            key = ''
            for j in range(self.size):
                if j==" ":
                    None
                else:
                    difference = (ord(ciphertext[j]) - ord(word[j])) % 26
                    key += chr(difference + 65)
            keys.append(key)

        if keys:
            print(f"Created list of possible keys for ciphertext {'1' if keys is self.keys1 else '2'}")
        else:
            print("No keys found")

    def find_matching_keys(self):
        matching_keys = set(self.keys1) & set(self.keys2)
        self.candidate_keys = list(matching_keys)

        if self.candidate_keys:
            if len(self.candidate_keys) > 1:
                print(f"\nMultiple matches for key found: {self.candidate_keys}")
            else:
                print(f"Key found: {self.candidate_keys[0]}")
        else:
            print("No matching keys")

    def decrypt_ciphertext(self):
        if self.candidate_keys:
            for key in self.candidate_keys:
                print(f"\nDecryption for key: {key}")

                for idx, ciphertext in enumerate([self.ciphertext1, self.ciphertext2]):
                    plaintext = ''
                    for j in range(self.size):
                        difference = (ord(ciphertext[j]) - ord(key[j])) % 26
                        plaintext += chr(difference + 65)

                    plaintext_print = plaintext + '?' * (len(ciphertext) - self.size)
                    print(f"Plaintext {idx + 1}: {plaintext_print}")

                    possible_matches = [word for word in self.words if word.startswith(plaintext)]
                    if len(possible_matches) == 1 and possible_matches[0] != plaintext:
                        plaintext = possible_matches[0]
                        print(f"Likely match: {plaintext}")
                    elif len(possible_matches) > 1 and plaintext not in possible_matches:
                        print(f"Closest matches: {possible_matches}")

        else:
            raise Exception("Cannot decrypt ciphertext as key not found")
        
        



if __name__ == "__main__":
    cracker = VigenereCracker(rejtjelez("curiosity",kulcs), rejtjelez("data",kulcs), "/Users/gerolevente/Documents/wordlist.txt")


if __name__ == "__main__":
    cracker = VigenereCracker(rejtjelez("danger",kulcs), rejtjelez("daughter",kulcs), "/Users/gerolevente/Documents/wordlist.txt")

if __name__ == "__main__":
    cracker = VigenereCracker(rejtjelez("customer",kulcs), rejtjelez("explain",kulcs), "/Users/gerolevente/Documents/wordlist.txt")


    