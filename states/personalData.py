from aiogram.dispatcher.filters.state import StatesGroup,State


class PersonalData(StatesGroup):
    fullname = State()
    phone = State()
    course_name = State()
    murojat_kimga = State()
    murojat = State()
    fullbutton = State()
    Confirm = State()