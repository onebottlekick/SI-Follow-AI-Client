from abc import ABC, abstractmethod


class PhaseService(ABC):
    @abstractmethod
    def get_current_phase(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_backlogs(self, *args, **kwargs):
        pass