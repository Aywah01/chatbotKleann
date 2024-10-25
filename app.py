from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    solutions = get_cleaning_solutions(user_input)
    return jsonify({"response": solutions})

def get_cleaning_solutions(user_input):
    # Assuming the user input gives a clue about the problem
    query = user_input.replace(" ", "+")  # Prepare query for URL
    url = f"https://www.google.com/search?q={query}+cleaning+tips"

    # Fetch the search result page
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant results
    results = []
    for g in soup.find_all('div', class_='BNeawe iBp4i AP7Wnd'):
        results.append(g.get_text())
        if len(results) >= 3:  # Limit to 3 results
            break
            
    return results if results else ["Sorry, no solutions found."]

if __name__ == '__main__':
    app.run(debug=True)
