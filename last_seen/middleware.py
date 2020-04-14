# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .models import user_seen


class LastSeenMiddleware(object):
    """
        Middlewate to set timestampe when a user
        has been last seen
    """
    def process_request(self, request):
        if request.user.is_authenticated:
            user_seen(request.user)

        return None
