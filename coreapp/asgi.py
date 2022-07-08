import os

from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter #added

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreapp.settings')

application = get_asgi_application()


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # Just HTTP for now. (We can add other protocols later.)
# })
