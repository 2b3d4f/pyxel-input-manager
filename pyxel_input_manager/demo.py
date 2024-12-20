
import pyxel
from pyxel_input_manager import InputMap, InputEvent, AnalogBinding

import math

class InputDemo:
    """Simple demo showing input manager usage."""

    def __init__(self):
        """Initialize the demo."""
        # Initialize Pyxel
        pyxel.init(160, 144, title="Input Manager Demo")

        # Create player
        self.player_x = 80
        self.player_y = 60

        # Add velocity and physics parameters
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.8
        self.friction = 0.75
        self.max_speed = 2.5

        self.setup_input()

        # Start game loop
        pyxel.run(self.update, self.draw)

    def setup_input(self):
        """Setup input mapping."""
        # Create input map with both keyboard and gamepad support
        initial_bindings = {
            # Digital inputs (keyboard)
            "move_right": [pyxel.KEY_D, pyxel.KEY_RIGHT, pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT],
            "move_left": [pyxel.KEY_A, pyxel.KEY_LEFT, pyxel.GAMEPAD1_BUTTON_DPAD_LEFT],
            "move_up": [pyxel.KEY_W, pyxel.KEY_UP, pyxel.GAMEPAD1_BUTTON_DPAD_UP],
            "move_down": [pyxel.KEY_S, pyxel.KEY_DOWN, pyxel.GAMEPAD1_BUTTON_DPAD_DOWN],

            # Analog inputs (gamepad)
            "stick_x": AnalogBinding(pyxel.GAMEPAD1_AXIS_LEFTX, dead_zone=0.2),
            "stick_y": AnalogBinding(pyxel.GAMEPAD1_AXIS_LEFTY, dead_zone=0.2, invert=True)
        }

        self.input_map = InputMap(initial_bindings)
        self.input_event = InputEvent(self.input_map)

    def update(self):
        """Update game state."""
        # Update input states
        self.input_event.update_states()

        # Calculate input direction
        input_x = 0
        input_y = 0

        # Digital input
        if self.input_event.is_action_pressed("move_right"):
            input_x += 1
        if self.input_event.is_action_pressed("move_left"):
            input_x -= 1
        if self.input_event.is_action_pressed("move_up"):
            input_y -= 1
        if self.input_event.is_action_pressed("move_down"):
            input_y += 1

        # Analog input
        input_x += self.input_event.get_analog_value("stick_x")
        input_y -= self.input_event.get_analog_value("stick_y")

        # Apply acceleration
        self.velocity_x += input_x * self.acceleration
        self.velocity_y += input_y * self.acceleration

        # Apply friction when no input
        if abs(input_x) < 0.1:
            self.velocity_x *= self.friction
        if abs(input_y) < 0.1:
            self.velocity_y *= self.friction

        # Limit maximum speed
        speed = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
        if speed > self.max_speed:
            self.velocity_x = (self.velocity_x / speed) * self.max_speed
            self.velocity_y = (self.velocity_y / speed) * self.max_speed

        # Stop completely if velocity is very low
        if abs(self.velocity_x) < 0.01:
            self.velocity_x = 0
        if abs(self.velocity_y) < 0.01:
            self.velocity_y = 0

        # Update position
        self.player_x += self.velocity_x
        self.player_y += self.velocity_y

        # Keep player in bounds - stop at walls
        if self.player_x < 0:
            self.player_x = 0
            self.velocity_x = 0
        elif self.player_x > pyxel.width - 8:
            self.player_x = pyxel.width - 8
            self.velocity_x = 0

        if self.player_y < 0:
            self.player_y = 0
            self.velocity_y = 0
        elif self.player_y > pyxel.height - 8:
            self.player_y = pyxel.height - 8
            self.velocity_y = 0

        # Exit on Q key
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        """Draw game state."""
        pyxel.cls(1)

        pyxel.rect(int(self.player_x) + 2, int(self.player_y) + 2, 8, 8, 5)

        # Draw instructions
        pyxel.text(4, 4, "WASD/Arrows: Move", 7)
        pyxel.text(4, 12, "D-Pad/L-Stick: Move", 7)
        pyxel.text(4, 20, "Q: Quit", 7)

        velocity_str = f"Vel: ({self.velocity_x:.2f}, {self.velocity_y:.2f})"
        pyxel.text(4, 32, velocity_str, 7)

        # Draw player (8x8 square)
        pyxel.rect(int(self.player_x), int(self.player_y), 8, 8, 11)


def main():
    """Entry point for CLI."""
    InputDemo()

if __name__ == "__main__":
    main()
