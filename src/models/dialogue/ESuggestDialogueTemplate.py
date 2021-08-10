from src import DialogueTemplateBuilder
from . import DialogueTemplate
from src.constants import *
import copy

class ESuggestDialogueTemplate(DialogueTemplate):

    def __init__(self, id=-1, template=[], relation=[], blanks=[], nodes=[], dependent_nodes=[]):
        DialogueTemplate.__init__(self, id, DIALOGUE_TYPE_E_SUGGEST, template, relation, blanks, nodes, dependent_nodes);


    def fill_blanks(self, world, subj, lowest_perma):
        response = self.template
        # subj = 'Activity'

        response = [x.replace("1", subj) for x in response]     

        return response

    def get_usable_templates(self):
        # check if it has usable templates
        return []

    def get_template_to_use(self):
        # check if it has usable templates
        return []
