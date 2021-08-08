from src.knowledgeacquisition.followup import *
from src.models.dialogue import *
from src.constants import *
from src.models.dialogue.EFollowupDialogueTemplate import EFollowupDialogueTemplate


class DialogueTemplateBuilder:

   @staticmethod
   def build(id = -1, dialogue_type = "", template_string = "", relation_string = "", blank_string = "", nodes_string = "", dependent_nodes_string = ""):

      templates = str(template_string).split("_")

      relations_split = str(relation_string).split(",")
      relations = [r.strip().split(" ") for r in relations_split]

      blanks = str(blank_string).split(",")
      nodes = str(nodes_string).split(",")
      dependent_nodes = str(dependent_nodes_string).split(",")



      if dialogue_type == DIALOGUE_TYPE_PROMPT:
         return PromptDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_PUMPING_GENERAL:
         return PumpingGeneralDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)

      elif dialogue_type == DIALOGUE_TYPE_FEEDBACK:
         return FeedbackDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)

      elif dialogue_type == DIALOGUE_TYPE_HINTING:
         return HintingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)

      elif dialogue_type == DIALOGUE_TYPE_SUGGESTING:
         return SuggestingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)

      elif dialogue_type == DIALOGUE_TYPE_PUMPING_SPECIFIC:
         return PumpingSpecificDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
    
      elif dialogue_type == DIALOGUE_TYPE_FOLLOW_UP:
         return FollowUpDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
    
      #TODO: Add the suggestion_affirm here
        
      elif dialogue_type == DIALOGUE_TYPE_KNOWLEDGE_ACQUISITION_PUMPING:
         return KnowledgeAcquisitionPumpingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)


      elif dialogue_type == DIALOGUE_TYPE_INPUT_MISHEARD:
         return InputMisheardDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)


      elif dialogue_type == DIALOGUE_TYPE_C_PUMPING:
         return CPumpingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_D_CORRECTING:
         return DCorrectingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_D_PRAISE:
         return DPraiseDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_D_PUMPING:
         return DPumpingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_LABEL:
         return ELabelDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_PUMPING:
         return EPumpingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_EVALUATION:
         return EvaluationDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_RECOLLECTION:
         return RecollectionDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_END:
         return EEndDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_EMPHASIS:
         return EEmphasisDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_FOLLOWUP:
         return EFollowupDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_O_REFLECT:
         return OReflectDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_PRAISE:
         return PPraiseDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_MHBOT_CLOSING:
         return MClosingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_CLOSING_FOLLOWUP:
         return MFollowingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_MHBOT_INTRO:
         return MIntroDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_MHBOT_INTRO_FOLLOWUP:
         return IFollowupDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_MHBOT_WELCOME:
         return MWelcomeDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_ACKNOWLEDGE:
         return AcknowledgeDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_FEEDBACK:
         return EFeedbackDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_G_PRAISE:
         return GPraiseDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_COUNSELING:
         return CounselingDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_COUNSELING_FOLLOWUP:
         return CFollowupDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_FEEDBACK_Y:
         return CFeedbackyDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_FEEDBACK_N:
         return CFeedbacknDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_CARE:
         return PReflectCareDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_ENJOY:
         return PReflectEnjoyDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_MUSIC:
         return PReflectMusicDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_MUSIC_F2:
         return PReflectMusicF2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_MUSIC_POS:
         return PReflectMusicPosDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_MUSIC_NEG:
         return PReflectMusicNegDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_GRATEFUL:
         return PReflectGratefulDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_GRATEFUL_YES:
         return PReflectGratefulYesDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_GRATEFUL_NO:
         return PReflectGratefulNoDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_P_REFLECT_GRATEFUL_F2:
         return PReflectGratefulF2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_ACTIVITY:
         return EReflectActivityDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_ACTIVITY2:
         return EReflectActivity2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_PAST:
         return EReflectPastDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_PAST_F2:
         return EReflectPastF2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_NATURE:
         return EReflectNatureDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_NATURE2:
         return EReflectNature2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_E_REFLECT_EXCEL:
         return EReflectExcelDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_R_REFLECT_ENJOY:
         return RReflectEnjoyDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_R_REFLECT_FRIEND:
         return RReflectFriendDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_R_REFLECT_FRIEND2:
         return RReflectFriend2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_R_REFLECT_FRIEND2_F2:
         return RReflectFriend2F2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_M_REFLECT_ORG:
         return MReflectOrgDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_M_REFLECT_NEW:
         return MReflectNewDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_M_REFLECT_BORED:
         return MReflectOBoredDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_M_REFLECT_FRIEND:
         return MReflectFriendDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_A_REFLECT_GOAL:
         return AReflectGoalDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_A_REFLECT_GOAL2:
         return AReflectGoal2DialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_A_REFLECT_SUCCESS:
         return AReflectSuccessDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      elif dialogue_type == DIALOGUE_TYPE_A_REFLECT_ACHIEVE:
         return AReflectAchieveDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
      
      
      
      
      
      

      ##WELCOME MESSAGE
      elif dialogue_type == DIALOGUE_TYPE_EDEN_WELCOME:
         return EDENWelcomeDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)
        
      elif dialogue_type == DIALOGUE_TYPE_ORSEN_WELCOME:
         return ORSENWelcomeDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)

      else:
         return UnknownDialogueTemplate(id, templates, relations, blanks, nodes, dependent_nodes)