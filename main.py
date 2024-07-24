from fastapi import FastAPI
from typing import Optional
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
# @app.get("/blog")
# async def index():
#     return {"data": "Blog list..."}

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
async def show_blog(id: int):  #here this step is very much similar to thr type conversion, this sort of things are managed by pidentics.
    return {"data": "Blog info", "id": id}


# Now we are going to see API docs which are swegger and redocs

# creating API in other frameworks is somehow tough beause some time we dont have any frontend or way to test the API ,
# # but fastAPI provides the automaitc documentations called swegger ui and redoc where we can test our API whenever needed. 



# QUERY Parameters:

# supposse we have a database which contains a blog. So fetching all the blogs from the database is super inefficient, so here we have to limit those things.
# So to solve these things the query parameter was introduced. Syntax= "/blog?limit=0&"published"=true. example:

@app.get("/blog")
async def index(limit=10,published: bool=True, sort: Optional[str]=None):                  # hre we have to note one thing that if we do not define the type of published than the value of published is always true even if we give published=false because every thing we give in path or end point is accepted as string
        if published:                                    #We can also give the default value to the published and the limit in order to get no error if these values are not passed. 
                return{f"{limit} published blogs are fetched from the db."}  #We can accept the optional parameter also, for that we have to import optional from typing

        else:
                 return {"data": f"{limit} blogs fetched from the database."}
        
  



