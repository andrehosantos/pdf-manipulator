from utils.collatepdf import CollatePDFs as pdfcollator
from utils.intervals import Intervals as interhandler
from utils.items import ProcessItems as itemshandler
from utils.processfile import ProcessFile as filehandler
"""
This program changes the content of a base Postscript file, converts it to PDF,
create collection of PDFs and prepare the collections to printing.  
Requires the linux packages 'ps2pdf' and 'pdfjam'.
"""


def main():
    key = '_num'
    start_num = 1357701
    end_num = 1358300
    sets = 500

    in_file = './retinoides/retinoides.ps'
    file = filehandler(in_file, key)
    (lines, file_contents) = file.get_file_info()

    intervals = interhandler(start_num, end_num, sets)
    subintervals = intervals.prepare_intervals()

    items = itemshandler(key, file_contents, lines, subintervals)
    items.process_items()

    pdfcollator.collate(subintervals)


if __name__ == '__main__':
    main()
