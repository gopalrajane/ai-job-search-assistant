import re
from typing import List, Dict, Set
import logging

logger = logging.getLogger(__name__)

class PromptInjectionDetector:
    """Detect and prevent prompt injection attacks"""
    
    DANGEROUS_PATTERNS = [
        r"ignore\s+previous",
        r"forget\s+about",
        r"disregard\s+",
        r"new\s+instruction",
        r"system\s+prompt",
        r"hidden\s+message",
        r"secret\s+prompt",
        r"override\s+",
        r"bypass\s+",
        r"(<!--.*?-->|\{\{.*?\}\}|\[\[.*?\]\])",  # Comments and templates
    ]
    
    @staticmethod
    def detect(text: str) -> tuple[bool, str]:
        """Detect if text contains prompt injection patterns"""
        text_lower = text.lower()
        
        for pattern in PromptInjectionDetector.DANGEROUS_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                logger.warning(f"Prompt injection detected: {pattern}")
                return True, f"Detected suspicious pattern: {pattern}"
        
        return False, ""
    
    @staticmethod
    def sanitize(text: str) -> str:
        """Remove or neutralize potentially dangerous patterns"""
        sanitized = text
        for pattern in PromptInjectionDetector.DANGEROUS_PATTERNS:
            sanitized = re.sub(pattern, "", sanitized, flags=re.IGNORECASE)
        return sanitized.strip()

class PIIRedaction:
    """Redact Personally Identifiable Information"""
    
    # Patterns for various PII
    PATTERNS = {
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
        "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
        "credit_card": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
        "date_of_birth": r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b",
        "address": r"\b\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)",
    }
    
    @staticmethod
    def redact(text: str) -> tuple[str, Dict[str, List[str]]]:
        """Redact PII from text"""
        redacted_text = text
        detected_pii = {}
        
        for pii_type, pattern in PIIRedaction.PATTERNS.items():
            matches = re.findall(pattern, text)
            if matches:
                detected_pii[pii_type] = matches
                redacted_text = re.sub(pattern, f"[{pii_type.upper()}_REDACTED]", redacted_text)
                logger.warning(f"PII redacted: {pii_type}")
        
        return redacted_text, detected_pii
    
    @staticmethod
    def mask_email(email: str) -> str:
        """Mask email address"""
        parts = email.split("@")
        if len(parts) == 2:
            user, domain = parts
            masked_user = user[0] + "*" * (len(user) - 2) + user[-1] if len(user) > 2 else "*"
            return f"{masked_user}@{domain}"
        return email

class ScamDetector:
    """Detect potentially fraudulent job postings"""
    
    SCAM_KEYWORDS = [
        "guaranteed", "earn money fast", "no experience needed",
        "work from home money", "secret", "work from home with no experience",
        "make money instantly", "passive income", "nigerian prince",
        "wire transfer", "gift card", "bitcoin", "cryptocurrency",
        "upfront payment", "processing fee", "no interview"
    ]
    
    SUSPICIOUS_SALARY_PATTERNS = [
        r"\$\d{6,}",  # Unusually high salary
        r"unlimited\s+income",
        r"\$\d+\s+per\s+day",
    ]
    
    @staticmethod
    def is_likely_scam(job_title: str, job_description: str, company: str) -> tuple[bool, List[str], float]:
        """Detect if job posting is likely a scam"""
        risk_factors = []
        score = 0.0
        
        description_lower = job_description.lower()
        title_lower = job_title.lower()
        
        # Check for scam keywords
        for keyword in ScamDetector.SCAM_KEYWORDS:
            if keyword in description_lower or keyword in title_lower:
                risk_factors.append(f"Contains keyword: {keyword}")
                score += 0.15
        
        # Check for suspicious salary patterns
        if re.search(r"\d{6,}", job_description):
            risk_factors.append("Unusually high salary mentioned")
            score += 0.25
        
        # Check for poor grammar (common in scams)
        if len(re.findall(r"\s{2,}", job_description)) > len(job_description) * 0.02:
            risk_factors.append("Excessive whitespace (possible copy-paste)")
            score += 0.1
        
        # Check for generic company name
        if len(company) < 2:
            risk_factors.append("Suspicious company name")
            score += 0.15
        
        return score > 0.5, risk_factors, min(score, 1.0)

class AuditLogger:
    """Log security-relevant events"""
    
    @staticmethod
    def log_event(
        db,
        user_id: int,
        action: str,
        resource_type: str,
        resource_id: int = None,
        details: dict = None,
        ip_address: str = None,
        user_agent: str = None
    ):
        """Log security event to database"""
        from app.models import AuditLog
        
        audit_log = AuditLog(
            user_id=user_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            details=details or {},
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        db.add(audit_log)
        db.commit()
        logger.info(f"Audit log: {action} on {resource_type}")
