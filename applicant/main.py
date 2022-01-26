#******************************************************************************#
# Main Driver Code Should Be Here                                              #
#******************************************************************************#
from fastapi import FastAPI
import graphene
import starlette
from starlette.graphql import GraphQLApp
from schema import Query, Mutation

app = FastAPI()

# GraphQL Route
app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

#Checking if the server is running
@app.get("/")
def ping():
    return {"ping": "pong!"}
