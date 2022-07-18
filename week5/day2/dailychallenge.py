from mmap import PAGESIZE


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
print(alphabetList)
class Pagination:
    def __init__(self, items = [], pageSize = 10) -> None:
        self.items = items
        self.pageSize = pageSize
    def getVisibleItems(self):
        idx = 0
        items_shown = []
        while idx < self.pageSize:
           items_shown.append(self.items[idx])
           idx += 1
        print(items_shown)

class Two_pages(Pagination):
    pass
two_pages = Two_pages(alphabetList, 2)
two_pages.getVisibleItems()