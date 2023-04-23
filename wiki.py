# Run it in terminal directly
import wikipedia

def search_wiki(query):
    try:
        return wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as e:
        return "Can you please clarify your question? It could mean several things. Here are some options: \n\n" + '\n'.join(e.options)
    except wikipedia.exceptions.PageError:
        return "I'm sorry, I couldn't find any information on that topic. Can you please try again with another query?"

while True:
    user_input = input("Ask me anything: ")
    if user_input.lower() == "exit":
        break
    else:
        response = search_wiki(user_input)
        print("Question: " + user_input)
        print("Answer: " + response)
        print("-------------------------------------------------------------------------------------------------------------------")
