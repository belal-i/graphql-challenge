import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'plan')
        interfaces = (relay.Node, )
        name = 'User'


    @classmethod
    def get_node(cls, info, id):
        try:
            return User.objects.get(user_id=id)
        except User.DoesNotExist:
            return None


class UpgradeAccount(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserNode)


    async def mutate(root, info, user_id):
        user = await User.objects.aget(user_id=user_id)
        user.plan = 'PRO'
        await user.asave()
        return UpgradeAccount(ok=True, user=user)


class DowngradeAccount(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserNode)


    async def mutate(root, info, user_id):
        user = await User.objects.aget(user_id=user_id)
        user.plan = 'HOBBY'
        await user.asave()
        return DowngradeAccount(ok=True, user=user)


class UserMutation(graphene.ObjectType):
    upgrade_account = UpgradeAccount.Field()
    downgrade_account = DowngradeAccount.Field()
