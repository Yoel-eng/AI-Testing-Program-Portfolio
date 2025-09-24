global alphabet

from dotenv import load_dotenv
from openai import OpenAI
import translator
import random
import string
import base64
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
Model = "gpt-4o-mini"
openai = OpenAI()


alphabet = list(string.ascii_letters + string.digits + string.punctuation + ' ')

def chatBot(questionAndAnswer):
    SystemMsg = "You are learnBot, a smart ai assistant that allows user to be smart, with a help request from the user, respond only in plaintext, you would help user get to the answer, don't ever give them the answer straight away(but once the user get to the correct answer, you can confirm that they got it correct and give summary on how to get the answer again). and answers were separated by '|',(compare the answer that the user had to the correct answer of the block) the question that you have now is: " + questionAndAnswer
    MessageBlock = [
        {"role": "system", "content": SystemMsg}
        ]
    while True:
        userInput = input("prompt(\"/bye\" to quit): ")
        if userInput == "/bye":
            break
        MessageBlock.append({'role': 'user', 'content': userInput})
        print("Please wait...\n")
        response = openai.chat.completions.create(
            model=Model,
            messages=MessageBlock
        )
        output = response.choices[0].message.content
        print(output)
        MessageBlock.append({'role': 'assistant', 'content': output})


class substitute:

    def __init__(self, key = "key"):
        # reason why it's enclosed in class, is because if you want to call it again,
        # so if you want to do multistep, you can use this.
        self.shuffled = alphabet.copy()
        self.rand = random.Random(key)
        self.rand.shuffle(self.shuffled)
    def encrypt(self, text):
        encrypted_text = [self.shuffled[alphabet.index(c)] for c in text]
        return ''.join(encrypted_text)
    def decrypt(self, text):
        encrypted_text = [alphabet[self.shuffled.index(c)] for c in text]
        return ''.join(encrypted_text)
        

class vigenere:
    def __init__(self, key = "key"):
        # creates a new "RNG" for the vigenere to work.
        self.rand = random.Random(key)
        # makes a copy of the alphabet 2 times to create a more secure table
        self.alphabet = alphabet.copy()
        self.rand.shuffle(self.alphabet)
        self.key = list(key)
    
    def encrypt(self, text):
        text = list(text)
        self.key = [self.key[i%len(self.key)] for i in range(len(text))]
        text = [self.alphabet[(self.alphabet.index(text[i]) + self.alphabet.index(self.key[i]))%len(self.alphabet)] for i in range(len(text))]
        return ''.join(text)
    
    def decrypt(self, text):
        text = list(text)
        self.key = [self.key[i%len(self.key)] for i in range(len(text))]
        text = [self.alphabet[(self.alphabet.index(text[i]) - self.alphabet.index(self.key[i]))%len(self.alphabet)] for i in range(len(text))]
        return ''.join(text)


def base64_translator(string, type="normal"):
    string = string.encode("ascii")
    if type == "normal":
        string = base64.b64encode(string)
    elif type == "reverse":
        string = string.decode("ascii")
        padding = len(string) % 4
        if padding != 0:
            string += "=" * (4 - padding)
        string = base64.b64decode(string)
    return string.decode("ascii")

def makeQuestions():
    print("\nfor the y/n question, say [y]if its spelled correctly \n[n]if it's wrong(you can redo the question/answer)\n\n" \
    "select [c] to make an answer correct and [w] to make it incorrect.\n")
    sectionList = []
    tempQuestion = ""
    tempAnswers = []
    finishMakingQuestions = False
    while not finishMakingQuestions:
        while True:
            userInput = input("\nPlease write down the question(please check for incorrect spelling)[type quit to exit making anymore questions]:\n").strip()
            # checks if the user quits and sets finishMakingQuestion variable to True, so that the parent loop and answer making loop stops.
            if userInput.lower() == 'quit':
                finishMakingQuestions = True
                break
            correctOrNo = input("y/n:")
            if correctOrNo.lower() == 'y':
                tempQuestion = userInput.lower()
                break
        while not finishMakingQuestions:
            userInput = input("Please write down the answer down below(type quit to exit this answer):\n").strip()
            if userInput == 'quit':
                sectionList.append([tempQuestion, tempAnswers.copy()])
                tempAnswers.clear()
                tempQuestion = ""
                break
            correctOrNo = input("y/n: ")
            if correctOrNo.lower() == 'y':
                temp = "false"
                correctOrWrong = input("c/w: ")
                if correctOrWrong == "c":
                    temp = "true"
                tempAnswers.append([userInput, temp])
    # I just reuse finishMakingQuestions to lower the amount of variables needed.
    modes = input("test or learn mode(t/l): ")
    sectionList.append('test' if modes.lower() == 't' else 'learn')
    return sectionList

