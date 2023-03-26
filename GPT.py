import openai
import PictureToLatex
import WolframAlphaSolver

openai.api_key = "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"

def GPT_ask(GPTquestion):
    response = openai.Completion.create(
    model = "text-davinci-003",
    prompt=GPTquestion,
    temperature=0.2,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    )
    return response

try:
    question = PictureToLatex.get_formula('test.png')
except:
    question = input("Please enter your question: ")

simplify = "Turn this LaTeX equation into a equation: " + question

question = (GPT_ask(simplify)).choices[0].text

print(question) 

answer = WolframAlphaSolver.find_answer("Factor for x" + question)

print(answer)

response = GPT_ask("Given that the answer is "+ answer + ", explain how to solve "+ question)
final_explain = response.choices[0].text

print(final_explain)