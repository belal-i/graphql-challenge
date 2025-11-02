import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import DeployedApp
from users.models import User
from graphql_relay import from_global_id


class AppNode(DjangoObjectType):
    class Meta:
        model = DeployedApp
        fields = ("app_id", "active", "owner")
        interfaces = (relay.Node, )
        name = 'App'


    @classmethod
    def get_node(cls, info, id):
        # Accept either relay global ID or `app_...` id
        if id.startswith("app_"):
            return DeployedApp.objects.filter(app_id=id).first()
        pk = from_global_id(id)[1]
        return DeployedApp.objects.filter(pk=pk).first()


    def resolve_id(self, info):
        return self.app_id


    def resolve_active(self, info):
        return self.active


class AppQuery(graphene.ObjectType):
    app = relay.Node.Field(AppNode)
    all_apps = graphene.List(AppNode)


    def resolve_all_apps(root, info):
        return DeployedApp.objects.all()
