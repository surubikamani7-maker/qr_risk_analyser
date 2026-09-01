def calculate_risk(url_result, blacklist_result, whitelist_result):
    score = 0
    reasons = []

    # 1. Blacklist check
    if blacklist_result:
        score += 60
        reasons.append("Blacklisted domain")

    # 2. HTTP instead of HTTPS
    if not url_result.get("uses_https", False):
        score += 10
        reasons.append("HTTP connection")

    # 3. Long URL
    if url_result.get("is_long_url", False):
        score += 5
        reasons.append("Very long URL")

    # 4. Suspicious keyword
    if url_result.get("found_keywords"):
        score += 5
        reasons.append("Suspicious keyword found")

    # 5. Suspicious domain conditions
    suspicious_domain = (
        url_result.get("has_ip", False)
        or url_result.get("excessive_subdomains", False)
        or url_result.get("has_suspicious_characters", False)
    )

    if suspicious_domain:
        score += 20
        reasons.append("Suspicious domain")

    # Maximum score should be 100
    score = min(score, 100)

    # Final status
    if score <= 29:
        status = "SAFE"
    elif score <= 59:
        status = "SUSPICIOUS"
    else:
        status = "DANGEROUS"

    # Whitelist information
    if whitelist_result:
        reasons.append("Domain found in whitelist")

    return {
        "risk_score": score,
        "risk_percentage": f"{score}%",
        "status": status,
        "reasons": reasons
    }
test_url_result = {
    "uses_https": False,
    "is_long_url": True,
    "has_ip": False,
    "found_keywords": ["login"],
    "excessive_subdomains": False,
    "has_suspicious_characters": False
}

result = calculate_risk(
    test_url_result,
    blacklist_result=False,
    whitelist_result=False
)

print(result)
