import os

import nuke

import tank
from tank import Hook
from tank import TankError


class PreSubmitHook(Hook):
    def execute(self, **kwargs):

        scene_name = nuke.root()['name'].value()
        if not scene_name:
            raise TankError("Please Save your file before Rendering")

        jobname = os.path.splitext(os.path.basename(scene_name))[0]

        start = nuke.root()['first_frame'].value()
        end = nuke.root()['last_frame'].value()

        attrs = [
            {'name': 'work_file', 'value': str(scene_name), 'title': 'Work File'},

            {'name': 'start', 'value': start, 'title': 'Start Frame'},
            {'name': 'end', 'value': end, 'title': 'End Frame'},
            {'name': 'by', 'value': 1, 'title': 'By Frame'},

            {'name': 'jobname', 'value': str(jobname), 'title': 'Job Name'},
            {'name': 'queue', 'value': ['high', 'mid', 'low'], 'title': 'Queue'},
            {'name': 'submit', 'value': True, 'title': 'Submit Job'}
        ]

        nuke.scriptSave()

        return attrs
