import pyxel
from .input_types import InputType
from .input_map import InputMap

class InputEvent:
    """Manages input states and events."""

    def __init__(self, input_map: InputMap):
        """Initialize the InputEventManager.

        Args:
            input_map: InputMap instance containing key bindings.
        """
        self._input_map = input_map
        self._previous_states = {k: False for k in input_map._bindings}
        self._current_states = {k: False for k in input_map._bindings}
        self._analog_values = {}

    def update_states(self):
        """Update input states for the current frame."""
        self._previous_states = self._current_states.copy()

        for action, binding in self._input_map._bindings.items():
            if self._input_map.get_input_type(action) == InputType.DIGITAL:
                self._current_states[action] = any(pyxel.btn(key) for key in binding)
            else:  # ANALOG
                value = binding.process_input()
                self._analog_values[action] = value
                self._current_states[action] = abs(value) > 0.0

    def is_action_pressed(self, action: str) -> bool:
        """Check if an action is currently being held."""
        return self._current_states.get(action, False)

    def is_action_just_pressed(self, action: str) -> bool:
        """Check if an action was just pressed this frame."""
        return (self._current_states.get(action, False) and
                not self._previous_states.get(action, False))

    def is_action_just_released(self, action: str) -> bool:
        """Check if an action was just released this frame."""
        return (not self._current_states.get(action, False) and
                self._previous_states.get(action, False))

    def get_analog_value(self, action: str) -> float:
        """Get the current analog value for an action."""
        return self._analog_values.get(action, 0.0)

    def reset_states(self):
        """Reset all input states."""
        self._previous_states = {k: False for k in self._input_map._bindings}
        self._current_states = {k: False for k in self._input_map._bindings}
        self._analog_values.clear()
