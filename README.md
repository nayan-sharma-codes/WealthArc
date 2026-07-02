# WealthArc 📊

*A full-stack, lightweight personal finance tracker designed for speed, security, and minimalist data visualization.*

## Overview 🌟
WealthArc is a complete web application that allows users to seamlessly log their income and expenses, categorizing them into a clean, interactive dashboard. Built with a focus on a frictionless user experience, it features an automated registration system and dynamic, client-side rendering for real-time financial insights.

## Core Features ✨
* **Secure Authentication:** Custom session-based login gateway with automated user provisioning.
* **Live Visualizations:** Integrated Chart.js doughnut graphs that instantly recalculate and redraw upon new database entries.
* **Persistent Storage:** Robust SQLite relational database architecture linking unique user IDs to their specific transaction ledgers.
* **High-Fidelity UI:** A responsive, high-contrast landing page and dashboard utilizing CSS Grid and Flexbox for a premium layout.

## Tech Stack 🛠️
* **Frontend:** HTML5, CSS3, JavaScript, Chart.js
* **Backend:** Python, Flask 
* **Database:** SQLite3

## Local Installation 🚀
To run this project locally on your machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/WealthArc.git
Navigate into the directory and install the required backend framework:

Bash
cd WealthArc
pip install Flask
Initialize the local database:

Bash
python create_db.py
Boot up the local server:

Bash
python app.py
Open http://127.0.0.1:5000 in your web browser.

Future Roadmap 🗺️
[ ] Migrate from SQLite to PostgreSQL for scalable, cloud-based hosting.

[ ] Integrate Razorpay/Stripe APIs to transition the platform into a SaaS model.

[ ] Develop an affiliate recommendation engine for financial products.
