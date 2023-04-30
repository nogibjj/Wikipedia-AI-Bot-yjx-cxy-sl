# Final Project: Wikipedia AI Bot
### [*Option B: Pick Project from Practical MLOPs Book-Appendix E. Building a Technical Portfolio for MLOps*] (https://www.oreilly.com/library/view/practical-mlops/9781098103002/app05.html#idm45917434442872)

## Goals
We aim to create a Wikipedia AI bot that performs four main functions: wiki.py, search.py, chat.py, and app.py. These functions are designed to provide users with a seamless experience in accessing information from Wikipedia.

The first function, wiki.py, allows users to access information directly from the terminal. It presents information in an interactive manner, displaying paragraphs of text to provide a summary of the requested topic.

The second function, search.py, is focused on helping users quickly search for the main summary of a particular concept or definition. It is designed to simplify the search process by presenting only the most relevant information.

The third function, chat.py, aims to function as a chatbot that communicates with users via messages. It is designed to provide more detailed information on a given topic within 1-3 paragraphs, responding to users in a conversational manner.

Finally, app.py is designed for more accurate filtering, such as by date, location, category, and language. This allows users to find more specific information that meets their needs. Once filtered, the bot will present the relevant Wikipedia page directly to the user.

We believe that our Wikipedia AI bot will provide users with a seamless experience in accessing information from Wikipedia, making it easier and more efficient for them to learn and discover new things.

## Diagram
<img width="539" alt="Screen Shot 2023-04-23 at 8 53 09 PM" src="https://user-images.githubusercontent.com/112274822/233877015-96ecb553-20fd-4b4d-8ffe-55debf3e5b83.png">

## Demo Link


## How to Use
1. Save each file to a directory on your computer. You can save them to the same directory or to different directories, depending on your preference.

2. Open a command prompt or terminal window and navigate to the directory where you saved the files using the cd command. For example, if you saved the files to a directory called "wiki-bot" on your desktop, you could navigate to that directory using the command cd ~/Desktop/wiki-bot on a Mac/Linux or cd C:\Users\YourUserName\Desktop\wiki-bot on Windows.

3. Install the required Python modules. The four Python files require different modules, so you will need to install them separately. You can install the required modules using the following commands:

```
pip install wikipedia
pip install Flask requests
pip install Flask wikipedia
pip install Flask requests
```

4. Run the Python files. You can run each Python file by typing python filename.py in the command prompt or terminal window. For example, to run wiki.py, you would type python wiki.py and press Enter. This will start the program, and you will be prompted to enter a search query.

55. Follow the instructions for each program. Each program has its own interface and set of instructions, so follow the prompts and enter the required information. If you encounter any errors or issues, refer to the error messages or consult the documentation for the program.

6. To exit a program, enter the appropriate command. For example, in wiki.py, you can type "exit" to exit the program, and in the Flask applications (app.py, chat.py, and search.py), you can close the web browser or press Ctrl+C in the terminal window to stop the program.

<img width="859" alt="Screen Shot 2023-04-23 at 7 48 58 PM" src="https://user-images.githubusercontent.com/112274822/233873998-0bb48a06-2bc3-4085-bfc7-7511c06ed345.png">

## Methods and Results
### Simple Wiki functions 
#### **wiki.py**

This code defines a function named search_wiki that searches Wikipedia for a given query and returns a summary of the relevant article. The function includes some error handling to deal with situations where the query is ambiguous or no page is found.

The code then enters a loop that repeatedly prompts the user for input, calls search_wiki with the input as an argument, and prints the question and response. The loop continues until the user enters the string "exit", at which point the loop terminates and the program ends.

To run the code, save it to a Python file (e.g. "wiki_search.py") and run it in the terminal by navigating to the directory containing the file and typing "python wiki_search.py" (without quotes) and then press enter. The program will begin running and prompt the user for input.

