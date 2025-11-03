import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'plan', 'apps')


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user  = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_users(self, info):
        return User.objects.all()


    def resolve_user(self, info, id):
        return User.objects.get(pk=id)


class UpgradeAccount(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int(required=True)


    def mutate(self, info, id):
        user = User.objects.get(pk=id)
        user.plan = 'PRO'
        user.save()
        return UpgradeAccount(user=user)


class DowngradeAccount(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int(required=True)


    def mutate(self, info, id):
        user = User.objects.get(pk=id)
        user.plan = 'HOBBY'
        user.save()
        return DowngradeAccount(user=user)


class Mutation(graphene.ObjectType):
    upgrade_account   = UpgradeAccount.Field()
    downgrade_account = DowngradeAccount.Field()
