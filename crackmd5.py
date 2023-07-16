#Importing relevant modules
import hashlib
import argparse

#Creating Parser
parser = argparse.ArgumentParser(description="MD5 Cracker")

#Adding arguements
parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)
parser.add_argument("-w", dest="wordlist",help="wordlist", required=True)

#Parsing the arguement
args_ = parser.parse_args()


#Creating the main function

def main():
    crackedhash_ = ""
    with open(args_.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == args_.hash:
                crackedhash_ = line
                print("\n Hash has been cracked.The plaintext value is: %s." %line)
    if crackedhash_ == "":
        print("Oops, it failed. Try using a larger list :) ")

if __name__ == "__main__":
    main()