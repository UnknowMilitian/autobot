from aiogram.fsm.state import State, StatesGroup


class RegistrationStateGroup(StatesGroup):
    language = State()
    phone = State()
    name = State()


class MenuStateGroup(StatesGroup):
    new_detection = State()
    active_detections = State()
    settings = State()
