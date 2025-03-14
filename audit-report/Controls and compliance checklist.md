# Controls and compliance checklist

| Controls assessment | Yes/No | Comments |
| :---- | :---- | :---- |
| Least Privilege | No | Employees have unrestricted access to internal data. |
| Disaster Recovery Plans | No | No backups or recovery plans in place. |
| Password Policies | Partial | Password policy exists but lacks complexity  |
| Separation of Duties | No | Not implemented. |
| Firewall | Yes | Firewall is in place with defined security rules. |
| Intrusion Detection System (IDS) | No | No IDS installed. |
| Backups | No | No backups of critical data. |
| Antivirus Software | Yes | Installed and monitored regularly. |
| Manual Monitoring of Legacy Systems | Yes | Legacy systems are monitored but lack a regular schedule. |
| Encryption | No | Encryption not used for customer credit card data. |
| Password Management System | No | No centralized system; password resets require IT intervention. |
| Locks (Offices, Storefront, Warehouse) | Yes | Physical security is adequate. |
| CCTV Surveillance | Yes | Up-to-date and functioning. |
| Fire Detection/Prevention | Yes | Fire alarms and sprinkler systems are in place.  |

#### **Compliance Checklist**

**PCI DSS**

| Best Practice | Yes/No | Comments |
| :---- | :---- | :---- |
| Only authorized users have access to customers' credit card information. | No | All employees can access cardholder data. |
| Credit card information is stored, accepted, processed, and transmitted securely. | No | No encryption used for credit card data. |
| Implement data encryption procedures. | No | Encryption not implemented. |
| Adopt secure password management policies. | Partial | Password policy exists but lacks complexity.  |

**GDPR**

| Best Practice | Yes/No | Comments |
| :---- | :---- | :---- |
| E.U. customers' data is kept private/secured. | Partial | Privacy policies exist, but encryption is not used. |
| Notify E.U. customers within 72 hours of a breach. | Yes | Plan is in place. |
| Ensure data is properly classified and inventoried. | No | No data classification or inventory process. |
| Enforce privacy policies, procedures, and processes. | Yes | Policies exist but need better enforcement.  |

**SOC Type 1/2**

| Best Practice | Yes/No | Comments |
| :---- | :---- | :---- |
| User access policies are established. | No | No least privilege or separation of duties. |
| Sensitive data (PII/SPII) is confidential/private. | Partial | Privacy policies exist, but encryption is not used. |
| Data integrity ensures consistency, completeness, and accuracy. | Yes | IT department ensures data integrity. |
| Data is available to authorized individuals. | Yes | Availability is maintained. |

**Recommendations:**

1. **Implement Least Privilege and Separation of Duties: Restrict access to sensitive data.**  
1. **Encrypt Customer Data: Use AES-256 encryption for credit card information.**  
2. **Deploy an IDS: Monitor for suspicious activity.**  
3. **Create Disaster Recovery Plans**  
4. **Regularly back up critical data.**  
5. **Adopt a Password Management System**   
6. **Enforce strong password policies.**

