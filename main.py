from fastapi import FastAPI

app=FastAPI() #creating an instance of FastAPI

#what is an end point..
#amazon.com/create-user         " we can say that create user is an end point in this example which is creating a new user to the amazon.com , so for this we have to post some user info in this end point.
#there are various end points , some of the widely used end points are:
# GET - GET AN INFO
# POST - CREATE SOMETHING NEW 
# PUT  -TO UPDATE
# DELETE- TO DELETE SOMETHING

#creating an end point

# @app.get("/")


# async def index():
#     return {"data":{"name": "Aditya"}}

# @app.get("/about")
# async def about():
#     return {"data": "ABout page"}



# @app.get("/greet")
# async def greet():
#     return {"message" : "hello... FastAPI"}



# now we are going to learn about path parameters in fastapi...

#suppose we have to fetch a blog list
@app.get("/")
async def index():
    return {"data": "Blog list..."}

#above function will show {"data" : "blog list"}
#now we have to fetch a perticular blog info from the blog list.

# @app.get('/blog/{id}')          # Here we are passing the id dynamically.
# async def show_blog(id):
#     return {"data": "Blog info", "id": id}

#by running the above code we are getting the id in the form of string but we wanted the id in the form of integer.
# for that we have to define the type in the function parameter. 

@app.get("/blog/unpublished")                  #fetching this will through an error of integer cant be parsed in string.this error is because of the line by line execution of fastAPI.
async def unpublished():                       #firstly it will match with the localhost peth, and found unmatched , then it will compare it with the dynamic id function where it find that after blog some string is there so it will take it as a match and after proceding it will found that the str value is then converted into the int and this is not the valid match so it will through an error. to solve this we have to define unpublisd above the dynamic id function.
    return {"data":"unpublished blogs."}       #here we have defined it above dynamic id. and now it is error free

@app.get('/blog/{id}')          # Here we are passing the id dynamically.
async def show_blog(id: int):
    return {"data": "Blog info", "id": id}



