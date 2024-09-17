# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, name="", next=None):
        self.val = val
        self.next = next
        self.name = name


def merge_two_lists_per_node(node_l1: Optional[ListNode], node_l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    head = dummy

    while node_l1 and node_l2:
        if node_l1.val < node_l2.val:
            head.next = node_l1
            node_l1 = node_l1.next
        else:
            head.next = node_l2
            node_l2 = node_l2.next
        head = head.next

    if node_l1:
        head.next = node_l1
    elif node_l2:
        head.next = node_l2

    return dummy.next


def main():
    node13 = ListNode(4,"13")
    node12 = ListNode(2, "12", node13)
    node11 = ListNode(1, "11", node12)
    node24 = ListNode(5, "24")
    node23 = ListNode(4, "23", node24)
    node22 = ListNode(3, "22", node23)
    node21 = ListNode(1, "21", node22)

    merged_list = merge_two_lists_per_node(node11, node21)
    while merged_list:
        print("val: ", merged_list.val)
        merged_list = merged_list.next
    print("The end")


if __name__ == '__main__':
    main()
