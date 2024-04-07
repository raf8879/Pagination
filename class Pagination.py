class Pagination:

    def __init__(self, book, elem):
        self.book = book
        self.elem = elem
        self.l = self.make_str()
        self.total_pages = len(self.l)
        self.current_page = 1

    def make_str(self):
        s, r = {}, 1
        for i in range(0, len(self.book), self.elem):
            s.setdefault(r, self.book[i:i+self.elem])
            r += 1
        return s

    def get_visible_items(self):
        return self.l[self.current_page]

    def prev_page(self):
        self.current_page = max(self.current_page - 1, 1)
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, key):
        self.current_page = max(1, min(self.total_pages, key))
        return self

    def next_page(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self


alphabet = list('abcd')

pagination = Pagination(alphabet, 4)
print(pagination.l)
pagination.next_page()
print(pagination.get_visible_items())