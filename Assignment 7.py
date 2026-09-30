import re

# Sample text
text = """
Contact us at studentsection@gmail.com for more information.
You can also email admin@123college.edu or support123@yahoo.com.
"""

# Regular expression pattern for email
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the email addresses
print("Email addresses found:")
for email in emails:
    print(email)


"""

Email addresses found:
studentsection@gmail.com
admin@123college.edu
support123@yahoo.com

"""
