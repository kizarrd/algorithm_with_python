import collections

def isPalindrome(s: str) -> bool:
    
    a_deq = collections.deque()
    
    for char in s:
        if char.isalnum():
            a_deq.append(char.lower())

    print(a_deq)
    
    for _ in range(len(a_deq)//2):
        if a_deq.popleft() != a_deq.pop():
            return False
        
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))