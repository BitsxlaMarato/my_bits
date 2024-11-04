from .base import *
from .base import _BaseApplicationForm


class MentorApplicationForm(_BaseApplicationForm):

    valid = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(),
        initial=True,
    )

    type_of_helper = forms.Select(
        choices=models.TYPE_OF_HELPER_CHOICES,
    )

    bootstrap_field_info = {
        "Informació Personal": {
            "fields": [
                {"name": "gender", "space": 12},
                {"name": "other_gender", "space": 12},
                {"name": "under_age", "space": 12},
                {"name": "type_of_helper", "space": 12},
            ],
            "description": "Ei! Ens encantaria saber una mica més sobre tu, ens ajudes?",
        },
    }

    def mentor(self):
        return True

    def get_bootstrap_field_info(self):
        fields = super().get_bootstrap_field_info()
        discord = getattr(settings, "DISCORD_HACKATHON", False)
        personal_info_fields = fields["Informació Personal"]["fields"]
        polices_fields = [
            {"name": "terms_and_conditions", "space": 12},
            {"name": "email_subscribe", "space": 12},
        ]
        if not discord:
            personal_info_fields.extend(
                [
                    {"name": "diet", "space": 12},
                    {"name": "other_diet", "space": 12},
                ]
            )
            polices_fields.append({"name": "diet_notice", "space": 12})
        # Fields that we only need the first time the hacker fills the application
        # https://stackoverflow.com/questions/9704067/test-if-django-modelform-has-instance
        if not self.instance.pk:
            fields["HackUPC Policies"] = {
                "fields": polices_fields,
                "description": '<p style="color: margin-top: 1em;display: block;'
                'margin-bottom: 1em;line-height: 1.25em;">We, Hackers at UPC, '
                "process your information to organize an awesome hackathon. It "
                "will also include images and videos of yourself during the event. "
                "Your data will be used for admissions mainly. We may also reach "
                "out to you (sending you an e-mail) about other events that we are "
                "organizing and that are of a similar nature to those previously "
                "requested by you. For more information on the processing of your "
                "personal data and on how to exercise your rights of access, "
                "rectification, suppression, limitation, portability and opposition "
                "please visit our Privacy and Cookies Policy.</p>",
            }
        return fields


    class Meta(_BaseApplicationForm.Meta):
        model = models.MentorApplication

        help_texts = {
            "gender": "This is for demographic purposes.",
            # 'degree': 'What\'s your major/degree?',
            "other_diet": "Please fill here in your dietary requirements. We want to make sure we have food for you!",
        }

        labels = {
            "gender": "Amb quin gènere t'identifiques?",
            "other_gender": "Prefereixo descriure'm",
            "diet": "Restrictions alimentàries",
            "other_diet": "Si tens alguna restricció alimentària, si us plau, especifica-la",
            "type_of_helper": "Tipus d'ajudant",
        }
