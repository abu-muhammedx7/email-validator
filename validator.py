import re
import dns.resolver

def is_valid_email_format(email):
    """Check if email format is valid using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def domain_exists(email):
    """Check if the email's domain has MX records."""
    try:
        domain = email.split('@')[1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except Exception:
        return False

def is_valid_email(email):
    """Full email validation: format + domain existence."""
    return is_valid_email_format(email) and domain_exists(email)

if __name__ == "__main__":
    email = input("Enter an email to validate: ")
    if not is_valid_email_format(email):
        print("❌ Invalid email format.")
    elif not domain_exists(email):
        print("❌ Email domain does not exist.")
    else:
        print("✅ Valid and deliverable domain for this email.")
