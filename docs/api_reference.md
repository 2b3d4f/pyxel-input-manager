# Pyxel Input Manager API Reference

A flexible input management system for the Pyxel game engine that handles both digital and analog inputs.

## Core Classes

### InputType

An enumeration defining the types of input supported.

```python
class InputType(Enum):
    DIGITAL  # For button/key inputs
    ANALOG   # For analog inputs like joysticks
```

### AnalogBinding

Configures and processes analog input with dead zone handling.

#### Constructor

```python
AnalogBinding(axis_code: int, dead_zone: float = 0.2, invert: bool = False)
```

- `axis_code`: Pyxel axis code (e.g., GAMEPAD1_AXIS_LEFTX)
- `dead_zone`: Threshold for ignoring small inputs (0.0 to 1.0)
- `invert`: Whether to invert the axis value

#### Methods

- `process_input() -> float`: Returns processed analog value (-1.0 to 1.0)

### InputMap

Manages key bindings and actions for your game.

#### Constructor

```python
InputMap(initial_bindings: Optional[Dict[str, Union[List[int], AnalogBinding]]] = None)
```

#### Methods

- `add_action(action: str, bindings: List[int]) -> bool`: Add digital action
- `add_analog_action(action: str, binding: AnalogBinding) -> bool`: Add analog action
- `remove_action(action: str) -> bool`: Remove an action
- `get_bindings(action: str) -> Union[List[int], AnalogBinding]`: Get action bindings
- `set_bindings(action: str, bindings: List[int]) -> bool`: Update bindings
- `has_action(action: str) -> bool`: Check if action exists
- `clear_bindings()`: Remove all bindings
- `get_input_type(action: str) -> Optional[InputType]`: Get action's input type
- `actions -> List[str]`: Get all registered actions

### InputEvent

Handles input state tracking and event detection.

#### Constructor

```python
InputEvent(input_map: InputMap)
```

#### Methods

- `update_states()`: Update input states for current frame
- `is_action_pressed(action: str) -> bool`: Check if action is held
- `is_action_just_pressed(action: str) -> bool`: Check if action was pressed this frame
- `is_action_just_released(action: str) -> bool`: Check if action was released this frame
- `get_analog_value(action: str) -> float`: Get analog input value (-1.0 to 1.0)
- `reset_states()`: Reset all input states

## Usage Example

```python
import pyxel
from input_manager import InputMap, InputEvent, AnalogBinding

# Create input map
input_map = InputMap({
    "jump": [pyxel.KEY_SPACE],  # Digital input
    "move": AnalogBinding(pyxel.GAMEPAD1_AXIS_LEFTX)  # Analog input
})

# Create input event handler
input_event = InputEvent(input_map)

def update():
    # Update input states
    input_event.update_states()

    # Check inputs
    if input_event.is_action_just_pressed("jump"):
        player.jump()

    move_value = input_event.get_analog_value("move")
    player.move(move_value)
