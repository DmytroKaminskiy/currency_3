from annoying.functions import get_object_or_None

from django.db.models import F

from account.models import URLTracker


class URLTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        url_tracker, created = URLTracker.objects.get_or_create(path=request.path)
        if not created:
            url_tracker.counter = F('counter') + 1
            url_tracker.save(update_fields=('counter', ))

        return response
