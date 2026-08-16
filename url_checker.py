from urllib.parse import urlparse
import ipaddress
import re


def analyze_url(url):
    # Parse the URL
    parsed = urlparse(url)

    # Extract domain
    domain = parsed.hostname

    # Check HTTPS
    uses_https = parsed.scheme.lower() == "https"

    # Check URL length
    url_length = len(url)
    is_long_url = url_length > 100

    # Check whether domain is an IP address
    has_ip = False

    if domain:
        try:
            ipaddress.ip_address(domain)
            has_ip = True
        except ValueError:
            has_ip = False

    # Suspicious keywords
    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "password",
        "bank",
        "update",
        "secure"
    ]

    found_keywords = []

    lower_url = url.lower()

    for keyword in suspicious_keywords:
        if keyword in lower_url:
            found_keywords.append(keyword)

    # Check number of subdomains
    subdomain_count = 0

    if domain:
        parts = domain.split(".")

        if len(parts) > 2:
            subdomain_count = len(parts) - 2

    excessive_subdomains = subdomain_count > 3

    # Check suspicious URL characters
    has_suspicious_characters = bool(
        re.search(r"[@]", url)
    )

    # Return analysis result
    return {
        "url": url,
        "domain": domain,
        "uses_https": uses_https,
        "url_length": url_length,
        "is_long_url": is_long_url,
        "has_ip": has_ip,
        "found_keywords": found_keywords,
        "subdomain_count": subdomain_count,
        "excessive_subdomains": excessive_subdomains,
        "has_suspicious_characters": has_suspicious_characters
    }