# Saad-Abubakar-Portfolio-Organization-Web-Application

📌 Project Overview

This project is a full-stack web application developed as part of my 5th semester coursework in BS Software Engineering.

Instead of submitting a traditional written report describing my skills, I chose to demonstrate my practical knowledge by designing and implementing a complete web-based system using Flask.

The application includes:

A personal portfolio website

Admin authentication system

Contact message management

Rule-based chatbot

A linked fictional organization website (NovaEdge Skills Academy)

This entire project was developed independently, and all components are built using technologies that I understand and can confidently explain during viva.

🏗️ System Architecture

The system is divided into two main sections:

1️⃣ Personal Portfolio Website

The portfolio includes:

Home Page

About Page

Skills Page with animated progress bars

Projects Page

Services Page

Contact Form

Admin Login

Protected Admin Dashboard

Chatbot Page

The design uses gradient backgrounds, hover effects, and light animations implemented using CSS and JavaScript.

2️⃣ NovaEdge Skills Academy (Linked Website)

A fictional training institute connected to the portfolio.

It includes:

Home

About

Courses / Services

Contact

This section simulates a real-world organization system.

🤖 Chatbot Implementation

The chatbot is rule-based and implemented using Python logic.

It works by:

Converting user input to lowercase

Checking keywords using if / elif conditions

Returning predefined responses

It handles categories such as:

Greetings

Courses

Fee Structure

Institute Timings

Location

Contact Information

Registration

Technologies Used

Academic Information

Thanks & Goodbye

Default fallback responses

All chatbot interactions are stored in the SQLite database.

🛠️ Tech Stack
Frontend

HTML5

CSS3

JavaScript

Backend

Python

Flask

Database

SQLite (database.db)

No external CSS frameworks were used. All styling is written manually.

📂 Project Structure

Web project/
│
├── app.py
├── database.db
├── README.md
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
└── templates/
    ├── index.html
    ├── about.html
    ├── skills.html
    ├── projects.html
    ├── services.html
    ├── contact.html
    ├── login.html
    ├── dashboard.html
    ├── chatbot.html
    ├── academy_home.html
    ├── academy_about.html
    ├── academy_services.html
    └── academy_contact.html


    
