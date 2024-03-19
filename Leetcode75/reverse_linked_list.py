from typing import Optional
from colorama import Fore, init

init(autoreset=True)

OLD_LIST = Fore.CYAN
NEW_LIST = Fore.MAGENTA


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return "->".join(result)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # At the end of the loop, prev_node will point to the new head
        return prev_node


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(OLD_LIST + f"The input linked list is : \n{ head}\n")

    original_head = head

    answer = sol.reverseList(head)

    # print(f"\nThe original linked list was: \n{original_head}")
    print(NEW_LIST + f"The reversed linked list is : \n{ answer}")
