from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from functools import reduce

from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt

from ofertas.models import *
from ofertas.serializers import *

from rest_framework import status, mixins
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView


class CategoryViewSet(ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    #authentication_classes = (JSONWebTokenAuthentication, )
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OfferReadViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferReadSerializer

class OfferWriteViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, GenericViewSet):

    """
    API endpoint that allows offers to be edited.
    """

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = Offer.objects.all()
    serializer_class = OfferWriteSerializer

class FavsByUserViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    API endpoint that allows offers to be viewed or retrieve.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserFavsSerializer


class FavsEdit(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_offer(self, pk):
        try:
            return Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            raise Http404

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id_user, id_offer, format=None):
        print("get")
        user = self.get_user(id_user)
        offer = self.get_offer(id_offer)
        user.favorites.add(offer)
        print(user, offer)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id_user, id_offer, format=None):
        print("delete")
        user = self.get_user(id_user)
        offer = self.get_offer(id_offer)
        user.favorites.remove(offer)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def offer_search(request):
    """
    List all snippets, or create a new snippet.
    """

    search = request.GET.get('search', None)
    categories = request.GET.get('category', None)

    qFilter = Q()
    if(search):
        # description or offer_name contains search
        # split the search in words, then remove the
        # words with len < 4
        words = search.split()
        words = [x for x in words if len(x) > 3]

        # create the q filter for unorder items for description field
        qDescFilter = reduce(lambda x, y: x & y, [Q(description__icontains=word) for word in words])
        # same with offer_name field
        qNameFilter = reduce(lambda x, y: x & y, [Q(offer_name__icontains=word) for word in words])

        qFilter.add( qDescFilter | qNameFilter, Q.AND)

    if categories:
        # categories equals categories
        # qFilter.add( Q(categories__iexact=categories), Q.AND)
        qFilter.add( Q(categories=categories), Q.AND)

    results = Offer.objects.filter(qFilter).order_by('pub_date')
    serializer = OfferReadSerializer(results, many=True)
    return Response(serializer.data)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
