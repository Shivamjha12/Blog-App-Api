# Blog App API Documentation

This Django app provides API endpoints to manage blog posts and comments.


## Endpoints

### Get Blog List

Retrieves a list of all elevators.

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

