import nltk
from nltk.chat.util import Chat, reflections

# python app.py
# Training with Personal Ques & Ans
conversation = [
    (r'Hi', ["Hello! How can I help you today?"]),
    (r'Hello', ["Hello! How can I assist you?"]),
    (r'Hey', ["Hey! How can I help you?"]),
    (r'How are you?', [
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
    (r'What do you do?', ["I am made to give information about  Gobi Arts and Science College college."]),
    (r'What else can you do?', ["I can help you know more about  Gobi Arts and Science College."]),
    (r'Who created you?', ["Subha Created Me"]),
    (r'What is your name?', ["I Am A Chat Bot Only For Gobi Arts and Science College"]),
    (r'1', [
        "<b>STUDENT <br>The following are frequently searched terms related to student. Please select one from the options below:<br> 1.1 General College Information <br>1.2 Academic Calendar<br>1.3 Syllabus<br>1.4 Admission Procedure<br> 1.5 Departments and Courses<br>1.6 Facilities <br> 1.7 Fees and Scholarships<br> 1.8 Placements and Internships<br> 1.9 Examinations and Academics<br> 1.10 Extra-Curricular-Activities <br> 1.11 Emergency and Miscellaneous<br>"
    ]),
      (r'2', [
        "<b>FACULTY <br>The following are frequently searched terms related to student. Please select one from the options below:<br> 1.1 General College Information <br>1.2 Academic Calendar<br>1.3 Syllabus<br>1.4 Admission Procedure<br> 1.5 Departments and Courses<br>1.6 Facilities <br> 1.7 Fees and Scholarships<br> 1.8 Placements and Internships<br> 1.9 Examinations and Academics<br> 1.10 Extra-Curricular-Activities <br> 1.11 Emergency and Miscellaneous<br>"
    ]),
      (r'3', [
        "<b>PARENT <br>The following are frequently searched terms related to student. Please select one from the options below:<br> 1.1 General College Information <br>1.2 Academic Calendar<br>1.3 Syllabus<br>1.4 Admission Procedure<br> 1.5 Departments and Courses<br>1.6 Facilities <br> 1.7 Fees and Scholarships<br> 1.8 Placements and Internships<br> 1.9 Examinations and Academics<br> 1.10 Extra-Curricular-Activities <br> 1.11 Emergency and Miscellaneous<br>"
    ]),
      (r'4', [
        "<b>VISITORS <br>The following are frequently searched terms related to student. Please select one from the options below:<br> 1.1 General College Information <br>1.2 Academic Calendar<br>1.3 Syllabus<br>1.4 Admission Procedure<br> 1.5 Departments and Courses<br>1.6 Facilities <br> 1.7 Fees and Scholarships<br> 1.8 Placements and Internships<br> 1.9 Examinations and Academics<br> 1.10 Extra-Curricular-Activities <br> 1.11 Emergency and Miscellaneous<br>"
    ]),



(r'What courses are offered by Gobi Arts and Science College?',["Gobi Arts and Science College offers UG, PG, M.Phil, and Ph.D. programs in Arts, Science, and Commerce streams."]),
(r'Where is Gobi Arts and Science College located?',["The college is located in Karattadipalayam, Gobichettipalayam, Tamil Nadu - 638453."]),
(r'What are the contact details of the college?',["You can contact us at +91-4285-220441 or email principal@gobiartscollege.edu."]),
(r'What are the working hours of the college?',["The college operates from 10:00 AM to 4:00 PM, Monday to Saturday."]),
(r'What is the official website of the college?', ["The official website of Gobi Arts and Science College is www.gobiartscollege.edu."]),



(r'Academic Calendar?',[f"<b>Calendar 👉 <a href='http://localhost:5000/calendar'>Click Here</a><b>"]),

(r'Fees Structure?',[f"<b>Fees Structure 👉 <a href='http://localhost:5000/fees structure'>Click Here</a><b>"]),

(r' Syllabus?',[f"<b>Syllabus 👉 <a href='http://localhost:5000/Syllabus'>Click Here</a><b>"]),


 (r'What is the admission procedure?', ["<b>ADMISSION PROCEDURE 👉 <a href='http://localhost:5000/admission'>Click Here</a><b>"]),
(r'What is the admission process for Gobi Arts and Science College?',["Admissions involve submitting an online application form, eligibility verification, and document submission."]),
(r'What are the eligibility criteria for UG courses?',["Eligibility for UG courses requires completion of the 12th standard from a recognized board."]),
(r'What is the eligibility for PG courses?',["For PG courses, candidates must have completed a bachelor's degree in the relevant field."]),
(r'When does the admission process start?',["The admission process usually starts in May. Visit the college website for updates."]),
(r'What documents are required for admission?',["Required documents include mark sheets, Transfer Certificate, Community Certificate, and ID proof."]),



 (r'What departments are available in Gobi Arts and Science College?', ["Departments include Tamil, English, Mathematics, Physics, Chemistry, Computer Science, Commerce, Business Administration, and more."]),
(r'Does the college offer diploma or certificate courses?', ["Yes, the college offers short-term diploma and certificate courses in various fields."]),
(r'Are research programs like M.Phil and Ph.D. offered?', ["Yes, Gobi Arts and Science College offers M.Phil and Ph.D. programs in multiple disciplines."]),
(r'Does the college offer professional courses?',["Yes, the college offers professional programs like BBA, MBA, and MCA."]),
    

(r'Does Gobi Arts and Science College provide hostel facilities?',["Yes, the college provides separate hostels for boys and girls with modern amenities."]),
(r'What library facilities are available?',["The library includes a vast collection of books, e-resources, and research materials with a digital library feature."]),
(r'Does the college provide transportation services?',["Yes, college buses cover nearby towns and villages for students' convenience."]),
(r'Are there sports facilities at the college?',["Yes, the college has facilities for cricket, volleyball, athletics, and indoor games."]),
(r'Is the campus Wi-Fi enabled?',["Yes, the campus is Wi-Fi enabled for students and staff."]),


(r'What is the fee structure for Gobi Arts and Science College?',["The fee structure varies by course. Contact the college office or visit the website for details."]),
(r'Are there scholarships available?',["Yes, scholarships are available for merit-based, reserved category, and economically weaker students."]),
(r'Does the college provide fee concessions?',["Yes, eligible students can apply for fee concessions based on criteria like merit or economic background."]),
(r'How can I pay my fees?',["Fees can be paid online through the college portal or at the college office."]),
    

(r'Does the college provide placement assistance?',["Yes, the college has an active placement cell that collaborates with leading companies."]),
(r'What companies visit the college for placements?',["Companies like TCS, Infosys, Wipro, HCL, and Cognizant frequently visit the campus."]),
(r'Are internships available?',["Yes, internships are facilitated through industry tie-ups and collaboration programs."]),
(r'Does the college offer soft skills training?', ["Yes, the placement cell conducts soft skills and personality development training."]),
  

(r'What is the academic calendar for Gobi Arts and Science College?',["The academic calendar is updated on the college website under the 'Academics' section."]),
(r'How can I get my exam results?',["Results are published on the college website under the 'Examinations' section."]),
(r'What is the re-evaluation process for exam papers?',["Submit the re-evaluation form with the required fee at the examination office."]),
(r'How can I download my hall ticket?', ["Hall tickets can be downloaded from the college's online student portal."]),
    

(r'What extracurricular activities are available?',["Activities include NCC, NSS, cultural programs, and various student-run clubs."]),
(r'Does the college celebrate annual events?',["Yes, the college organizes annual cultural and sports events like 'Gobi Fest' and 'Sports Day'."]),
(r'What clubs can students join?',["Students can join clubs like the Literary Club, Science Club, and Eco Club."]),
(r'Are there leadership opportunities for students?',["Yes, students can take leadership roles in committees, clubs, and NSS/NCC programs."]),
    

(r'What should I do in case of a medical emergency?',["Medical assistance is available on campus, and students can contact the emergency helpline."]),
(r'How can I report grievances?',["Grievances can be submitted online through the grievance portal or to the grievance cell in person."]),
(r'Does the college support differently-abled students?', ["Yes, the college provides accessible infrastructure and support for differently-abled students."]),
(r'How can I get a Transfer Certificate?',["Submit an application form at the administration office to obtain a Transfer Certificate."])
]

chatbot = Chat(conversation, reflections)