<img width="1013" alt="Screen Shot 2023-04-23 at 7 48 01 PM" src="https://user-images.githubusercontent.com/112274822/233873972-42810f3c-1ebd-4237-a62a-931fb41f1813.png">
<img width="1016" alt="Screen Shot 2023-04-23 at 7 48 17 PM" src="https://user-images.githubusercontent.com/112274822/233873983-f4cf6373-79c6-40ff-b5de-076561e36604.png">

### Wikipedia SmartBot
**app.py**

This code defines a Flask web application that searches Wikipedia for articles based on user input. The application has a form with several fields, including a search query, start and end dates, a category, a location, and a language. When the form is submitted, the application constructs a URL for the Wikipedia API based on the form fields and sends a GET request to that URL. It then processes the response to extract the search results and displays them on a web page.

The index() function is the main view function for the application. It handles both GET and POST requests to the root URL ("/") and renders an HTML template called "index.html". If the request is a POST request (i.e. the user has submitted the form), the function extracts the form data from the request object and constructs a URL for the Wikipedia API based on the form data. It then sends a GET request to that URL using the requests module and processes the response to extract the search results. If the response is successful and contains search results, the function renders the "index.html" template with the search results and the original query. If the response is not successful or does not contain search results, the function renders the "index.html" template with an error message.

To run the code, save it to a Python file (e.g. "wiki_search_app.py") and run it in the terminal by navigating to the directory containing the file and typing "python wiki_search_app.py" (without quotes) and then press enter. The application will start running and can be accessed in a web browser at "http://localhost:5000/".

<img width="1214" alt="Screen Shot 2023-04-23 at 7 52 54 PM" src="https://user-images.githubusercontent.com/112274822/233873890-1b922ebe-b544-487a-8db5-04079ee8b990.png">
<img width="738" alt="Screen Shot 2023-04-23 at 7 53 02 PM" src="https://user-images.githubusercontent.com/112274822/233873894-b8754743-78d8-4d53-9b5b-12fbae6ef4a5.png">
<img width="1290" alt="Screen Shot 2023-04-23 at 7 53 30 PM" src="https://user-images.githubusercontent.com/112274822/233873921-20f809e6-8db3-44de-83b6-29b1775c2002.png">

### WikiChat Bot
**chat.py**

This code defines a Flask web application that provides a simple chatbot interface that uses Wikipedia to respond to user input. The application has a single HTML page called "chat.html" that includes a text input field for the user to enter a message and a button to submit the message. When the button is clicked, the application sends a POST request to the "/message" endpoint with the user's message as the request body. The application then processes the message by attempting to get a summary from Wikipedia and returning that summary as a JSON response. If the message is not recognized, the application returns an error message.

The index() function is the view function for the root URL ("/") and simply renders the "chat.html" template.

The reply() function is the view function for the "/message" endpoint. It handles POST requests and extracts the user's message from the request body using the request.get_json() method. It then attempts to get a summary from Wikipedia using the wikipedia.summary() function and returns that summary as a JSON response using the jsonify() method. If the message is not recognized, the function returns an error message.

To run the code, save it to a Python file (e.g. "wiki_chatbot.py") and run it in the terminal by navigating to the directory containing the file and typing "python wiki_chatbot.py" (without quotes) and then press enter. The application will start running and can be accessed in a web browser at "http://localhost:5000/".

<img width="833" alt="Screen Shot 2023-04-23 at 7 50 41 PM" src="https://user-images.githubusercontent.com/112274822/233873494-caa6b1d5-78a8-4de6-bff7-800c1dab0a6d.png">
<img width="836" alt="Screen Shot 2023-04-23 at 7 50 59 PM" src="https://user-images.githubusercontent.com/112274822/233873498-8a5120de-b35e-40f8-a52f-1fbc63617e9a.png">

### Searcher AI Bot
**search.py**

This code defines a Flask web application that searches Wikipedia for articles based on user input. The application has a single HTML page called "general.html" that includes a form with a single input field for the user to enter a search query. When the form is submitted, the application constructs a URL for the Wikipedia API based on the query and sends a GET request to that URL. It then processes the response to extract the search results and displays them on a web page.

