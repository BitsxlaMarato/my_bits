from .base import *
from .base import _BaseApplicationForm


class HackerApplicationForm(_BaseApplicationForm):
    bootstrap_field_info = {
        "Informació Personal": {
            "fields": [
                {"name": "university", "space": 12},
                {"name": "degree", "space": 12},
                {"name": "fibber", "space": 12},
                {"name": "graduation_year", "space": 12},
                {"name": "gender", "space": 12},
                {"name": "other_gender", "space": 12},
                {"name": "under_age", "space": 12},
            ],
            "description": "Ei! Ens encantaria saber una mica més sobre tu, ens ajudes?",
        },
    }

    university = common_university()

    degree = forms.CharField(
        required=True,
        label="Quin grau estudies o has estudiat?",
        help_text="El nom del grau que estàs cursant o has cursat",
    )

    fibber = forms.TypedChoiceField(
        required=True,
        label="Ets estudiant de la Facultat d'Informàtica de Barcelona?",
        initial=True,
        coerce=lambda x: x == "True",
        choices=((True, "Sí"), (False, "No")),
        widget=forms.RadioSelect,
    )


    def __init__(
        self,
        data=None,
        files=None,
        auto_id="id_%s",
        prefix=None,
        initial=None,
        error_class=ErrorList,
        label_suffix=None,
        empty_permitted=False,
        instance=None,
        use_required_attribute=None,
    ):
        super().__init__(
            data,
            files,
            auto_id,
            prefix,
            initial,
            error_class,
            label_suffix,
            empty_permitted,
            instance,
            use_required_attribute,
        )


    def get_bootstrap_field_info(self):
        fields = super().get_bootstrap_field_info()
        # Fieldsets ordered and with description
        discord = getattr(settings, "DISCORD_HACKATHON", False)
        hybrid = getattr(settings, "HYBRID_HACKATHON", False)
        personal_info_fields = fields["Informació Personal"]["fields"]
        personal_info_fields.append({"name": "online", "space": 12})

        polices_fields = [
            {"name": "email_subscribe", "space": 12},
            {"name": "terms_and_conditions", "space": 12},
        ]

        if not hybrid:
            self.fields["online"].widget = forms.HiddenInput()
        
        if not discord:
            personal_info_fields.extend(
                [
                    {"name": "diet", "space": 12},
                    {"name": "other_diet", "space": 12},
                ]
            )
            polices_fields.append({"name": "diet_notice", "space": 12})

        personal_info_fields.append({"name": "discover", "space": 12})

        # Fields that we only need the first time the hacker fills the application
        # https://stackoverflow.com/questions/9704067/test-if-django-modelform-has-instance
        if not self.instance.pk:
            fields["Polítiques de BitsXLaMarato"] = {
                "fields": polices_fields,
                "description": '<p style="color: margin-top: 1em;display: block;'
                'margin-bottom: 1em;line-height: 1.25em;">Nosaltres, Hackers at UPC, '
                "processem la teva informació per a organitzar una hackathon al·lucinant. "
                "Això inclou imatges i vídeos on puguis sortir, durant l'esdeveniment. " 
                "Les teves dades es processaran majoritàriament per l'admissió i logística de l'esdeveniment. "
                "Hi ha la possibilitat que t'enviem mails respecte a altres esdeveniments similars "
                "que organitzem. Per a més informació respecte al processament de les teves dades "
                "i com exercir els teus drets d'accés, rectificació, eliminació, limitació, portabilitat, o oposició, "
                "no dubtis a revisar les nostres Polítiques de Privacitat i Cookies.</p>",
            }
        return fields

    class Meta(_BaseApplicationForm.Meta):
        model = models.HackerApplication
        extensions = getattr(settings, "SUPPORTED_RESUME_EXTENSIONS", None)

        help_texts = {
            "gender": "Aquesta informació es per motius demogràfics. Pots deixar-la en blanc si ho prefereixes.",
            "degree": "Quina carrera estudies o has estudiat en el passat?",
            "other_diet": "Si us plau, avisa'ns de les teves restriccions alimentàries! Volem fer el possible per tenir menjar per tu.",
        }

        class CustomSelect(forms.Select):
            def create_option(
                self, name, value, label, selected, index, subindex=None, attrs=None
            ):
                if index == 0:
                    attrs = {"disabled": "disabled"}
                return super().create_option(
                    name, value, label, selected, index, subindex=subindex, attrs=attrs
                )

        def clean_discover(self):
            discover = self.cleaned_data.get("discover")
            if discover == "":
                raise forms.ValidationError("Si us plau, selecciona una opció.")
            return discover

        discover_choices = (
            ("", "- Selecciona una opció -"),
            (1, "Xarxes socials de HackUPC"),
            (2, "A través de la universitat (XXSS, Emails, etc.)"),
            (3, "Amics"),
            (4, "Altres hackathons"),
            (5, "Edicions anteriors"),
            (6, "Altres"),
        )

        widgets = {
            "discover": CustomSelect(choices=discover_choices),
            "graduation_year": forms.Select(),
        }

        labels = {
            "gender": "Amb quin gènere t'identifiques?",
            "other_gender": "Prefereixo descriure'm",
            "graduation_year": "Quin any esperes graduar-te o t'has graduat?",
            "diet": "Restriccions alimentàries",
            "discover": "Com ens has conegut?",
        }
