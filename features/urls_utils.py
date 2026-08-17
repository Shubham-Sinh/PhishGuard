from urllib.parse import urlparse


def normalize_url(url):
    """
    Normalize a URL so that:
    google.com
    http://google.com
    https://google.com

    are represented consistently.
    """

    url = str(url).strip().lower()

    if not url:
        return ""

    # Add a scheme temporarily if missing
    if "://" not in url:
        parsed = urlparse("http://" + url)
    else:
        parsed = urlparse(url)

    # Get hostname
    hostname = parsed.hostname or ""

    # Remove leading www.
    if hostname.startswith("www."):
        hostname = hostname[4:]

    # Reconstruct useful URL information
    normalized = hostname

    if parsed.path and parsed.path != "/":
        normalized += parsed.path

    if parsed.query:
        normalized += "?" + parsed.query

    return normalized