from ..files_factory.pdf import PDF
from ..files_factory.power_point import PowerPoint


class FactoryFile():
    @classmethod
    def create_file_class(cls, file_type):
        if file_type == '.pdf':
            return PDF()
        elif file_type == '.pptx':
            return PowerPoint()
