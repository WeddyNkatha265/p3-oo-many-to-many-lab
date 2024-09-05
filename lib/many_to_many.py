# many_to_many.py
class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]

    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise TypeError("contract must be an instance of Contract")


class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise TypeError("contract must be an instance of Contract")

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.__class__.all.append(self)
        self.author.add_contract(self)
        self.book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, target_date):
        return [contract for contract in cls.all if contract.date == target_date]
