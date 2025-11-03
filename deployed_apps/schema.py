import graphene
from graphene_django import DjangoObjectType

from .models import DeployedApp


class AppType(DjangoObjectType):
    class Meta:
        model = DeployedApp
        fields = ('id', 'name', 'active', 'owner')


class Query(graphene.ObjectType):
    apps = graphene.List(AppType)
    app  = graphene.Field(AppType, id=graphene.Int(required=True))

    def resolve_apps(self, info):
        return DeployedApp.objects.all()


    def resolve_app(self, info, id):
        return DeployedApp.objects.get(pk=id)
