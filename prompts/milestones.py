import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def milestones_model(input):
    response = openai.Completion.create(
        model = "text-davinci-002",
        prompt = "The following text is meant to describe the milestones of a team that is working to build a product. Score the text from 1-100 on how clear and realistic the milestones may be. After providing a score, write a few sentences explaining why this score was given. \n\ {}".format(input),
        temperature = 0.2,
        max_tokens = 512,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return response["choices"][0]["text"]
 
"""
for internal testing

test_input = ""
print(milestones(test_input))
"""