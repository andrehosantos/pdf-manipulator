import subprocess
from utils.globalvars import PRINT_PATH, BASE_TMP_PATH


class CollatePDFs:
    """
    A class that uses the pdfjam linux package to create collections of PDFs
    and prepare them to printing.
    Requires the 'pdfjam' linux package.
    """

    def __init__(self) -> None:
        self.file_count = 1

    def create_collection(
        self,
        subinterval: list,
        restart: bool = False,
        restart_num: int = None
    ):  # TODO: restart
        """
        Create a bash script to collate PDFs
        """
        start_num, end_num = subinterval
        numbers_list = []
        for index in range(start_num, end_num):
            if restart:
                number = "{:04d}".format(index + restart_num)
            number = "{:04d}".format(index)
            numbers_list.append(number)
        outfile = PRINT_PATH + f"/numeracao-" + \
            "{:04d}".format(self.file_count) + ".pdf"
        self.file_count += 1
        filenames = self.ordenate_collection(numbers_list)
        command = "pdfjam --nup 1x2 --papersize '{213mm,297mm}' --landscape" + \
            f" --scale 1 --noautoscale true {filenames} -o {outfile} \n"
        with open("./collate.sh", 'a') as collate_file:
            collate_file.write(command)

    def ordenate_collection(self, numbers_list: list):
        """
        Create a list of filenames that obeys a FILO queue
        """
        files = ""
        mid = len(numbers_list) // 2
        range_1 = numbers_list[0:mid][::-1]
        range_2 = numbers_list[mid:][::-1]
        for i in range(0, mid):
            file1 = self.create_filename(range_1[i])
            file2 = self.create_filename(range_2[i])
            files += file1 + file2
        return files

    @staticmethod
    def create_filename(file: str) -> str:
        """
        Generate a formatted filename
        """
        basename = BASE_TMP_PATH + "/numeracao-{0}.pdf"
        return basename.format(file)

    @staticmethod
    def collate(intervals: list):
        """
        Execute the collection of PDFs for each interval
        """
        collator = CollatePDFs()
        for interval in intervals:
            collator.create_collection(interval)
            subprocess.run(["sh", "./collate.sh"])
