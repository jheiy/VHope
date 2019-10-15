import numpy as np

from src import DEFAULT_SEED


class ContentDetermination:

    def __init__(self):
        super().__init__()
        self.move_to_execute = ""
        self.curr_event = []
        np.random.seed(DEFAULT_SEED)

    def set_state(self, move_to_execute, curr_event, usable_template_list):
        self.move_to_execute = move_to_execute
        self.curr_event = curr_event
        self.usable_template_list = usable_template_list

    def reset_state(self):
        self.move_to_execute = ""
        self.curr_event = []
        self.usable_template_list = []

    def perform_content_determination(self):
        print("FETCHING: ", self.move_to_execute)

        #choose template
        chosen_template = self.choose_template()
        print("CHOSEN TEMPLATE IS: ", chosen_template)
        print("TEMPLATE IS: ", chosen_template.template)

        #fill template to use
        if len(chosen_template.template) == 1:
            response = chosen_template.template[0]
        else:
            response = chosen_template.fill_blanks(self.curr_event)

        print("response is: ")
        print(response)
        if type(response) is not type("dump"):
            str_response = ' '.join(response)
            # TODO replace multiple occurences of spaces with only one space.
        else:
            str_response = response
        print("RESPONSE IS: ", str_response)

        self.reset_state()
        return str_response, chosen_template

    def choose_template(self):
        print("templates:")
        print(self.usable_template_list)
        return np.random.choice(self.usable_template_list)



