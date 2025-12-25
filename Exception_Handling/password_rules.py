class WeakPasswordError(ValueError):
    def __init__(self, reasons) -> None:
        self.reasons = reasons
        super().__init__("; ".join(reasons)) #in order to join the messages inside the reasons list we use .join

def validate_password(pw: str):
    reasons = []
    pw = pw.strip()
    if not pw:
        reasons.append("Password cannot be empty")
    if (len(pw) < 8):
        reasons.append("Password must be at least 8 characters")
    # checks = [char.isupper() for char in pw]
    # has_upper = any(checks) 
    if not any(char.isupper() for char in pw): # same thing above in one line 
        reasons.append("Must include an Uppercase letter")
    if not any(char.isdigit() for char in pw):
        reasons.append("Must include a digit")
    
    if reasons: #if reasons list contain at least one reasons then raise the WeakPasswordError and include all those messages
        raise WeakPasswordError(reasons=reasons)

#testing the limits
tests = ["Abcdefgh", "Abc123def", "abcdefgh2", "", " 123aasd123", "123a1234 ", "Abc1234ba"]
for i in tests:
    try:
        validate_password(pw=i)
        print(i, "-->OK")
    except WeakPasswordError as e:
        print(i, "->", e.reasons)
    