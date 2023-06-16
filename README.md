# AI-LightHouse

AI-LightHouse is a Flask web application that scrapes articles related to AI safety, machine learning, and artificial intelligence from various news sources using the News API. The application saves the article information in a PostgreSQL database, which can be queried to fetch and display articles on the frontend.

-----Installation------
Before you start, ensure you have installed the following:

Python 3.6 or newer
pip (Python package installer)
Virtualenv (for creating a virtual environment)
PostgreSQL (database)

------Set Up------------

1. Clone the repository:

  Use the following command to clone the repository to your local machine:

  git clone https://github.com/tonionio/AI-LightHouse.git

2. Set up the virtual environment:

  Navigate to the directory where you cloned the repository and create a virtual environment:

  cd AI-LightHouse
  python3 -m venv venv

  Activate the virtual environment:

  source venv/bin/activate

3. Install the requirements:

  Use pip to install the requirements from the requirements.txt file:

  pip install -r requirements.txt

4. Set up the database:

  Start your PostgreSQL service and create a database. Use the provided SQL script aisafety.sql to create the required tables. Make sure       to update the config.py file with your PostgreSQL connection details.

5. Set up environment variables:

  Create a .env file in the root directory of the project and define the following variables:

  makefile:

  FLASK_APP=run.py
  FLASK_ENV=development

  This will ensure Flask is correctly set up when you run the application.

6. Run the application:

  You can now run the application using the following command:

  flask run

  The application is now running and you can access it in your web browser at http://localhost:5000.

Please note that a frontend for this application has not been developed yet. The application currently only scrapes and stores articles in the database when the /scrape route is accessed.

Thanks for checking our my project:)

