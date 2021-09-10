from src import DialogueTemplateBuilder
from . import DialogueTemplate
from src.constants import *
import random
from src.dbo.concept.DBOConceptCustom import DBOConceptCustom
from src.dbo.concept.DBOConceptGlobalImpl import DBOConceptGlobalImpl
import copy

class MPumpingDialogueTemplate(DialogueTemplate):

    def __init__(self, id=-1, template=[], relation=[], blanks=[], nodes=[], dependent_nodes=[]):
        DialogueTemplate.__init__(self, id, DIALOGUE_TYPE_M_PUMP, template, relation, blanks, nodes, dependent_nodes)


    def fill_blanks(self, world, subj, pumping_type):
        print("blanks", self.blanks)
        print("templates", self.template)
        response = self.template
        # subj = 'playing_basketball'
        # pumping_type = 'isFun'
        # lowest_perma = 'POS_M'
        
        custom_concept = DBOConceptGlobalImpl()
        concepts = []
        
        if pumping_type == 'AtPlace':
            if type(custom_concept.get_concept_by_relation(subj, 'AtLocation')) is list:
                for x in custom_concept.get_concept_by_relation(subj, 'AtLocation'):
                    concepts.append(x[3])
            else:
                concept = custom_concept.get_concept_by_relation(subj, 'AtLocation')
                concepts.append(concept)
        elif pumping_type == 'isFun':
            if type(custom_concept.get_related_concepts(subj, 'fun')) is list:
                for x in custom_concept.get_related_concepts(subj, 'fun'):
                    concepts.append(x[1])
            else:
                concept = custom_concept.get_related_concepts(subj, 'fun')
                if concept:
                    concepts.append(concept.first)

            
        response = [x.replace("1", random.choice(concepts).replace("_", " ")) for x in response]
        
        return response

    def get_usable_templates(self):
        # check if it has usable templates
        return []

    def get_template_to_use(self):
        # check if it has usable templates
        return []
