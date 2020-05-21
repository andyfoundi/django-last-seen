from last_seen.models import user_seen


class LastSeenMiddleware:
    """
        Middlewate to set timestampe when a user
        has been last seen
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_seen(request.user)
        response = self.get_response(request)
        return response
