import graphene

from .core import schemas

class Query(schemas.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)