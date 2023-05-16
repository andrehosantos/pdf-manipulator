import array
import os
import subprocess


class ProcessFile:
    """
    Performs the creation or modification of files.
    Requires the 'ps2pdf' linux package.
    """

    def __init__(
            self,
            file: str = "",
            key: str = ""
    ):
        self.filename = file
        self.key = key

    def get_file_info(self):
        """
        Get the base file contents and line indices needed for modification.
        """
        line_numbers = []
        contents = []
        with open(self.filename, 'r', encoding='latin-1') as gs_file:
            for index, line in enumerate(gs_file):
                contents.append(line)
                if self.key in line:
                    line_numbers.append(index)
        return line_numbers, contents

    @staticmethod
    def save_file(filename: str, contents: array.array):
        """
        Save the file to disk
        """
        with open(filename, 'w') as out_file:
            for line in contents:
                out_file.write(line)

    @staticmethod
    def convert_to_pdf(ps_file: str, pdf_file: str):
        """
        Convert a Postscript file to a PDF file using the ps2pdf linux package.
        """
        subprocess.run(["ps2pdf", "-dPDFX=true", ps_file, pdf_file])
        os.remove(ps_file)

    @staticmethod
    def replace_text(
        contents: list,
        lines_to_change: list[int],
        replacements: list[str]
    ) -> list:
        """
        Replace the content of indicated lines in base file with new content.
        """
        old_text, new_text = replacements
        for line in lines_to_change:
            line_content = contents[line]
            new_line_content = line_content.replace(old_text, new_text)
            contents[line] = new_line_content
        return contents
