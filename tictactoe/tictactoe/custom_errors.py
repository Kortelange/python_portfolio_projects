class InvalidSlotError(Exception):
    def __init__(self, slot):
        self.slot = slot
        self.message = f"Slot {slot} is invalid, should be a number between 1 and 9."
        super().__init__(self.message)


class OccupiedSlotError(Exception):
    def __init__(self, slot):
        self.slot = slot
        self.message = f"Slot {slot} is already occupied."
        super().__init__(self.message)
