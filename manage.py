import sys
import os
import dotenv
from django.conf import settings
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DEBUG = True if os.environ['DEBUG'] == "True" else False
SECRET_KEY = os.environ['DEBUG']
ALLOWED_HOSTS = ['*']

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

)

def index(request):
    return HttpResponse('Hello World')


urlpatterns = [
    path('', index, name='index'),
]

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)