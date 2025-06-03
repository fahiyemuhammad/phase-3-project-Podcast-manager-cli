# phase-3-project-Podcast-manager-cli

Podcast Tracker CLI
A personal command-line tool to track podcasts and episodes, built with Python and SQLAlchemy.

Features
Add podcasts to your personal library

Track episodes (listened, in-progress, or to-listen)

Search and filter your podcast collection

Statistics about your listening habits

Export/import your podcast data

Installation
Clone this repository:

bash
git clone https://github.com/fahiyemuhammad/podcast-tracker-cli.git
cd podcast-tracker-cli
Set up a virtual environment (recommended):

bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
pip install -r requirements.txt
Configuration
Copy the example configuration file:

bash
cp config.example.py config.py
Edit config.py to set your preferences:

python
DATABASE_URI = 'sqlite:///podcasts.db' # SQLite by default

# DATABASE_URI = 'postgresql://user:password@localhost/podcasts' # For PostgreSQL

Usage
Run the CLI tool:

bash
python main.py
Basic Commands
add [podcast_name]: Add a new podcast

list: Show all podcasts

episodes [podcast_id]: List episodes for a podcast

update [podcast_id]: Mark episodes as listened

stats: Show listening statistics

help: Show available commands

exit: Quit the application

Database Schema
The application uses the following database structure:

Podcasts: id, name, url, description, added_date

Episodes: id, podcast_id, title, url, duration, publish_date, status (listened/in-progress/to-listen)

Development
Dependencies
Python 3.8+

SQLAlchemy

pytest (for testing)

Running Tests
bash
pytest
Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
