import logging

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseNotFound

logger = logging.getLogger("django.server")


class IsOwnerMixin(UserPassesTestMixin):
    """Only load view if the current user owns the object."""
    user_field_name = 'owner'

    def test_func(self):
        # return True
        if not hasattr(self, 'get_object'):
            logger.error(
                'IsOwnerMixin applied to class "%s" without a get_object method.',
                self.__class__.__name__,
            )
            return False
        self.object = self.get_object()
        if not hasattr(self.object, self.user_field_name):
            logger.error(
                'No field "%s" available on %s, could not check for owner.',
                self.user_field_name,
                self.object.__class__.__name__,
            )
            return False
        return self.request.user == self.object.owner

    # def handle_no_permission(self):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseNotFound()
    #     else:
    #         return super()
