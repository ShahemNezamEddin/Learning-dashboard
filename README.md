# Learning-dashboard
- Learning-dashboard is a site that hopes to demonstrate how pure HTML, CSS, JavaScript, Python and, Django  works in a real-world context. 
- The site will be targeted users who want to CRUD notes, CRUD homework, and search a book, and wikipedia.
- The site hopes to help users to make their learning easier.
- The users can register to us the notes, and homework.
- The users can us the books, and wikipedia with out register.
- It will show that the notes and the homeworks after the user is login.
- Learning-dashboard is a application will have a postgres database.

[Learning-dashboard]() site.

![Responsive Mockup]()

# Navigator

- [**User experience UX**](<#user-experience-ux>)
    - [User stories](<#user-stories>)
    - [Site structure](<#site-structure>)
- [**Features**](<#features>)
    - [Existing features](<#existing-features>)
        - [Home](<#home>)
        - [Notes](<#notes>)
        - [Delete_note](<#delete_note>)
        - [Homework](<#homework>)
        - [Update_homework](<#update_homework>)
        - [Delete_homework](<#delete_homework>)
        - [Books](<#books>)
        - [Wiki](<#wiki>)
        - [Register](<#register>)
    - [Future features](<#future-features>)
- [**Technologies used**](<#technologies-used>)
- [**Python Packages**](<#python-packages>)        
- [**Testing**](<#testing>)
    - [Code Validation](<#code-validation>)
    - [Browser Compatibility](<#browser-compatibility>)
    - [Responsiveness Test](<#responsiveness-test>)
    - [Lighthouse](<#lighthouse>)
    - [Manual testing](<#manual-testing>)
    - [User stories testing](<#user-stories-testing>)
    - [Fixed bugs](<#Fixed-bugs>)
# User experience (UX)

## User stories

- As a user, I want to understand the purpose of this site upon loading it.
- As a user, I want to be able to know what are the instructions to use this site.
- As a user, I want to be able to add or delete note, and update the database.
- As a user, I want to be able to add or delete homework, and update the database.
- As a user, I want to be able to search a book, and open in a now tap.
- As a user, I want to be able to search on wikipedia, and open in a now tap.
- As a user, I want to be able to register, login and logout.
- As a user, I want to be able to navigate easily on the site.
- As a user I want have an easy way of getting back to the home page.

[Back to top](<#navigator>)

## Site structure

- Learning-dashboard is application that is being presented in 8 pages website.
- When the application starts the user see a short welcome message, and four choices.
- Two of them are accessed without login
- Two of them are accessed with login.
 
[Back to top](<#navigator>)

# Features 

## Existing features

### Home
- Render the home page.

[Back to top](<#navigator>)

### Notes
- Render the notes page, and the user abel to add note.
- The user gets a success message after he adds the note.

[Back to top](<#navigator>)

### Delete_note
- Redirect to the notes page, and the user abel to delete note.
- The user gets a success message after he deletes the note.

[Back to top](<#navigator>)

### Homework
- Render the homework page, and the user abel to add homework.
- The user gets a success message after he adds the homework.

[Back to top](<#navigator>)

### Update_homework
- Render the homework page, and the user abel to update is_finished in homework.

[Back to top](<#navigator>)

### Delete_homework
- Redirect to the notes page, and the user abel to delete homework.
- The user gets a success message after he deletes the homework.

[Back to top](<#navigator>)

### Books
- Render the books page, get the input text from the user then search it, and get the top ten results.

[Back to top](<#navigator>)

### Wiki
- Render the wiki page, get the input text from the user then search it.

[Back to top](<#navigator>)

### Register
- Render the register page, get the input text from the user then create a user.
- The user gets a success message after he register.
- Redirect to the login page.

[Back to top](<#navigator>)

## Future features

[Back to top](<#navigator>)

# Technologies used
- [Django](https://www.djangoproject.com/) - Provides Python web framework for the application.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the application.
- [ElephantSQL](https://customer.elephantsql.com/) - Used to host the application data.
- [Gitpod](https://www.gitpod.io/#get-started) - used to deploy the website.
- [Github](https://github.com/) - used to host and edit the website.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.

[Back to top](<#navigator>)

# Python Packages
- [Sys](https://docs.python.org/3/library/sys.html) - A module that provides access to used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available (*text taken from [here](https://docs.python.org/3/library/sys.html)*)
- [OS](https://docs.python.org/3/library/os.html) - A module that provides a portable way of using OS dependent functionality.

[Back to top](<#navigator>)

# Testing 

## Code Validation

### Python

* No errors were returned when passing through the official [CI Python Linter](https://pep8ci.herokuapp.com/)

![CI Python Linter]()

[Back to top](<#navigator>)

## Browser Compatibility

- Learning-dashboard site was tested on the following browsers Google Chrome, Safari and Mozilla Firefox.
- Appearance, functionality and responsiveness were consistent on a range of different device sizes and browsers.

[Back to top](<#navigator>)

## Responsiveness Test

* The responsive tests were exercised by using [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/).

|        | iPad mine | Galaxy S5 | iPhone 6/7/8 | iPad | iPad Pro | iPhone 6/7/8 plus | Display >950px  |
|--------|-----------|-----------|--------------|------|----------|-------------------|-----------------|
| Text   | pass      | pass      | pass         | pass | pass     | pass              | pass            |
| images | pass      | pass      | pass         | pass | pass     | pass              | pass            |
| forms  | pass      | pass      | pass         | pass | pass     | pass              | pass            |
[Back to top](<#navigator>)

## Lighthouse
Shahem inventory site was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools to test the page for:
- Performance - How the page performs whilst loading.
- Accessibility - Is the site accessible for all users and how can it be improved.
- Best Practices - Site conforms to industry best practices.
- SEO - Search engine optimization. Is the site optimized for search engine result rankings.

![Lighthouse test results Dice Game page]()

[Back to top](<#navigator>)

## Manual testing
- Show home page working as expected.
- Home page features working as expected.
- Show notes page working as expected.
- Notes page features working as expected.
- Show homework page working as expected.
- Homework page features working as expected.
- Show books page working as expected.
- Books page features working as expected.
- Show wiki page working as expected.
- Wiki page features working as expected.
- Show register page working as expected.
- Register page features working as expected. 
- If user is not login notes and homework pages redirect to the login page.
- After delete note redirect to the notes page.
- After delete homework redirect to the homework page.
- The navigation bar working as expected. 


[Back to top](<#navigator>)
