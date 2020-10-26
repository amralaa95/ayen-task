# from __future__ import annotations
from abc import ABC, abstractmethod


class FileFactory(ABC):
    @abstractmethod
    def search(self, file_path, search_term, **kwargs):
        pass
