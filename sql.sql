create database register;
create table users(name varchar(30),email varchar(30),password varchar(30));
create table suggestion(email varchar(30),message varchar(100));
-- Create the database
CREATE DATABASE CollegeChatbot;

-- Use the created database
USE CollegeChatbot;
-- Insert sample data
INSERT INTO chatbot_responses (question, answer) VALUES
('what courses do you offer?', 'We offer courses in Computer Science, Engineering, Business, and Arts.'),
('what is the admission process?', 'You can apply online through our portal or contact the admission office for assistance.'),
('what are the college timings?', 'The college operates from 8:00 AM to 5:00 PM, Monday to Friday.')