import re

from common.aboutFile import file_path
from common.database import queryNoteList

if __name__ == "__main__":
 queryNoteList(file_path)





# import re
#
# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")