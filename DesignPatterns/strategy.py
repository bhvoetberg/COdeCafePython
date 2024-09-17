import string
import random_example
from typing import List
from abc import ABC, abstractmethod


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FiloOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append((SupportTicket(customer, issue)))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(self.tickets) == 0:
            print("There are no tickets")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("====")
        print(f"Processing ticket: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print("====")





app = CustomerSupport()
app.create_ticket("John", "Some issue")
app.create_ticket("Joe", "Other issue")
app.create_ticket("Jim", "None issue")

app.process_tickets(RandomOrderingStrategy())
