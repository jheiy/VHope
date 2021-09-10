from src import DialogueTemplateBuilder
from . import DialogueTemplate
from src.constants import *
import random
from src.dbo.concept.DBOConceptCustom import DBOConceptCustom
from src.dbo.concept.DBOConceptGlobalImpl import DBOConceptGlobalImpl
import copy

class RAdviceDialogueTemplate(DialogueTemplate):

    def __init__(self, id=-1, template=[], relation=[], blanks=[], nodes=[], dependent_nodes=[]):
        DialogueTemplate.__init__(self, id, DIALOGUE_TYPE_R_ADVICE, template, relation, blanks, nodes, dependent_nodes)


    def fill_blanks(self, world, subj, lowest_perma):
        print("blanks", self.blanks)
        response = self.template
        # subj = 'teacher'
        # lowest_perma = 'POS_M'
        
        custom_concept = DBOConceptGlobalImpl()
        concepts = []
        for x in custom_concept.get_concept_by_relation(subj, 'CapableOf'):
            concepts.append(x[3])
            
        response = [x.replace("2", random.choice(concepts).replace("_", " ")) for x in response]        
        response = [x.replace("1", subj) for x in response]
        
        return response

    def get_usable_templates(self):
        # check if it has usable templates
        return []

    def get_template_to_use(self):
        # check if it has usable templates
        return []
