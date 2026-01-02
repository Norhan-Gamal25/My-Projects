# Braille Tutorials Web App
### Video Demo: <https://youtu.be/HgRcto3mcWs?list=PLWAx-nV-HqdXRIGZUCqCVqhEh6_8XgAJy>
### Description:

This is a comprehensive web application built with Flask and SQLite, designed to facilitate the learning of the Braille system. It provides structured lessons, interactive quizzes across different Braille categories, and a dedicated progress tracking feature to monitor the user's learning journey.

### Purpose:

A heartfelt attempt to create an accessible and interactive educational platform, offering a self-paced and engaging method for individuals to master the fundamentals of Braille.

> \[\!IMPORTANT\]
> Ensure that all required libraries and database configurations are met to run the web application smoothly. The database structure must be initialized with the necessary tables (`users`, `braille_quizzes`, `quiz_attempts`).

### Libraries and Technologies:

  * **Flask:** A lightweight and flexible Python web framework used to build the application's core structure, routes, and templating.
    [\[Documentation\]](https://flask.palletsprojects.com/)
  * **CS50 SQL (`cs50` library):** A simplified wrapper for database operations, making it easy to interact with the SQLite database (`braille.db`) for managing user data and quiz information.
    [\[Documentation\]](https://cs50.readthedocs.io/libraries/sql/python/)
  * **Werkzeug Security:** Utilized for secure password hashing (using `generate_password_hash`) and verification (`check_password_hash`) during user registration and login.
    [\[Documentation\]](https://werkzeug.palletsprojects.com/en/latest/utils/#security-helpers)
  * **Flask-Session:** Manages user sessions, storing essential data (like `user_id`) on the filesystem to maintain state across requests.
    [\[PyPI package\]](https://pypi.org/project/Flask-Session/)
  * **Python's `os`:** Used primarily for accessing environment variables, such as a secure `SECRET_KEY`, or generating a random key for session security.
    [\[Documentation\]](https://docs.python.org/3/library/os.html)
  * **Custom Helpers (`helpers.py`):** Includes utility functions such as `login_required` (to protect routes), `apology` (for funny user-friendly error pages), and potentially `textToaudio` (for audio feedback on quiz attempts, a unique feature).

### Core Functionality and Structure:

The application is structured around user authentication, lesson delivery, quiz interaction, and progress reporting:

1.  **Authentication Routes (`/login`, `/register`, `/logout`):**
    
      * Handles user signup, securely hashing and storing passwords in the `users` table.
      * Authenticates returning users and manages the session using `session["user_id"]`.
      * Ensures secure, non-cached responses with the `@app.after_request` function.

2.  **Home and Lessons (`/`, `/lessons`):**
    
      * The root route (`/`) serves as the application's landing page.
      * The Lessons route (`/lessons`) is protected by `@login_required` and displays the educational content for Braille.

3.  **Interactive Quizzes (`/quizzes`):**
    
      * **GET Request:** Fetches quizzes from the `braille_quizzes` table, segregating them into sections: 'Alphabet & Numbers', 'Punctuation', and 'Contractions'.
      * **POST Request:** Processes user submissions. It checks the input against the correct answer from the database.
      * **Feedback System:** Records the attempt (`is_correct` 1 or 0) in the `quiz_attempts` table, and provides immediate, engaging feedback to the user via the `textToaudio` helper.

4.  **Progress Tracking (`/progress`):**
    
      * Protected by `@login_required`.
      * Queries the database to retrieve a user's complete history of quiz attempts, showing the question, correctness, and timestamp, allowing users to track their learning curve.

### Features:

  * **Secure User Authentication:** Implements industry-standard password hashing using `werkzeug.security`.
  * **Categorized Learning:** Structured quizzes covering different phases of Braille (Alphabet, Numbers, Punctuation, Contractions).
  * **Interactive Audio Feedback:** Uses the `textToaudio` function to give immediate, spoken feedback upon quiz submission.
  * **Comprehensive Progress Report:** A dedicated page to visualize all past quiz attempts and results.

### Limitations:

  * **Database Scalability:** Uses SQLite, which is ideal for development and small-scale use, but less suitable for high-traffic, large-scale deployments.
  * **Content Management:** Quiz content is hardcoded into the `braille_quizzes` table and must be manually updated.
  * **Language Support:** The content and feedback mechanisms are currently structured for English Braille.

### Conclusion:

This program reflects a foundational, yet feature-rich, approach to creating educational web tools. By combining a solid web framework with a structured learning path and engaging feedback, it provides a valuable resource for anyone beginning their journey with Braille.

