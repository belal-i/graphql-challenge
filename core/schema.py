import graphene
import users.schema
import deployed_apps.schema


class Query(
    users.schema.Query,
    deployed_apps.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
