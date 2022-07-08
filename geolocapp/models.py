from django.db import models as realModels
from django.contrib.gis.db import models as realgeoModels
from django.contrib.gis.db import models as gis_models

AVAILABILITY_PRODUCT = (
    ('Stock', 'In Stock'),
    ('Out', 'Out Of Stock'),
    ('Pre', 'Pre-Order'),
)
PRODUCT_CONDITION = (
    ('Brand New', 'Brand New'),
    ('Refurbished', 'Refurbished'),
)

class Factory(realModels.Model):
    name = realModels.TextField()
    geofence = gis_models.PolygonField()

#id = realModels.UUIDField(primary_key=True, default=uuid4, editable=False)

class Bank(realgeoModels.Model):
    name = realgeoModels.CharField(max_length=20)
    address = realgeoModels.CharField(max_length=128)
    zip_code = realgeoModels.CharField(max_length=5)
    poly = realgeoModels.PolygonField()

    def __str__(self):
        return self.name 

    """
    from app.models import Bank
    from django.contrib.gis.geos import GEOSGeometry
    in shell
    polygon = GEOSGeometry('POLYGON ((-98.503358 29.335668, -98.503086 29.335668, -98.503086 29.335423, -98.503358 29.335423, -98.503358 29.335668))', srid=4326)
    bank = Bank(name='Suntrust Bank', address='144 Monsourd Blvd, San Antonio Texas, USA',zip_code='78221', poly=polygon)
    bank.save()
    """
# to store raster field
class Elevation(realgeoModels.Model):
    name = realgeoModels.CharField(max_length=100)
    rast = realgeoModels.RasterField()

    """
    Below, GDALRaster takes in the raster.tif file, reads it as a file object 
    and abstracts it into a GDALRaster object that can be stored in the model’s RasterField:

    from django.contrib.gis.gdal import GDALRaster
    rast = GDALRaster('/path/to/raster/raster.tif', write=True)
    rast.name
    /path/to/raster/raster.tif

    rast.width, rast.height # this file has 163 by 174 pixels
    (163, 174)

    topography = Elevation(name='Mount Fuji', rast=rast)
    topography.save()

    A new raster can also be created using raw data from a Python dictionary containing the 
    parameters scale, size, origin, and srid. Below, you can see how to define a new raster 
    that describes a canyon with a width and height of 10 pixels and bands which represent a 
    single layer of data in the raster:

    rst = GDALRaster({
        'width': 10, 'height': 10, 'name': 'canyon', 'srid': 4326, 
        'bands': [
            {"data": range(100)}
            ]
        })
    rst.name
    'canyon'
    topography = Elevation(name='Mount Fuji', rast=rst)
    topography.save()
    """

"""
Searching for Points in Space Using Geometry Lookups
Geometry Lookups help you find points, lines, and polygons within another geometry. 
For example, you can use geometry lookups to determine if a point lies within a polygon's surface.
First, create a Country model defined as follows:
"""

