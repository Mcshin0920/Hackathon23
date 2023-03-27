# importing the wolframalpha module
import wolframalpha

# defining a function to find answer
def find_answer(question):

    # declaring a variable to store the APP ID
    app_id = 'X9U37K-669LUEXRYH'

    # creating an object of the Client() class using the APP ID
    the_client = wolframalpha.Client(app_id)

    # storing the responses from wolfram alpha
    response = the_client.query(question)

    # including only the text from the responses
    answer = next(response.results).text

    # returning the answer
    return answer