#!/usr/bin/env python3

class SaveMixin:
    def get_distracting_state(self):
        # Get all variables in a class
        state = {key:val for key, val in vars(self).items() if not callable(getattr(self, key)) and not key.startswith('__')}
        state.pop('_env')
        return state
