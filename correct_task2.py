def count_valid_emails(emails):
    count = 0

    for email in emails:
        # Skip non-string entries
        if not isinstance(email, str):
            continue
            
        # Must have @ symbol
        if "@" not in email:
            continue
            
        # Split by @ to check structure
        parts = email.split("@")
        
        # Must have exactly 2 parts (before @ and after @)
        if len(parts) != 2:
            continue
            
        local_part, domain_part = parts
        
        # Both parts must be non-empty and no spaces allowed
        if (len(local_part) > 0 and 
            len(domain_part) > 0 and 
            " " not in email):
            count += 1

    return count
