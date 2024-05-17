# Assignment-Library-website

Assignment web 2024

# How to run the django project

1. clone the rep
   - `git clone https://github.com/Feglawy/Assignment-Library-website.git`
2. make sure to have python installed

- check by typing `python` in terminal if it opened python then its all good

3. open the terminal in the project directory
4. make the venv
   - type in the terminal `python -m venv .venv` this is for windows
5. activate the venv

   - `./.venv/scripts/Activate.ps1` for powershell
   - `./.venv/scripts/activate.bat` for cmd

6. install the requirements
   - `pip install -r ./requirements.txt`
7. add the variables to the .env file see `.evn-example` file

   1. create a `.env` file then add your variables
   2. if you added on and used it in the project add the variable you used to the `.env-example` file to let us know
8. do the migrations
- `python manage.py makemigrations`
- `python manage.py migrate`

9.  run the server

- `python manage.py runserver`

10. run the server on any local device

- `python manage.py runsever 0.0.0.0:8000`

if there was any firewall problems allow the port 8000 by adding the rule in the firewall settings

### phase 1 html

- [x] navigation bar
- [x] home page (working on it) --Abdallah
- [x] login and signup pages (Done) --Islam
- [x] about page
- [x] preview page
- [x] update page
- [x] search (almost done)
- [x] available books
- [x] borrowed books
- [x] profile (Done) --Ahmed

---

### phase 2 js and css

- [x] make the password and confirm pass if they don't match make a pop up to tell the user the passwords should be the same
  - visualized it in the form
- [x] make the local and session storage
  - i've made local storage for the theme toggler

---

### phase 3 backend

- [x] django app structure
- [x] dark theme
- [x] make the database
  - [x] users database
  - [x] books database
  - [x] authors database
  - [x] geners database
  - [x] types database
  - [x] borrowed books database
- [ ] admin's update books page
      ...
- [ ] USE AJAX INSTEAD OF JS FETCH

---

- [x] TO-DO add to css some checks to screen width and hight
- [x] TO-DO add the tags and author name to the book preview page

---

## [Database structure](https://drawsql.app/teams/feglawy/diagrams/library)

### good assits

[Good website for shadowing](https://getcssscan.com/css-box-shadow-examples)

[Good website for glassy background](https://css.glass)

[Fonts website](https://fonts.google.com/)

[icons website](https://fonts.google.com/icons)

[quotes api](https://publicapi.dev/quotes-on-design-api)
