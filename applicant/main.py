#******************************************************************************#
# Main Driver Code Should Be Here                                              #
#******************************************************************************#
from fastapi import FastAPI
import graphene
import starlette
from starlette.graphql import GraphQLApp
from schema import Query

app = FastAPI()

# GraphQL Route
app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))

#Checking if the server is running
@app.get("/")
def ping():
    return {"ping": "pong!"}