def testOrLearnMode(sectionList):
    question = sectionList[:-1]
    mode = sectionList[-1]
    random.shuffle(question)
    for q in question:
        random.shuffle(q[1])
    allowChatBot = False
    correctAnswers = 0
    currentNumber = 1
    if mode == "test": 
        print("Test mode selected, write which answer (index of the number, starts from 1)")
    elif mode == "learn":
        print("Learn mode selected, ChatBot is allowed," \
        "write which answer (index of the number, starts from 1)")
        allowChatBot = True
    for q in question:
        print(f"{q[0]}")  # print the question
        for a in q[1]:
            print(f"- {a[0]}")
        answerIndex = int(input("Enter the index(-1 for chatbot): ")) - 1
        if allowChatBot and answerIndex <= -1:
            questionToPass = "question: " + q[0] + "| Answers: "
            for a in q[1]:
                questionToPass += a[0]
                questionToPass += "|"
            chatBot(questionToPass)
        else: 
            selectedAnswer = q[1][answerIndex]
            if selectedAnswer[1] == "true":
                correctAnswers += 1
            else:
                pass
    print(f"the {mode} mode has concluded, you gotten {correctAnswers} correct, out of {len(question)} ")
        
    

if __name__ == '__main__':
    # predefining encryption layers:

    print("Welcome to the testing program, before doing anything, when you want to do test or learn mode\n" \
    "please paste in the configuration in the configuration.txt, and save it, if you are making quesitons,\n" \
    "the program will reset the whole thing by itself.")

    userKey = input("Please put your key here(to encrypt/decrypt questions): ")
    configPath = os.path.abspath("configuration.txt")
    userKey = userKey.strip()
    substitute1 = substitute(userKey)
    substitute2 = substitute(userKey)
    substitute3 = substitute(userKey)
    vigenere1 = vigenere(userKey)
    vigenere2 = vigenere(userKey)
    vigenere3 = vigenere(userKey)
    running = True
    modes = "tlqe"
    # for program, not going to be used, used automatically
    def encrypt(stringToEncrypt):
        stringToEncrypt = substitute1.encrypt(stringToEncrypt)
        stringToEncrypt = vigenere1.encrypt(stringToEncrypt)
        stringToEncrypt = substitute2.encrypt(stringToEncrypt)
        stringToEncrypt = vigenere2.encrypt(stringToEncrypt)
        stringToEncrypt = substitute3.encrypt(stringToEncrypt)
        stringToEncrypt = vigenere3.encrypt(stringToEncrypt)
        stringToEncrypt = base64_translator(stringToEncrypt)
        return stringToEncrypt
    # this on the other hand, will be used extensively by user choices, basically to decrypt it
    # and send it to the translator program to make it a readable list for the program to process it
    def decrypt(encryptedString):
        encryptedString = base64_translator(encryptedString, "reverse")
        encryptedString = vigenere3.decrypt(encryptedString)
        encryptedString = substitute3.decrypt(encryptedString)
        encryptedString = vigenere2.decrypt(encryptedString)
        encryptedString = substitute2.decrypt(encryptedString)
        encryptedString = vigenere1.decrypt(encryptedString)
        encryptedString = substitute1.decrypt(encryptedString)
        return encryptedString
    while running:
        modeSelector = input("\nHello, welcome to the GHP Program, select modes:\n- t: test mode\n- l: learn mode\n- q: create question mode\n- e: exit program\n\ninput: ")
        if modeSelector.lower() in modes:
            if modeSelector.lower() == 't' or modeSelector.lower() == 'l':
                with open(configPath, "r") as reader:
                    configuration = reader.read().strip()
                if configuration != '':
                    configuration = translator.stringToList(decrypt(configuration))
                    if configuration == "|E8572.sdgfu8SD+,e3834W|":
                        print("Invalid key/configuration.")
                    elif type(configuration) == list:
                        testOrLearnMode(configuration)
                else:
                    print("No configuration found. Please paste in your config in configuration.txt or create questions!.")
            elif modeSelector.lower() == 'q':
                question = encrypt(translator.listToString(makeQuestions()))
                with open(configPath, "w") as edit:
                    edit.write(question)
                print("Please copy the content in the configuration file.")
            elif modeSelector.lower() == 'e':
                running = False
                print("Exitting Program...")
            else:
                print("Invalid option, please select from the list.\n")
