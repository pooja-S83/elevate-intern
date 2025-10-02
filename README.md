<h1>TASK 1</h1>
<h3>Enhanced CLI Calculator 🧮</h3>
<br>
A small, safe, and user-friendly command-line calculator written in Python.
<br>
<b>Features</b>
Basic operations: add, subtract, multiply, divide
Extras: power, square root, percent
Free-form expressions (safe AST-based evaluation)
ans token → reuse last result
Shows and saves calculation history
<br>
<b>Follow the menu options:<b/>
1-7 → basic operations
<br>
8 → enter an expression (2+3*4, ans/2, etc.)
<br>
9 → show history
<br>
S → save history to file
<br>
Q → quit

<h1> TASK2 </h1>
<h3>Weekly To-Do List Manager</h3>

A simple <b>console-based Python application</b> to manage your weekly to-do tasks.  
You can add multiple tasks per day, mark them as done, edit, remove, or clear all tasks at once. Tasks are stored persistently in a text file (`tasks.txt`) in the same folder.

<h5>Features</h5>
- Add tasks for each day of the week (Monday → Sunday)  
- View tasks day-wise with status symbols:
  - ⏳ Pending  
  - 👍 Done  
- Mark a single task as done  
- Edit a task  
- Remove a single task  
- Remove all tasks at once
- Mark all tasks as done 
- Tasks are saved in `tasks.txt` in the same folder, so they persist across sessions

  Follow the on-screen menu to:
1. View tasks
2. Add tasks
3. Mark tasks as done
4. Remove tasks
5. Edit tasks
6. Remove all tasks
7. Mark all tasks as done
8. Exit

<h5>File Structure</h5>
<br>
task2/
│
<br>
├─ todo.py        # Main Python script
<br>
├─ tasks.txt      # Stores your weekly tasks (auto-created)
<br>
└─ README.md      # Project documentation

<h1> TASK3 </h1>
<h3>Web Scraper for News Headlines</h3>

📌 Objective

Build a Python script that automatically scrapes top news headlines from a public website and saves them into a text file.

<h5>🛠 Tools & Libraries Used </h5>
Python 3
<br>
requests – to send HTTP requests and fetch HTML
<br>
BeautifulSoup4– to parse and extract data from HTML
<br>
<b>Project Structure</b>
<br>
├── scraper.py      <br>
├── headlines.txt <br>
<br>

<h5>🚀 How It Works</h5>
<br>
The script sends an HTTP GET request to a news website (e.g., BBC News).
<br>
The HTML response is parsed using BeautifulSoup.
<br>
The program extracts all h2 tags (commonly used for headlines).
<br>
The cleaned text is saved in headlines.txt.
<br>

<h1>task 4</h1>
<h3>REST API with Flask</h3>
<br>
"A simple Flask REST API for managing users with GET, POST, PUT, and DELETE endpoints"
<br>
<h5>🚀 Features</h5>
<br>
- GET all users
<br>
- GET a single user by ID
<br>
- POST new user
<br>
- PUT update user
<br>
- DELETE user
<br>
<br>
<h5>🧠 Notes</h5>
<br>
- All responses are in JSON format.
<br>
- Error messages are descriptive and follow HTTP status codes.
<br>
- Designed for easy extension into database-backed APIs.
<br>

<h1>task 5</h1>
<h3>📊 Sales Data Analysis & Visualization</h3>
<br>
This project demonstrates how to load, process, and visualize sales data using Python's **Pandas** and **Matplotlib** libraries. It includes robust error handling for missing files and provides insights into total sales by product category.
<br>

<h5>🚀 Features</h5>
<br>
- Loads sales data from a CSV file using `pandas.read_csv()`
<br>
- Automatically generates sample data if the CSV is missing
<br>
- Displays DataFrame structure and summary
<br>
- Groups sales by product category using `groupby()` and `sum()`
<br>
- Visualizes results with a clean bar chart using `matplotlib.pyplot`
<br>
- Highlights highest and lowest selling categories
<br>

<h5>📈 Sample Output</h5>
- A bar chart showing total sales by product category
<br>
- Console output summarizing
<br>
- DataFrame structure
<br>
- Total sales per category
<br>
- Highest and lowest selling categories
<br>

<h1>task6</h1>
<h3>Personal Portfolio</h3>

<h5>🌟 Overview</h5>

This is a personal portfolio website showcasing the projects, skills, education, certificates, and contact details of Pooja Sajjan, a passionate Full Stack Developer specializing in Python, Django, JavaScript, React, and AI/ML.
<br>
Built with Flask, HTML, CSS, and Bootstrap for a clean and responsive design.

<h5>🚀 Features</h5>

👩‍💻 About Section — Personal introduction, skills summary.
<br>
🎓 Education Section — Academic achievements.
<br>
📝 About Me — Bio with personal vision and expertise.
<br>
💻 Skills Section — Technical proficiencies.
<br>
📂 Projects Showcase — Descriptions and tools used.
<br>
🏆 Certificates — Verified digital certifications.
<br>
📬 Contact Section — Email, LinkedIn, GitHub, phone.

<h1>task 7</h1>
<h3>🖼️ Image Resizer Tool</h3>

<h5>📌 Overview</h5>
<br>

This project is a Python-based Image Resizer and Converter built using the Pillow (PIL) library.
<br>
It allows you to batch resize images and convert formats (e.g., JPG → PNG) automatically.
<br>

🔹 <b>Technologies Used</b>: Python, Pillow, OS module
<br>
🔹 <b>Key Concepts</b>: File Handling, Image Processing
<br>

<h5>🚀 Features</h5>

Resize all images in a folder to a fixed size (default: 800x800).
<br>
Convert image formats (default: JPG/PNG/BMP → PNG).
<br>
Works on multiple image types (.jpg, .jpeg, .png, .gif, .bmp).
<br>
Skips unsupported files automatically.
<br>
Error handling with try-except.
<br>

<h5>behavior:</h5>

Reads all images from input_images/
<br>
Resizes them to 800x800
<br>
Converts them to PNG
,br>
Saves results inside output_images/
<br>
<h5>📂 Folder Structure</h5>

Image-Resizer-Tool/
<br>
 ├── task7_resizer.py
<br> 
 ├── input_images/      
<br>
 ├── output_images/
