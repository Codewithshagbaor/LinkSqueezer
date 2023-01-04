# LinkSqueezer
This is a simple URL shortener built using Django. It allows users to input a long URL and receive a shorter, unique URL in return. The short URL can then be shared and used to redirect to the original long URL.

To help prevent abuse and spam, the URL shortener includes a "I'm not a robot" validation check powered by reCAPTCHA. Users will need to verify that they are not a robot before they can be redirected the URL

# Preview
https://web-production-43d1.up.railway.app

# Prerequisites
Before getting started, make sure you have the following prerequisites installed:

Python 3
Django
Any additional dependencies listed in requirements.txt
A reCAPTCHA API key (obtainable from the reCAPTCHA website)
Installation
To install the URL shortener, follow these steps:

1. Clone the repository: git clone https://github.com/Codewithshagbaor/LinkSqueezer.git
2. Navigate to the project directory: cd LinkSqueezer
3. Install the required dependencies: pip install -r requirements.txt
4. Set up the reCAPTCHA API key:
In the project directory, create a file named .env
Add the following line to the file, replacing YOUR_API_KEY with your actual API key: RECAPTCHA_SITE_KEY=YOUR_API_KEY
5. Run the migration scripts to set up the database: python manage.py migrate
6. Start the development server:python manage.py makemigrations then  python manage.py runserver
# Usage
To use the URL shortener, follow these steps:

1. Open your web browser and go to http://localhost:8000/
2. Enter the long URL you want to shorten in the input field
3. Click the "Shorten URL" button
4. Share the short URL with others to redirect them to the original long URL

# Contributions
If you want to contribute to this project, please follow these guidelines:

1. Create a new branch for your changes: git checkout -b NEW-BRANCH-NAME
2. Make your changes and commit them: git commit -am 'Add some changes'
3. Push your changes to your branch: git push origin NEW-BRANCH-NAME
4. Create a pull request to merge your changes into the master branch

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
