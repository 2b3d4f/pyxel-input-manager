from typing import Dict, List, Optional, Union
from .input_types import InputType
from .input_bindings import AnalogBinding

class InputMap:
    """Manages key bindings for game actions."""

    def __init__(self, initial_bindings: Optional[Dict[str, Union[List[int], AnalogBinding]]] = None):
        """Initialize the InputMap with optional initial bindings.

        Args:
            initial_bindings: Dictionary mapping action names to either:
                            - List[int]: Digital key codes
                            - AnalogBinding: Analog input configuration
        """
        self._bindings = {}
        self._input_types = {}

        if initial_bindings:
            for action, binding in initial_bindings.items():
                if isinstance(binding, AnalogBinding):
                    self._bindings[action] = binding
                    self._input_types[action] = InputType.ANALOG
                else:
                    self._bindings[action] = binding
                    self._input_types[action] = InputType.DIGITAL

    def add_action(self, action: str, bindings: List[int]) -> bool:
        """Add a new action with its key bindings."""
        if action in self._bindings:
            return False
        self._bindings[action] = bindings.copy()
        self._input_types[action] = InputType.DIGITAL
        return True

    def add_analog_action(self, action: str, binding: AnalogBinding) -> bool:
        """Add a new analog action."""
        if action in self._bindings:
            return False
        self._bindings[action] = binding
        self._input_types[action] = InputType.ANALOG
        return True

    def remove_action(self, action: str) -> bool:
        """Remove an action and its bindings."""
        if action not in self._bindings:
            return False
        del self._bindings[action]
        del self._input_types[action]
        return True

    def get_bindings(self, action: str) -> Union[List[int], AnalogBinding]:
        """Get the key bindings for an action."""
        return self._bindings.get(action, [])

    def set_bindings(self, action: str, bindings: List[int]) -> bool:
        """Set key bindings for an action."""
        if action not in self._bindings:
            return False
        self._bindings[action] = bindings.copy()
        self._input_types[action] = InputType.DIGITAL
        return True

    def has_action(self, action: str) -> bool:
        """Check if an action exists."""
        return action in self._bindings

    def clear_bindings(self):
        """Clear all action bindings."""
        self._bindings.clear()
        self._input_types.clear()

    def get_input_type(self, action: str) -> Optional[InputType]:
        """Get the input type for an action."""
        return self._input_types.get(action)

    @property
    def actions(self) -> List[str]:
        """Get list of all registered actions."""
        return list(self._bindings.keys())
