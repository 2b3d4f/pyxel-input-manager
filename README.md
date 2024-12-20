# Pyxel Input Manager

A simple input manager for Pyxel.

## Features

- Bind keys to actions
- Easy integration with Pyxel
- Lightweight and simple to use

## Installation

You can install the Pyxel Input Manager via pip:

```sh
pip install pyxel-input-manager
```

<!-- Make sure you have Python 3.11 or higher. -->

## Demo

```sh
python -m pyxel_input_manager demo
```

or

```sh
pyxel-input-manager demo
```

## Usage

To use the Pyxel Input Manager in your Pyxel project, you can import and initialize it as follows:

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
```

<!-- ## Contributing

If you would like to contribute to this project, please feel free to submit a pull request. For major changes, please open an issue first to discuss what you would like to change. -->

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
