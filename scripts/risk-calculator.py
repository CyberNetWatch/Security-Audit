# risk-calculator.py  
def calculate_risk_score(likelihood, impact):  
    """Calculate risk score based on likelihood and impact."""  
    return likelihood * impact  

def classify_risk(score):  
    """Classify risk as Low, Medium, or High based on the score."""  
    if score <= 20:  
        return "Low"  
    elif score <= 50:  
        return "Medium"  
    else:  
        return "High"  

# Example usage  
likelihood = 8  # On a scale of 1-10  
impact = 5      # On a scale of 1-10  
risk_score = calculate_risk_score(likelihood, impact)  
risk_level = classify_risk(risk_score)  
print(f"Risk Score: {risk_score}")  
print(f"Risk Level: {risk_level}")  