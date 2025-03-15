# Botium Toys Security Audit  

## Overview  
This repository documents a **security audit** for Botium Toys, a fictional U.S.-based toy company (Google Cybersecurity Professional Certificate). The audit assesses the company's current security posture, identifies risks, and provides recommendations for improving controls and compliance with frameworks like **NIST CSF**, **PCI DSS**, and **GDPR**.  

## Key Deliverables  
1. **Scope, Goals, and Risk Assessment Report**: Outlines the audit's scope, goals, and identified risks.  
2. **Controls and Compliance Checklist**: Evaluates existing controls and compliance with industry standards.  

## Repository Structure  
- `audit-report/`: Contains the audit report and checklist.  
- `scripts/`: Example scripts demonstrating tools for risk analysis and password validation.  

## How to Use  
1. Review the `audit-report/` folder for the full audit documentation.  
2. Explore the `scripts/` folder for example tools that could be used to address identified issues:  

### Scripts  
#### `risk-calculator.py`  
Calculates risk scores and classifies them as **Low**, **Medium**, or **High** based on likelihood and impact.  

#### `password-checker.py`
Validates password complexity requirements and rates password strength.

- Requirements:
- At least 8 characters long.
- Contains at least one uppercase letter.
- Contains at least one digit.
- Contains at least one special character (!@#$%^&*).