The index() function is the main view function for the application. It handles both GET and POST requests to the root URL ("/") and renders the "general.html" template. If the request is a POST request (i.e. the user has submitted the form), the function extracts the search query from the form data and constructs a URL for the Wikipedia API based on the query. It then sends a GET request to that URL using the requests module and processes the response to extract the search results. If the response is successful and contains search results, the function renders the "general.html" template with the search results and the original query. If the response is not successful or does not contain search results, the function renders the "general.html" template with an error message.

To run the code, save it to a Python file (e.g. "wiki_search_app.py") and run it in the terminal by navigating to the directory containing the file and typing "python wiki_search_app.py" (without quotes) and then press enter. The application will start running and can be accessed in a web browser at "http://localhost:5000/".

<img width="1338" alt="Screen Shot 2023-04-23 at 7 51 16 PM" src="https://user-images.githubusercontent.com/112274822/233873832-82e4a91d-3a42-41ee-b4f7-077a2a54f546.png">

## Deployment and load test
### Deployment on the cloud
We then deployed the app on the **AWS App Runner**, so that the websites are able to be accessible to public. We used separated repositories for deployment.  

<img width="1437" alt="Screen Shot 2023-04-29 at 11 54 16 PM" src="https://user-images.githubusercontent.com/112274822/235334756-70bef80e-b11e-4689-94af-d3d7b65f850a.png">

You can find them here:  
- [wiki-bot-app](https://github.com/LiuSuen/wiki-bot-app/tree/main): https://yp2tum2pjq.us-east-1.awsapprunner.com
- [wiki-bot-chat](https://github.com/LiuSuen/wiki-bot-chat/tree/main): https://vqmeb2ndjf.us-east-1.awsapprunner.com
- [wiki-bot-search](https://github.com/LiuSuen/wiki-bot-search/tree/main): https://hq9ftb23ie.us-east-1.awsapprunner.com
### Load test
We used `locust` to test the scalability of the websites. Define the user behavior in locustfile.py, then run `locust` and visit http://localhost:8089 to start the test. And our websites are able to scale to 1000+ request.

<img width="999" alt="Screen Shot 2023-04-29 at 11 53 51 PM" src="https://user-images.githubusercontent.com/112274822/235334764-b7adecb3-3115-45fb-8e91-11a48fa81710.png">

```Python
pip3 install locust
# after creating a locustfile.py
locust
```
You can find more information about `locust` here: [Locust website](https://docs.locust.io/en/stable/what-is-locust.html)

<img width="1505" alt="Screen Shot 2023-04-29 at 11 53 38 PM" src="https://user-images.githubusercontent.com/112274822/235334772-16f9aa50-9b32-4f7d-943a-d6de33d336fa.png">

## Discusiions
### limitations
Although these applications provide useful functionality, they have some limitations. One limitation is that they rely solely on Wikipedia for information. This means that they may not always provide the most accurate or complete information, and they may not be able to answer all types of questions. Additionally, some of the applications have limited functionality, such as chat.py, which can only respond to messages with Wikipedia summaries.

### Future Work
There are several ways in which these applications could be improved or expanded in the future. One possibility is to incorporate other sources of information in addition to Wikipedia, such as other online encyclopedias or databases. Another possibility is to use machine learning algorithms to improve the accuracy and completeness of the information provided by these applications. Additionally, the chatbot interface could be expanded to support more advanced natural language processing techniques, allowing it to understand and respond to a wider range of user queries. Overall, there is a lot of potential for future development and improvement of these applications.

## Conclusions
To sum up, the four Python scripts provided above demonstrate the versatility and usefulness of Wikipedia as a source of information. They provide different ways to search and retrieve information from Wikipedia, ranging from a simple command-line interface to a more sophisticated web-based chatbot and AI search engine. Each of these scripts has its own unique features, strengths, and limitations, making them suitable for different use cases and audiences.