class Country(realgeoModels.Model):
    name = realgeoModels.CharField(max_length=50)
    area = realgeoModels.IntegerField()
    pop2005 = realgeoModels.IntegerField('Population 2005')
    fips = realgeoModels.CharField('FIPS Code', max_length=2, null=True)
    iso2 = realgeoModels.CharField('2 Digit ISO', max_length=2)
    iso3 = realgeoModels.CharField('3 Digit ISO', max_length=3)
    un = realgeoModels.IntegerField('United Nations Code')
    region = realgeoModels.IntegerField('Region Code')
    subregion = realgeoModels.IntegerField('Sub-Region Code')
    lon = realgeoModels.FloatField()
    lat = realgeoModels.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = realgeoModels.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name 

    """
    Country represents a table that stores the boundaries of world countries. 
    Next, you can use GeoDjango to check if a particular Point coordinate is stored
    in a mpoly field in one of the countries in the database:

    from app.models import Country
    from django.contrib.gis.geos import Point
    point = Point(954158.1, 4215137.1, srid=32140)
    Country.objects.filter(mpoly__contains=point)
    <QuerySet [<Country: United States>]>

    ####
    san_marino = Country.objects.get(name='San Marino')
    pnt = Point(12.4604, 43.9420) # Valdagrone, San Marino
    san_marino.mpoly.contains(pnt)
    True
    ####
    CALCULATING DISTANCE BETWEEN POINTS
    Finally, GeoDjango can be used to calculate the distance between two points. 
    Assuming you know two point coordinates and want to find the distance between them, 
    you could run the following in your Python shell:

    from django.contrib.gis.geos import GEOSGeometry
    point1 = GEOSGeometry(
        'SRID=4326;POINT(-167.8522796630859 65.55173492431641)'
        ).transform(900913, clone=True) # Tin City, Alaska
    point2 = GEOSGeometry(
        'SRID=4326;POINT(-165.4089813232422 64.50033569335938)'
        ).transform(900913, clone=True) # Nome, Alaska
    distance = point1.distance(point2) # in meters
    distance / 1000 # in Kilometers
    388.3890308954561
    This example uses the transform method to convert the Point 
    coordinates from latitude/longitude decimal degrees to metric distance
    """
"""
To illustrate a more Django-specific example, you could create a model for cities 
in the United States that looks like this:
"""

class Cities(realgeoModels.Model):
    feature = realgeoModels.CharField(max_length=20)
    name = realgeoModels.CharField(max_length=30)
    county = realgeoModels.CharField(max_length=20)
    state = realgeoModels.CharField(max_length=20)
    the_geom = realgeoModels.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name  

    """
    To calculate the distance between the cities Point Hope and Point Lay, 
    you can use the models like this:

    from app.models import Cities
    pt_hope = Cities.objects.get(name='Point Hope')
    pt_lay = Cities.objects.get(name='Point Lay')
    pt_hope_meters = pt_hope.the_geom.transform(900913, clone=True)
    pt_lay_meters = pt_lay.the_geom.transform(900913, clone=True)
    pt_hope_meters.distance(pt_lay_meters)
    594946.4349305361

    ####
    GeoDjango also provides some distance lookup functions such as distance_lt, 
    distance_lte, distance_gt, distance_gte and dwithin. For example:

    from django.contrib.gis.geos import Point
    from django.contrib.gis.measure import D
    pnt = Point(-163.0928955078125, 69.72028350830078) # Point Lay
    dist = Cities.objects.filter(the_geom__distance_lte=(pnt, D(km=7))) # find all cities within 7 kilometers of Point Lay
    dist = Cities.objects.filter(the_geom__distance_gte=(pnt, D(mi=20))) # find all cities greater than or equal to 20 miles away from Point Lay

    """   
class Shop(realgeoModels.Model):
    name = realgeoModels.CharField(max_length=100)
    location = realgeoModels.PointField()
    address = realgeoModels.CharField(max_length=100)
    city = realgeoModels.CharField(max_length=50)

class Merchandise(realModels.Model):
    name = realModels.CharField(max_length=200)
    price = realModels.FloatField()
    discount_price = realModels.FloatField(default=0)
    availability = realModels.CharField(choices=AVAILABILITY_PRODUCT, max_length=30, blank=True, null=True, default='Stock')
    product_condition = realModels.CharField(choices=PRODUCT_CONDITION, max_length=30, blank=True, null=True, default='Brand New')
    slug = realModels.SlugField(blank=True, null=False, unique=True)
    is_slider = realModels.BooleanField(default=False)
    is_featured = realModels.BooleanField(default=False)
    brand = realModels.CharField(max_length=20, blank=True, null=True, default='Home&Craft')
    create_at = realModels.DateTimeField(auto_now_add=True)
    update_at = realModels.DateTimeField(auto_now=True)


