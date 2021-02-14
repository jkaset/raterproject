from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Gamer
from django.contrib.auth.models import User


class Gamers(ViewSet):
    """Level up games"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        gamers = Gamer.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(gametype__id=game_type)

        serializer = GamerSerializer(
            gamers, many=True, context={'request': request})
        return Response(serializer.data)

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    class Meta:
        model = Gamer
        fields = ('user', 'bio')
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    class Meta:
        model = User
        fields = ('first_name')
        depth = 1