import pyxel

class AnalogBinding:
    """Manages analog input binding configuration.

    Attributes:
        axis_code (int): The pyxel axis code for the analog input.
        dead_zone (float): The dead zone threshold (0.0 to 1.0).
        invert (bool): Whether to invert the input value.
    """
    def __init__(self, axis_code: int, dead_zone: float = 0.2, invert: bool = False):
        """Initialize analog binding.

        Args:
            axis_code: The pyxel axis code (e.g., GAMEPAD1_AXIS_LEFTX).
            dead_zone: Dead zone threshold, defaults to 0.2 (20%).
            invert: Whether to invert the axis value.
        """
        self.axis_code = axis_code
        self.dead_zone = max(0.0, min(1.0, dead_zone))
        self.invert = invert

    def process_input(self) -> float:
        """Process the analog input with dead zone.

        Returns:
            float: Processed analog value between -1.0 and 1.0.
        """
        raw_value = pyxel.btnv(self.axis_code) / 32767.0

        if abs(raw_value) < self.dead_zone:
            return 0.0

        normalized = (abs(raw_value) - self.dead_zone) / (1.0 - self.dead_zone)
        normalized = max(-1.0, min(1.0, normalized)) * (1 if raw_value > 0 else -1)

        return -normalized if self.invert else normalized
