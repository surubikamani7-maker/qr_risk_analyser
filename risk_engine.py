# ==========================================
# QR RISK ENGINE
# ==========================================

def calculate_risk(url_result, blacklist_result, whitelist_result):

    score = 0
    reasons = []

    # ==========================================
    # 1. BLACKLIST CHECK
    # ==========================================

    if blacklist_result.get("blacklisted", False):
        score += 60
        reasons.append("Blacklisted domain")

    # ==========================================
    # 2. HTTPS CHECK
    # ==========================================

    if not url_result.get("uses_https", False):
        score += 10
        reasons.append("HTTP connection")

    # ==========================================
    # 3. LONG URL CHECK
    # ==========================================

    if url_result.get("is_long_url", False):
        score += 5
        reasons.append("Very long URL")

    # ==========================================
    # 4. SUSPICIOUS KEYWORD CHECK
    # ==========================================

    if url_result.get("found_keywords"):
        score += 5
        reasons.append("Suspicious keyword found")

    # ==========================================
    # 5. SUSPICIOUS DOMAIN CHECK
    # ==========================================

    suspicious_domain = (
        url_result.get("has_ip", False)
        or url_result.get("excessive_subdomains", False)
        or url_result.get("has_suspicious_characters", False)
    )

    if suspicious_domain:
        score += 20
        reasons.append("Suspicious domain")

    # ==========================================
    # 6. WHITELIST CHECK
    # ==========================================

    if whitelist_result.get("whitelisted", False):
        reasons.append("Domain found in whitelist")

    # ==========================================
    # MAXIMUM SCORE = 100
    # ==========================================

    score = min(score, 100)

    # ==========================================
    # 7. FINAL STATUS
    # ==========================================

    if score <= 29:
        status = "SAFE"

    elif score <= 59:
        status = "SUSPICIOUS"

    else:
        status = "DANGEROUS"

    # ==========================================
    # 8. FINAL RESULT
    # ==========================================

    return {
        "risk_score": score,
        "risk_percentage": f"{score}%",
        "status": status,
        "reasons": reasons
    }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    test_url_result = {
        "uses_https": False,
        "is_long_url": True,
        "has_ip": False,
        "found_keywords": ["login"],
        "excessive_subdomains": False,
        "has_suspicious_characters": False
    }

    test_blacklist_result = {
        "blacklisted": False,
        "domain": "example.com",
        "reason": None
    }

    test_whitelist_result = {
        "whitelisted": False,
        "domain": "example.com"
    }

    result = calculate_risk(
        test_url_result,
        test_blacklist_result,
        test_whitelist_result
    )

    print("================================")
    print("       QR RISK ANALYSIS")
    print("================================")
    print("Risk Score      :", result["risk_score"])
    print("Risk Percentage :", result["risk_percentage"])
    print("Status          :", result["status"])
    print("Reasons         :", result["reasons"])
    print("================================")
