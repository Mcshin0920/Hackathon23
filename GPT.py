import openai
import PictureToLatex
import WolframAlphaSolver
import SearchRelatedVideos
import matplotlib.pyplot as plt
import numpy as np

openai.api_key = "discord"

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
    simplified_equation_question = "Turn this LaTeX equation into a equation: " + question + "Do not simplify the equation."
    simplified_question = (GPT_ask(simplified_equation_question)).choices[0].text
except:
    question = input("Please enter your question: ")
    simplified_equation_question = "Turn this question into an equation: " + question + "Do not simplify the equation."
    simplified_question = (GPT_ask(simplified_equation_question)).choices[0].text

video_link = GPT_ask("What concept of math is this using? " + question + " Only give the name of the concept. (Example: Quadratic Formula)")

answer = WolframAlphaSolver.find_answer(simplified_question)

response = GPT_ask("Given that the answer is "+ answer + ", explain how to solve "+ simplified_question)
final_explain = response.choices[0].text


graph_form = GPT_ask("Convert this equation into matplotlib graph's y vector form (Example: 2x^2+3x+1 becomes 2*x**2+3*x+1)" + simplified_question)
graph_form = graph_form.choices[0].text
graph_form = graph_form.replace("\n", "")
graph_form = graph_form.replace("x", "%s")

x = np.linspace(-10, 10, 100)
y = graph_form % x
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)

# Save the plot
plt.savefig('myplot.png')


print(final_explain)
print("For more help on the concept, go check out these videos: " + SearchRelatedVideos.findYT(video_link.choices[0].text + " math tutorial"))