# GitHub OAuth-Based Secure Login Mechanism

## Abstract

This project demonstrates the implementation of GitHub OAuth authentication using Flask, a lightweight web framework in Python. The objective was to understand and integrate OAuth 2.0 for user authentication, enabling secure login via GitHub accounts. The project implements key functionalities, including user login, data storage in SQLite, and user account management (logout and account deletion). A responsive front-end designed with HTML and CSS complements the back-end operations. Through this project, we learned to handle API responses, manage user sessions, and securely store user data. This application lays the foundation for integrating third-party OAuth services into web applications.

## Introduction
### Overview of GitHub OAuth
GitHub OAuth (Open Authorization) is a secure authentication mechanism that allows users to log into third-party applications using their GitHub accounts. OAuth 2.0 eliminates the need for applications to handle sensitive user credentials directly. Instead, it uses access tokens issued by GitHub after the user grants permission. These tokens allow the application to access authorized user data, such as profile information and email addresses, without exposing the user's password. This project uses GitHub's OAuth API to integrate login functionality, enabling users to authenticate seamlessly and securely while ensuring compliance with modern authentication standards.
### Purpose of the Project
The purpose of this project is to understand and implement OAuth 2.0, a modern authentication standard, using GitHub's API. It aims to provide a secure, user-friendly login mechanism for web applications while protecting user credentials. By storing and managing user information in an SQLite database, the project also demonstrates the integration of back-end database systems with a web application.

## Objectives

•	Understand the OAuth 2.0 authentication protocol.

•	Build a web application to demonstrate GitHub-based login functionality.

•	Securely store user data in a database.

•	Implement features for account management, including logout and account deletion.



## Technologies and Tools Used

•	Languages: Python, HTML, CSS.

•	Framework: Flask.

•	Database: SQLite.

•	APIs: GitHub API.

•	Libraries: Flask-Session, Requests, SQLite3.

•	Development Tools: Code editor (e.g., VS Code), GitHub for version control.


## Implementation

### Application Architecture: 
The project follows a client-server model. The Flask application serves as the back end, handling authentication requests, session management, and database interactions. The front end, built with HTML and CSS, provides a user-friendly interface for login and account management.
![image](https://github.com/user-attachments/assets/171184de-d1f5-4aa2-9003-348c78661106)
 
### Website Registration:
Third party should register their website for OAuth access.
 ![image](https://github.com/user-attachments/assets/9780ef65-f608-4612-aa59-8f8c68c18d24)

### Database Design:
We had used SQLite database here that includes a table named user with columns for id, username, github_id, email, and access_token. This schema stores essential user information securely.
 ![image](https://github.com/user-attachments/assets/2d0c7b49-3c01-443e-b1d4-43ac283f1dea)

## Results
The project successfully implements GitHub OAuth authentication. Users can log in using their GitHub accounts, with their details securely stored in the SQLite database. 

Key functionalities include:

•	Secure login and session management.

•	Display of user information (GitHub ID, username, email) on the welcome page.

•	Options to log out and delete accounts.


### Screenshots:

•	**Home Page:** Displays the "Sign in with GitHub" button.
 ![image](https://github.com/user-attachments/assets/6f2bdf36-08e3-4eac-b317-135209c774fe)

Now we will click Sign in with Github.
![image](https://github.com/user-attachments/assets/9b1d5426-ee4c-4baa-9a62-4eb8722537e4)
 
•	**Authorize user:** It will ask for authorization.
 ![image](https://github.com/user-attachments/assets/9e77f055-431f-46bf-992b-9726302d7485)

Click on authorize user. Then it will ask for password the user will  enter their github account password.

•	**Welcome Page:** Shows the logged-in user's details.
 ![image](https://github.com/user-attachments/assets/65ae509b-5904-4a16-bffb-c57e89382244)

Email is private in Github. That is why, it is None here.

We can logout by clicking on logout button that will return to homepage and can delete account by clicking on delete account button.

•	**Error Page:** Handles authentication errors gracefully.
 ![image](https://github.com/user-attachments/assets/2ac46fd9-45a7-4f6d-b0b9-7a6de8bb0ecd)

In case there is any issue with tokens or sessions these situations are handled in the code by rendering error.html.

•	**Registered Application page:**
 ![image](https://github.com/user-attachments/assets/a4a02dea-f06a-43bf-a972-af394b7ec7d2)

Here, we can see that how many users are currently logged in to website through github and can revoke tokens of all users.

The Client ID and secret also mentioned here. We used the same in code.

## Challenges and Learnings
### •	Challenges:

 • Managing GitHub API responses and handling errors.
 	
 • Securely revoking tokens and clearing sessions.
 	
 • Ensuring database consistency during account deletion.
 
### •	Learnings:
 	
 • Gained practical experience in implementing OAuth 2.0.
 	
 • Learned to manage user sessions and secure sensitive data.
 	
 • Improved understanding of Flask and database integration.

## Future Enhancements

•	Add support for other OAuth providers, such as Google or Facebook.

•	Implement user activity logs to track login history.

•	Deploy the application on a cloud platform for broader accessibility.


## Conclusion
The GitHub OAuth-based application ensures secure user authentication and session management through the implementation of OAuth 2.0 protocols and Flask-Session. By integrating token revocation and secure database management, the project demonstrates a strong commitment to safeguarding user data. Error handling mechanisms further enhance the reliability of the system, protecting it from potential vulnerabilities. This project serves as a robust foundation for understanding secure authentication workflows and provides opportunities for future enhancements, such as token encryption and improved scalability.
