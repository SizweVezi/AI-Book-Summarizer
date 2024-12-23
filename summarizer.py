import os
from openai import OpenAI, completions, models
import prompts
from dotenv import load_dotenv, find_dotenv
import PyPDF2

from prompts import system_message

#Integrate OpenAI API
_= load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
topic = ""

#OpenAI Configurations

model = "gpt-4o-mini"
temperature = 0.3
max_completion_tokens = 1000

#Open the file to summarize
book = ""
file_path = "AI-Crypto-Exploring-Use-Cases-and-Possibilities.pdf"
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 4
    end_page = total_pages - 9

    for page_number in range(start_page, end_page):
        page = reader.pages[page_number]
        book += page.extract_text() + " "

#Intergrate the ChatGPT Logic
#1. Prompts
system_message = prompts.system_message
user_prompt = prompts.generate_prompt(book,topic)

#2. Messages
messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]

#3 Summary from the gpt model
def get_summary():
    completion = client.chat.completions.create(
    messages = messages,
    model = model,
    temperature = temperature,
    max_completion_tokens = max_completion_tokens

)
    return completion.choices[0].message.content

print(get_summary())






































"""
import os
#import reader
import PyPDF2
from openai import OpenAI, models, completions
from dotenv import load_dotenv, find_dotenv
import prompts
import dotenv
from prompts import system_message


#initiate the env variables.
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)
print(os.environ.get("OPENAI_API_KEY"))
#book to summarize

#OpenAI API configurations
model = "gpt-4o-mini-2024-07-18"
temperature = 0.3
max_completion_tokens = 2000
topic = "What are the different use cases"

#open and reading the book
book = ""
path_to_file = "2023-04-29-Adan-Regulating-DeFi-in-Europe-issues-for-consideration-mini (1).pdf"
with open(path_to_file, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 5
    end_page = total_pages - 3

    for page_number in range(start_page, end_page):
        page = reader.pages[page_number]
        book += page.extract_text() + " "

#prompts
system_message = prompts.system_message
prompts = prompts.generate_prompt(book,topic)

#messages
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompts}
]

def get_summary():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_completion_tokens
    )
    return completion.choices[0].message.content

print(get_summary())
"""
