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

@app.get("/")


async def index():
    return {"data":{"name": "Aditya"}}

@app.get("/about")
async def about():
    return {"data": "ABout page"}



@app.get("/greet")
async def greet():
    return {"message" : "hello... FastAPI"}
