class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Hash set to store all the unique emails.
        uniqueEmails = set()

        for email in emails:
            # Split into two parts: local and domain.
            name, domain = email.split('@')

             # Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.', '')
                    # [0]인 이유는 +후는 ignore하기 때문

            # Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)

        return len(uniqueEmails)