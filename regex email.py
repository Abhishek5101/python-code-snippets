import re

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']


def find_emails(string):
    return re.findall(r'[-\w+.]+@[-\w.]+', string)
