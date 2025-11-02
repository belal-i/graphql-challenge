import graphene
from users.schema import UserQuery, UserMutation
from deployed_apps.schema import AppQuery


class Query(UserQuery, AppQuery, graphene.ObjectType):
    node = graphene.relay.Node.Field()


class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
