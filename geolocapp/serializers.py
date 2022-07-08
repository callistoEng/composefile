from rest_framework import serializers
from .models import Factory

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"


## GEOS API
from django.contrib.gis.geos import Point, Polygon, LineString

point = Point(5, 3)
linestring = LineString((0,0), (0,50), (50,50), (50,0))
polygon = Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0,0.0)) )

