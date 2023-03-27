import openai
import PictureToLatex
import WolframAlphaSolver
import SearchRelatedVideos

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

def picturelatexsolver(question1):
    question = PictureToLatex.get_formula(question1)
    print("ADSSADASDASD")
    simplified_equation_question = "Turn this LaTeX equation into a equation: " + question + "Do not simplify the equation."
    simplified_question = (GPT_ask(simplified_equation_question)).choices[0].text
    print(simplified_question)
    video_link = GPT_ask("What concept of math is this using? " + question + " Only give the name of the concept. (Example: Quadratic Formula)")
    print("passed1")
    answer = WolframAlphaSolver.find_answer(simplified_question)
    print("passed2")

    response = GPT_ask("Given that the answer is "+ answer + ", explain how to solve "+ simplified_question)
    print("passed3")
    final_explain = response.choices[0].text


    # graph_form = GPT_ask("Convert this equation into matplotlib graph's y vector form (Example: 2x^2+3x+1 becomes 2*x**2+3*x+1)" + simplified_question)
    # graph_form = graph_form.choices[0].text
    # graph_form = graph_form.replace("\n", "")
    # PlotGraph.graph(graph_form)



    reccomendation = "\n\nFor more help on the concept, go check out these videos: " + SearchRelatedVideos.findYT(video_link.choices[0].text + " math tutorial")
    print("passed4")
    FinalResult = final_explain +reccomendation
    print(FinalResult)
    return FinalResult

def textlatexsolver(question1):
    question = question1
    simplified_equation_question = "Turn this question into an equation: " + question + "Do not simplify the equation."
    simplified_question = (GPT_ask(simplified_equation_question)).choices[0].text
    video_link = GPT_ask("What concept of math is this using? " + question + " Only give the name of the concept. (Example: Quadratic Formula)")

    answer = WolframAlphaSolver.find_answer(simplified_question)

    response = GPT_ask("Given that the answer is "+ answer + ", explain how to solve "+ simplified_question)
    final_explain = response.choices[0].text


    # graph_form = GPT_ask("Convert this equation into matplotlib graph's y vector form (Example: 2x^2+3x+1 becomes 2*x**2+3*x+1)" + simplified_question)
    # graph_form = graph_form.choices[0].text
    # graph_form = graph_form.replace("\n", "")
    # PlotGraph.graph(graph_form)



    reccomendation = "For more help on the concept, go check out these videos: " + SearchRelatedVideos.findYT(video_link.choices[0].text + " math tutorial")
    FinalResult = str(final_explain)  +  str(reccomendation)
    return FinalResult
