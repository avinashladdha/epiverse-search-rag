import requests

def fetch_universe_metadata(universe = "epiverse-connect"):
    """
    Fetch metadata about packages from an R-universe repository.

    Args:
        universe (str): The name of the R-universe repository (default is "epiverse-connect").

    Returns:
        list: A list of dictionaries containing package metadata, including:
            - Package name
            - Title
            - Description
            - Logo URL
            - Website URL
            - Source repository URL
            - List of article URLs
    """

    url = f"https://{universe}.r-universe.dev/api/packages"
    headers = {"User-Agent": "epiverse-connect metadata collection script"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    package_metadata = response.json()

    processed_metadata = []
    for pkg in package_metadata:
        # We don't know if articles are hosted in a pkgdown website so we rely
        # on the rendered version hosted in our r-universe
        articles = [
            f"https://{universe}.r-universe.dev/articles/{pkg['Package']}/{vignette['filename']}"
            for vignette in pkg.get("_vignettes", [])
        ]

        url_list = [url.strip() for url in pkg.get("URL", "").split(',') if url.strip()]

        # First URL that doesn't look like a link to a GitHub repo
        docs_url = next((url for url in url_list if not url.startswith("https://github.com")), None)

        processed_metadata.append({
            "package": pkg.get("Package"),
            "title": pkg.get("Title"),
            "description": pkg.get("Description"),
            "logo": pkg.get("_pkglogo"),
            "website": docs_url,
            "source": pkg.get("RemoteUrl"),
            "articles": articles
        })

    return processed_metadata
