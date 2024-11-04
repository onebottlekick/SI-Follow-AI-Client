from user_defined_protocol.protocol import UserDefinedProtocolNumber


class LlamaGetCurrentPhaseResponse:
    def __init__(self, responseData):
        self.protocolNumber = UserDefinedProtocolNumber.LLaMA_GET_CURRENT_PHASE.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"LlamaGetCurrentPhaseResponse({self.__dict__})"
