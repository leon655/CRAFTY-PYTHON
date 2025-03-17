The Blue-Collar Booking App is a command-line interface (CLI) application that allows you to manage workers and jobs. This is the backend system for a blue-collar worker booking platform.

Features
✔️ Add Workers (Plumbers, Electricians, Carpenters, etc.)
✔️ View Available Workers
✔️ Assign Jobs to Workers (Book a Worker)
✔️ View All Jobs (See which workers have been booked)
✔️ Delete Workers & Jobs

⚙️ Installation & Setup
Step 1: Clone the Repository
sh
Copy code
git clone https://github.com/your-repo/blue-collar-booking.git
cd blue-collar-booking

Step 2: Install Dependencies
Make sure you have pipenv installed. If not, install it:


pip install pipenv
Then install the project dependencies:


pipenv install

Step 3: Run the CLI
Activate the virtual environment:



pipenv shell
Run the CLI:


python cli.py
