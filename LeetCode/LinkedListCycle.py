from typing import Optional


class ListNode:
    def __init__(self, val=0, name="", next=None):
        self.next = next
        self.val = val
        self.name = name


def has_cycle(head: Optional[ListNode]) -> bool:
    slow_pointer = head
    fast_pointer = head
    while slow_pointer.next is not None and fast_pointer.next is not None:
        if slow_pointer.val > fast_pointer.val or fast_pointer is fast_pointer.next.next:
            return True
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return False


def main():
    node17 = ListNode(17, "17")
    node16 = ListNode(16, "16", node17)
    node15 = ListNode(15, "15", node16)
    node14 = ListNode(14, "14", node15)
    node13 = ListNode(13, "13", node14)
    node12 = ListNode(12, "12", node13)
    node11 = ListNode(11, "11", node12)
    node17.next = node12
    print(has_cycle(node16))


if __name__ == '__main__':
    main()
