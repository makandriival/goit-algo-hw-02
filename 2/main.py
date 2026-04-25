from collections import deque
from constants import strings
import asyncio
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def is_palindrome(s):
    is_palindrome = True
    cleaned = ''.join(s.split()).lower()
    d = deque(cleaned)
    
    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        print(f"Comparing '{left}' and '{right}'")
        if left != right:
            is_palindrome = False
            break
    
    if is_palindrome:
        return f"{Fore.GREEN}'{s}' is a palindrome.{Style.RESET_ALL}"

    return f"{Fore.RED}'{s}' is not a palindrome.{Style.RESET_ALL}"

async def loop():
    for str in strings:
        print("="*50)
        print(f"Checking if '{str}' is a palindrome...")
        print(is_palindrome(str))
        await asyncio.sleep(1)
        
asyncio.run(loop())
