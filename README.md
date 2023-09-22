# Ingenious


**Step 1: Setup Environment**

- Make sure you have Python installed on your system. You can download it from the official Python website (https://www.python.org/).
- Create a virtual environment for your project. Open the terminal or command prompt and navigate to your project directory.
- Run the following command to create a virtual environment (OPTIONAL):

   ` python -m venv env `

- Activate the virtual environment:
  - For Windows:

    ` .\env\Scripts\activate `

  - For macOS/Linux:

    ` source env/bin/activate  `

**Step 2: Install Dependencies**

- With the virtual environment activated, install Django and other project dependencies. You can do this by running the following command:

    ` pip install django `

**Step 3: Database Setup**

- Configure the database settings in your Django project. Open the `settings.py` file located in your project's root directory.
- Update the `DATABASES` dictionary with the appropriate database settings (e.g., database engine, name, user, password).
- If you're using SQLite as the database, Django will create a default database file in your project directory. Otherwise, make sure the specified database server is running.

**Step 4: Run Migrations**

- Apply the database migrations to create the necessary tables in the database. In the terminal or command prompt, run the following command:

  ` python manage.py migrate `

**Step 5: Create a Superuser (Optional)**

- To access the Django admin interface and manage the project's data, you can create a superuser account by running the following command:

  ` python manage.py createsuperuser `

- Follow the prompts to provide a username, email (optional), and password for the superuser.
  - This superuser account can then be used to log in to the Django admin interface by accessing the `/admin` URL.
- This step allows you to create a superuser account without any conditional statements.

**Step 6: Run the Development Server**

- Start the Django development server by running the following command:

   ` python manage.py runserver `

- By default, the server will run on `http://localhost:8000/` .

**Step 7: Access the Project**

- Open your web browser and go to `http://localhost:8000/` (or the specified address).
- You should see your Django project running.

**Step 8: Explore and Test**

- Navigate through your Django project, access different views, and interact with the functionality.
- Ensure that all the features and requirements of your project are working as expected.

By following these steps, you can run your Ingenious project, and explore its functionalities.
