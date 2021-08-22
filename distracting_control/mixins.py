#!/usr/bin/env python3

class SaveMixin:
    def save_state(self, filepath):
        import cloudpickle
        # Get all variables in a class
        state = {key:val for key, val in vars(self).items() if not callable(getattr(self, key)) and not key.startswith('__')}
        state.pop('_env')
        with open(filepath, 'wb') as f:
            cloudpickle.dump(state, f)
