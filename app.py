# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     user_input = request.json['message']
    
#     # Fetching tips and video links
#     tips = fetch_cleaning_tips(user_input)
#     video = fetch_youtube_video(user_input)
    
#     # Log the responses
#     print(f"User Input: {user_input}")
#     print(f"Tips: {tips}")
#     print(f"Video: {video}")
    
#     return jsonify({"tips": tips, "video": video})

# def fetch_cleaning_tips(query):
#     # Example cleaning tips fetch function
#     return ["Tip 1: Use vinegar for cleaning.", "Tip 2: Don't forget to dust!"]

# def fetch_youtube_video(query):
#     api_key = 'AIzaSyC1oOkmOUefvJ8Z_J8HbVacUwXdQZ3spCI'# dont forget to insert ur API key
#     url = "https://www.googleapis.com/youtube/v3/search"
    
#     params = {
#         "part": "snippet",
#         "q": query + " cleaning tips",
#         "key": api_key,
#         "maxResults": 1,  # Limit results to 1 video
#         "type": "video"   # Ensure only video results
#     }

#     try:
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             video_data = response.json()
#             if video_data['items']:
#                 video_id = video_data['items'][0]['id']['videoId']
#                 return f"https://www.youtube.com/watch?v={video_id}"
#             else:
#                 return "No video found."
#         else:
#             return f"Error: {response.status_code} - {response.text}"
#     except requests.RequestException as e:
#         return f"Error fetching video: {str(e)}"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Example user profiles (This can be expanded or modified)
user_profiles = {
    'user1': {
        'name': 'John Doe',
        'job': 'Software Engineer',
        'age': 28,
        'busy': True,
        'commitment_level': 'medium'
    },
    'user2': {
        'name': 'Sarah Smith',
        'job': 'Teacher',
        'age': 34,
        'busy': False,
        'commitment_level': 'high'
    },
    'user3': {
        'name': 'Alex Johnson',
        'job': 'Freelancer',
        'age': 22,
        'busy': False,
        'commitment_level': 'low'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data['message']
    user = data['profile']  # Get user profile from the input
    
    # Generate recommendations based on user characteristics
    recommendations = generate_recommendations(user)

    # Fetching tips and video links
    tips = fetch_cleaning_tips(user_input)
    video = fetch_youtube_video(user_input)
    
    # Log the responses
    print(f"User Input: {user_input}")
    print(f"User Profile: {user}")
    print(f"Tips: {tips}")
    print(f"Video: {video}")
    
    # Combining everything into a single response
    return jsonify({"tips": tips, "video": video, "recommendations": recommendations})

def fetch_cleaning_tips(query):
    # Example cleaning tips fetch function
    return ["Tip 1: Use vinegar for cleaning.", "Tip 2: Don't forget to dust!"]

def fetch_youtube_video(query):
    api_key = 'AIzaSyC1oOkmOUefvJ8Z_J8HbVacUwXdQZ3spCI'  # Don't forget to insert your API key
    url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        "part": "snippet",
        "q": query + " cleaning tips",
        "key": api_key,
        "maxResults": 1,  # Limit results to 1 video
        "type": "video"   # Ensure only video results
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            video_data = response.json()
            if video_data['items']:
                video_id = video_data['items'][0]['id']['videoId']
                return f"https://www.youtube.com/watch?v={video_id}"
            else:
                return "No video found."
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.RequestException as e:
        return f"Error fetching video: {str(e)}"

def generate_recommendations(user):
    recommendations = []
    
    if user['busy']:
        recommendations.append("Set aside short daily cleaning sessions.")
        recommendations.append("Focus on one task at a time to avoid overwhelm.")
    else:
        recommendations.append("Create a cleaning schedule to maintain order.")
        recommendations.append("Consider involving others to make it a social activity.")
        
    if user['commitment_level'] == 'high':
        recommendations.append("Plan for monthly deep cleaning days.")
    elif user['commitment_level'] == 'medium':
        recommendations.append("Maintain regular cleaning routines.")
    else:
        recommendations.append("Start with small tasks to avoid burnout.")
    
    return recommendations

if __name__ == '__main__':
    app.run(debug=True)