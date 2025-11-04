import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import DeployedApp
from users.models import User


class AppNode(DjangoObjectType):
    class Meta:
        model = DeployedApp
        fields = ('app_id', 'active', 'owner')
        interfaces = (relay.Node, )
        name = 'App'


    @classmethod
    def get_node(cls, info, id):
        if id.startswith("app_"):
            return DeployedApp.objects.filter(app_id=id).first()
        return DeployedApp.objects.filter(pk=pk).first()


    def resolve_id(self, info):
        return self.app_id


    def resolve_active(self, info):
        return self.active
