from ringo.model.modul import ActionItem
from ringo.model.mixins import Mixin
from ringo.lib.form import get_form_config
from ringo_anonymizer import views


class Anonymizable(Mixin):
    """Mixin to anonymize other item. Anonymization means removing data
    from the item. Values which should be anonymized must be marked in
    the items form configuration with the tag "anonymize". Anonymization
    is done depended on the fields datatype:

     * Datefields will be set to the first day and month of the date.
     * All other types will be set to None

    If the anonymize tag is set on a relation the anonymization will
    proceed in the related items (currently not implemented) """

    @classmethod
    def get_mixin_actions(cls):
        actions = []
        # Add Evaluation action
        action = ActionItem()
        action.name = 'Anonymize'
        action.url = 'anonymize/{id}'
        action.icon = 'glyphicon glyphicon-eye-close'
        action.bundle = True
        actions.append(action)
        return actions

    def _get_fields_to_anonymize(self):
        """@todo: Docstring for _get_fields_to_anonymize.
        :returns: @todo

        """
        pass

    def anonymize(self):
        """Will delete marked fields in the form with the given name. If
        no name is provided then the 'create' form ist taken.

        :form: Name of the form configuration
        :returns: None

        """
        values = self.get_values()
        self.set_values(self.anonymize_values(values))

    def anonymize_values(self, values, form="create"):
        """Will return a anonymized version of the values dictionary

        :values: Dictionary with values of the item.
        :returns: Dictionary with anonymized values of the item.

        """
        formconfig = get_form_config(self, form)
        anon_values = {}
        fields = formconfig.get_fields()
        for key in fields:
            value = values.get(key)
            if not value:
                continue
            field = fields[key]
            if "anonymize" not in field.tags:
                anon_values[key] = values[key]
                continue
            # Special handling of datatypes:
            if field.type == "date":
                anon_values[key] = None
            else:
                anon_values[key] = None

        # Finally remove some global values
        for key in ["uuid"]:
            anon_values[key] = None
        return anon_values
