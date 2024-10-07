from enum import Enum


class UserDefinedProtocolNumber(Enum):
    # 예약된 정보 (1, 2, 11, 12, 13, 21) 을 제외하고 사용하도록 함
    FIRST_USER_DEFINED_FUNCTION_FOR_TEST = 5
    SI_AGENT_OPERATION = 3773
    WATCHDOG_OPERATON = 3377
    GET_CURRENT_PHASE = 77
    GET_BACKLOGS = 7733

    @classmethod
    def hasValue(cls, value):
        return any(value == item.value for item in cls)
