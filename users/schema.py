import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery


class AuthMutations(graphene.ObjectType):
    register = mutations.Register.Field()



class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)