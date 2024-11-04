from .base import *


class MentorApplication(
    BaseApplication,
):

    valid = models.BooleanField(default=False)
    type_of_helper = models.CharField(max_length=100, null=True, blank=True, choices=TYPE_OF_HELPER_CHOICES)
    status = models.CharField(max_length=50, default=APP_CONFIRMED)  
    
    def can_be_edit(self, app_type="M"):
        return self.status in [APP_PENDING, APP_DUBIOUS] and not utils.is_app_closed(app_type)
