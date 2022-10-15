# TodoListApi
TodoListApi

A simple Todo list Api, built with Django rest framework.
It features a simple custom username, email and password signup and
email and password login.

## Endpoints
To get the list of todos
> ```localhost:3000/```

## To sign up
Endpoint
> ```localhost:3000/auth/signup/```

Request Type
> ```POST```
   * Request body
     >```json
     >{
     >    "username": "unique_username",
     >    "email": "fake@gmail.com",
     >    "last_name": "Last name",
     >    "first_name": "First name",
     >    "password": "123456789"
     >}
     >```

# To sign in
Endpoint
> ```localhost:3000/auth/signin/```
Request Type
> ```POST```
   * Request body
     >```json
     >{
     >    "email": "fake@gmail.com",
     >    "password": "123456789"
     >}
     >```

This project uses token based authentication.
The token is return in the response after each sign in or sign up request.

Still an unfinished project.
