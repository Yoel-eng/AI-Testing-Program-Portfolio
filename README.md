# AI-Testing-Program
This program powered with Python and OpenAI GPT infrastructure, key features:
- test mode
- learn mode(allows you to talk with AI Chatbots to get to the correct answer)
- question maker mode(combined with encryption method and base64 encoding to save the configuration and be able to be used later)

resources used:
- https://www.youtube.com/watch?v=0eCMCk9Bstw&t=502s
- https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/?ranMID=39197&ranEAID=%2FjZHTpnCvx8&ranSiteID=_jZHTpnCvx8-HuW5j2CqBP7LDpY76KBPyA&utm_source=aff-campaign&LSNPUBID=%2FjZHTpnCvx8&utm_medium=udemyads&couponCode=MT250923G3
- https://www.youtube.com/watch?v=Jo_ifPc1TnY&t=336s (primarily used to make my older ecnryption algorithm program to be more efficient)

Prerequisites:
- python 3.13 (can be downloaded from Microsoft Store)
- pip installer

Preparation of use:
- create a virtual environment inside the folder https://www.youtube.com/watch?v=JYdd1k44FRM
  > python3 -m venv venv
- remove the execution policy to unrestricted to allow enter the virtual env
  > Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
- Then this to activate the virtual environment:
  > venv\Scripts\Activate
- Then install the dependencies
  > pip install -r requirements.txt
- run the program by running this command:
  > & .\venv\Scripts\python.exe0 .\main.py

how to use:
- everytime, starting a new one, don't forget to activate the virtual environment, then run the main.py
- in the start, you'd have to create quesiton first, or paste configuration given by your teacher/friend into configuration.txt, don't put any 2nd line, paste it, save it, close it.
- The program starts with main.py (& .\venv\Scripts\python.exe0 .\main.py)
- Program starts with asking the user for the encryption key, this will be used for both question maker mode and the test/learn mode.
- if you have not pasted any configuration given by a teacher in configuration.txt, and want to create question, select for question maker mode
question maker mode allows the user to create questions, and after doing all of these, the question will be made into encrypted format in configuration.txt, in which users will share, program will not work if the key that has been set by students in the beginning doesn't matching to the same key that the maker of the question set.
- test and learn mode were 2 same things, the difference is that Learn mode allows you to use a chatbot, powered with OpenAI's frontier models(specifically GPT-4o mini)
- additional instructions on operating the program will be printed out during the use of the program.
