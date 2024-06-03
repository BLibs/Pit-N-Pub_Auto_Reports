# Declaring a variable to act like a switch case so the targeted email, password, recipient, and account are active
TARGET = "SELB"

# Storing the smtp information
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Host for getting emails
HOST = "imap.gmail.com"

''' Checking the target to dictate which variable values to use '''
''' All variable values have been redacted for security reasons '''
# Northside
if TARGET == "NORTH":
    EMAIL = "redacted"
    PASSWORD = "redacted"
    PATH = "redacted"
    RECIPIENT_EMAIL = "redacted"
# Selbyville
elif TARGET == "SELB":
    EMAIL = "redacted"
    PASSWORD = "redacted"
    PATH = "redacted"
    RECIPIENT_EMAIL = "redacted"
# Test
elif TARGET == "TEST":
    EMAIL = "redacted"
    PASSWORD = "redacted"
    PATH = "redacted"
    RECIPIENT_EMAIL = "redacted"
