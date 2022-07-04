from http import HTTPStatus

from django.views.generic import View
from django.http import JsonResponse

from django.conf import settings


class Server(View):
    def get(self, request):
        return JsonResponse({}, status=HTTPStatus.OK)

    def post(self, request):
        return JsonResponse(
            {
                'version': settings.WWT_VERSION,
                'project_name': settings.WWT_NAME
            },
            status=HTTPStatus.OK
        )
