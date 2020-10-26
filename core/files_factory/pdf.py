import pdftotext

from core.files_factory.base_file_type import FileFactory
import logging
logger = logging.getLogger(__name__)


class PDF(FileFactory):
    def search(self, file_path, search_term, **kwargs):
        try:
            with open(file_path, "rb") as f:
                pdf = pdftotext.PDF(f)
                for page in pdf:
                    if search_term in page:
                        return True
        except Exception as e:
            logger.error(f'Error while extract pdf {file_path}: {e}')
        return False
