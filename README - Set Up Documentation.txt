DOCUMENTATION FOR SETTING UP AND RUNNING THE HOMESTAYHUB DJANGO PROJECT

YOU NEED TO HAVE PYTHON AND DJANGO INSTALLED ON YOUR COMPUTER BEFORE PROCEEDING.

RUNNING THE PROJECT
1) Open project in VS Code.
2) Open the terminal and type "python manage.py runserver"
3) Once the server is live, type the URL that is in the terminal in your preferred browser. Then type "/propertylistings" at the end of the URL to reach the homepage of the website. (ex: http://127.0.0.1:8000/propertylistings)
4) Finally, you have all of the listings shown on the page. You can click "More Info" on whichever listing to view the details page.

ADMIN PANEL OPERATIONS
1) Using the same URL that was in the VS Code terminal after runing the server, type "/admin" at the end of the URL to reach the admin page. (ex: http://127.0.0.1:8000/admin)
2) Go back to the terminal to create a login and password to access the admin panel. Type "python manage.py createsuperuser". You will then have to enter a username, email address and password. You now have an admin account and can login as an admin.
3) Enter your login info on the admin page to access the admin panel.
4) From here, you should be able to see the "Authentication and Authorization" section, where you can make changes or add Groups and Users. And you can also see the "Property Listings" sections, where you can make changes or add Listings for the website.
5) You can now add and/or change any detail for any listing you would like.