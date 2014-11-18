from ringo.model.modul import ActionItem
from ringo.model.mixins import Mixin
from ringo_anonymizer import views

class Anonymizable(Mixin):

    """Mixin to anonymize other items. Anonymization means removing data
    from the item."""

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


