from src import DialogueTemplateBuilder
from . import DialogueTemplate
from src.constants import *
import copy

class EEmphasisDialogueTemplate(DialogueTemplate):

    def __init__(self, id=-1, template=[], relation=[], blanks=[], nodes=[], dependent_nodes=[]):
        DialogueTemplate.__init__(self, id, DIALOGUE_TYPE_E_EMPHASIS, template, relation, blanks, nodes, dependent_nodes);

    def fill_blanks(self, curr_emotion_event):
        if v_mode:
            print("curr perma: ", curr_emotion_event)
            response = copy.deepcopy(self.template)

            for i in range(len(self.nodes)):
                to_insert = ""
                curr_index = response.index(self.nodes[i])
                if self.blanks[i] == 'Wellbeing':
                    to_insert = curr_emotion_event
                response[curr_index] = to_insert
        else:
            print("curr emotion: ", curr_emotion_event.emotion)
            response = copy.deepcopy(self.template)

            for i in range(len(self.nodes)):
                to_insert = ""
                curr_index = response.index(self.nodes[i])
                if self.blanks[i] == 'Emotion':
                    to_insert = curr_emotion_event.emotion
                response[curr_index] = to_insert
        return response

    def get_usable_templates(self):
        # check if it has usable templates
        return []

    def get_template_to_use(self):
        # check if it has usable templates
        return []
