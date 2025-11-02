import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import User
from graphql_relay import from_global_id


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        fields = ("user_id", "username", "plan")
        interfaces = (relay.Node, )


    @classmethod
    def get_node(cls, info, id):
        # Accept either relay global ID or `u_...` id
        if id.startswith("u_"):
            return User.objects.filter(user_id=id).first()
        pk = from_global_id(id)[1]
        return User.objects.filter(pk=pk).first()


    # Override id field to use user_id
    def resolve_id(self, info):
        return self.user_id


    def resolve_username(self, info):
        return self.username


    def resolve_plan(self, info):
        return self.plan


class UserQuery(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = graphene.List(UserNode)
    get_user = graphene.Field(UserNode, user_id=graphene.String(required=True))


    def resolve_all_users(root, info):
        return User.objects.all()


    def resolve_get_user(root, info, user_id):
        return User.objects.filter(user_id=user_id).first()


class UpgradeAccount(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
    user = graphene.Field(UserNode)


    async def mutate(root, info, user_id):
        user = await User.objects.aget(user_id=user_id)
        user.plan = 'PRO'
        await user.asave()
        return UpgradeAccount(user=user)


class DowngradeAccount(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
    user = graphene.Field(UserNode)

    async def mutate(root, info, user_id):
        user = await User.objects.aget(user_id=user_id)
        user.plan = 'HOBBY'
        await user.asave()
        return DowngradeAccount(user=user)


class UserMutation(graphene.ObjectType):
    upgrade_account = UpgradeAccount.Field()
    downgrade_account = DowngradeAccount.Field()
