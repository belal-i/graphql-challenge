import graphene
from graphene import relay
from users.models import User
from users.schema import UserNode, UpgradeAccount, DowngradeAccount
from deployed_apps.models import DeployedApp
from deployed_apps.schema import AppNode


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = graphene.List(UserNode)
    all_apps  = graphene.List(AppNode)

    async def resolve_all_users(root, info):
        return [user async for user in User.objects.all()]

    async def resolve_all_apps(root, info):
        return [app async for app in DeployedApp.objects.all()]


class Mutation(graphene.ObjectType):
    upgrade_account   = UpgradeAccount.Field()
    downgrade_account = DowngradeAccount.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[UserNode, AppNode])
