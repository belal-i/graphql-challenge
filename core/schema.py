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

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_apps(root, info):
        return DeployedApp.objects.all()


class Mutation(graphene.ObjectType):
    upgrade_account   = UpgradeAccount.Field()
    downgrade_account = DowngradeAccount.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[UserNode, AppNode])
