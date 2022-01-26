#******************************************************************************#
# Queries and Mutations Here                                                   #
#******************************************************************************#
import graphene

class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value="World"))

    @staticmethod
    def resolve_say_hello(root, info, name):
        return f"Hello {name}!"
