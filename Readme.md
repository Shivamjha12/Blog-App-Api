# Blog App API Documentation

This Django app provides API endpoints to manage blog posts and comments.


## Endpoints

### Get Blog List

Retrieves a list of all blogs from database.

- **URL:** `blogs/`
- **Method:** GET
- Return all the list of blogs in the Database.

### Get Blog Detail

Retrieves details of a blog.

- **URL:** `/blog/{id}/`
- **Method:** GET
- Return the detail about blog when id passed.

### Fetch Blog Comments

Fetches the comments of a blog.

- **URL:** `blogcomments/{id}/`
- **Method:** GET
- Return the comments[] of a particular blog.

### Add New BLog Post to Database

- **URL:** `addblog`
- **Method:** POST
- Add the blog post in the database, by passing the json.

eg: 
{
"title":"why you start reading",
"content":"Reading books help us to focus more, by doing this for long time our focus ability get increased",
"user":"admin@gmail.com"
}

### Add Comment to Blog

- **URL:** `addcomment/`
- **Method:** POST
- Add the comment on specific blogPost, by passing the json.

### Update the Blog

- **URL:** `updateblog/{blog_id}/`
- **Method:** PUT
- It updates the values of blog fields by passing the json, but Author of the blog can only update the values.


## Users API

###  Register the user

- **URL:** `users/register`
- **Method:** POST
- It Register new user on blog app by passing values name,email and password as json.
- eg: { "name": "Shivam Jha", "email": "testuser@gmail.com","password":"123" }

###  Login for users

- **URL:** `users/login`
- **Method:** POST
- It helps user to login on blog app by passing values email and password as json.
- eg: { "email": "testuser@gmail.com","password":"123" }

###  GET USER

- **URL:** `users/user/{JWT TOKEN}`
- **Method:** GET
- It helps gey the user email id from blog app by passing JWT token as json, we also use it for verification.
- eg: {"jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNjkyNjUwNTAxLCJpYXQiOjE2OTI2MDczMDF95ah2JczenYR5XY18IopW_0KkVHS4LBJlYJyOZiAie5g"
}

###  Logout for users

- **URL:** `users/logout`
- **Method:** POST
- It helps user to logout from blog app.
