import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Example story with placeholders
story_template = """
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. One day, the {noun1} met a {adjective2} {noun2} while walking through the {place}.
"""

# Function to extract placeholders using regular expressions
def extract_placeholders(story):
    return re.findall(r'{(.*?)}', story)

# Homepage route to render the form dynamically
@app.route('/')
def form():
    placeholders = extract_placeholders(story_template)
    return render_template('form.html', placeholders=placeholders)

# Route to display the completed story
@app.route('/story', methods=['POST'])
def story():
    user_inputs = {placeholder: request.form[placeholder] for placeholder in extract_placeholders(story_template)}
    completed_story = story_template.format(**user_inputs)
    return render_template('story.html', story=completed_story)

if __name__ == '__main__':
    app.run(debug=True)
