from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from launchdarkly_drf import has_feature


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(["GET"])
def test_view(request: Request) -> Response:
    value = has_feature("TEST_FLAG", request=request)
    return Response(f"Test flag value: {value=}")
