from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on=False) -> None:
        super().__init__(0, 0, warning_light_on)
        self.warning_light_on = warning_light_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on