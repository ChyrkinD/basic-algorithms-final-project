class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Функція для реверсування однозв'язного списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція для сортування злиттям однозв'язного списку
def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

# Функція для знаходження середини списку
def get_middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Функція для об'єднання двох відсортованих списків
def merge(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next