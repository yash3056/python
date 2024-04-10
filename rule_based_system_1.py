def check_discount_eligibility(age):
    if age < 18:
        return "Not eligible for discount"
    elif age >= 18 and age <= 25:
        return "Eligible for student discount"
    elif age > 65:
        return "Eligible for senior citizen discount"
    else:
        return "Eligible for regular discount"

# Test the rule-based system
age = 20
print(f"For age {age}: {check_discount_eligibility(age)}")
