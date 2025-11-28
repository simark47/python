"""
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
"""

import re

def fun(s):
    pattern = r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return re.match(pattern, s) is not None
# done


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

"""
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
"""