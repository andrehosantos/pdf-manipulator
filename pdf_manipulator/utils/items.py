import multiprocessing
import os
from utils.processfile import ProcessFile
from utils.globalvars import BASE_TMP_PATH


class ProcessItems:
    """
    A class that processes items in parallel using multiprocessing.
    """

    def __init__(
        self,
        key: str,
        file_content: list[str],
        lines_to_change: list[int],
        intervals: list[tuple[int, int]]
    ) -> None:
        self.key = key
        self.file_content = file_content
        self.lines_to_change = lines_to_change
        self.intervals = intervals

    @staticmethod
    def format_number(number: int) -> str:
        """
        Formats a number to seven digits name, e.g. 357701 => 0357701.
        """
        formatted_index = "{:08d}".format(number)
        formatted_number = formatted_index[:2] + "." + \
            formatted_index[2:5] + "." + formatted_index[5:]
        return formatted_number

    def process_items(self) -> None:
        """
        Process the items in parallel
        """
        for interval in self.intervals:
            range_init, range_end = interval
            with multiprocessing.Pool(os.cpu_count()) as p:
                p.map(self.run, range(range_init, range_end + 1))

    def run(self, index: int) -> None:
        """
        Replace contents on base Postscript file and converts it to PDF.
        """
        formatted_number = self.format_number(index)
        filename = BASE_TMP_PATH + "/" + str(index)
        out_ps_file = filename + ".ps"
        out_pdf_file = filename + ".pdf"
        replacements = [self.key, formatted_number]
        contents_copy = self.file_content.copy()
        new_contents = ProcessFile.replace_text(
            contents_copy, self.lines_to_change, replacements)
        ProcessFile.save_file(out_ps_file, new_contents)
        ProcessFile.convert_to_pdf(out_ps_file, out_pdf_file)
