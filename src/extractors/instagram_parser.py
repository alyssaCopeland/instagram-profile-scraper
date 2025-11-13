thonimport requests
from bs4 import BeautifulSoup

def parse_profile(url):
    """Extracts profile data from an Instagram profile URL"""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve profile at {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    profile_data = {}

    # Extracting profile information (example)
    profile_data['username'] = soup.find('meta', property='og:title')['content']
    profile_data['profile_pic_url'] = soup.find('meta', property='og:image')['content']
    profile_data['followers'] = soup.find('meta', property='og:description')['content'].split()[0]
    
    # You can extend this to extract more detailed information

    return profile_data