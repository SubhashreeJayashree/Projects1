import nltk
from nltk.chat.util import Chat, reflections

# python app.py
# Training with Personal Ques & Ans
conversation = [
    (r'Hi', ["Hello! How can I help you today?"]),
    (r'Helloo!', ["Hello! How can I assist you?"]),
    (r'Hey', ["Hey! How can I help you?"]),
    (r'How are you\?', [
        "I'm good. Go ahead and write the number of any query. 😃✨<br>1. Student's Section Enquiry.</br>2. Faculty Section Enquiry.</br>3. Parent's Section Enquiry.</br>4. Visitor's Section Enquiry.</br>"
    ]),
    (r'Great', [
        "Go ahead and write the number of any query. 😃✨<br>1. Student's Section Enquiry.</br>2. Faculty Section Enquiry.</br>3. Parent's Section Enquiry.</br>4. Visitor's Section Enquiry.</br>"
    ]),
    (r'good', [
        "Go ahead and write the number of any query. 😃✨<br>2. Faculty Section Enquiry.</br>3. Parent's Section Enquiry.</br>4. Visitor's Section Enquiry.</br>"
    ]),
    (r'fine', [
        "Go ahead and write the number of any query. 😃✨<br>2. Faculty Section Enquiry.</br>3. Parent's Section Enquiry.</br>4. Visitor's Section Enquiry.</br>"
    ]),
    (r'Thank You', ["You're welcome 😄"]),
    (r'Thanks', ["You're welcome 😄"]),
    (r'Bye', ["Thank you for visiting!"]),
    (r'What do you do\?', ["I am made to give information about  Gobi Arts and Science College college."]),
    (r'What else can you do\?', ["I can help you know more about  Gobi Arts and Science College."]),
    (r'1', [
        "<b>STUDENT <br>The following are frequently searched terms related to student. Please select one from the options below:<br> 1.1 Curriculars<br>1.2 Extra-Curriculars<br>1.3 Administrative<br>1.4 Examination<br>1.5 Placements </b>"
    ]),
    (r'1.1', [
        "<b>CURRICULAR <br>These are the top results: <br> 1.1.1 Moodle<br> 1.1.2 Academic Calendar<br>1.1.3 Syllabus</b>"
    ]),
    (r'1.1.1', [
        "<b>1.1.1 Moodle<br>The link to Moodle 👉 <a href='http://gyan.fragnel.edu.in:2222/moodle/'>Click Here</a></b>"
    ]),
    (r'1.1.2', [
        "<b>1.1.2 Academic Calendar<br>The link to Academic Calendar👉<a href='http://www.frcrce.ac.in/index.php/academics/academic-calendar'>Click Here</a></b>"
    ]),
    (r'1.1.3', [
        "<b>1.1.3 Syllabus<br>The link to Syllabus 👉 <a href='http://www.frcrce.ac.in/index.php/academics/tlp/syllabus'>Click Here</a></b>"
    ])
]

chatbot = Chat(conversation, reflections)
