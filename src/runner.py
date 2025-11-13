thonimport json
from extractors.instagram_parser import parse_profile
from outputs.exporters import export_to_json
from config.settings import CONFIG

def main():
    # Example Instagram profile URLs
    profile_urls = CONFIG['profile_urls']

    # Parse profiles
    profiles = []
    for url in profile_urls:
        profile_data = parse_profile(url)
        profiles.append(profile_data)
    
    # Export profiles to JSON
    export_to_json(profiles, CONFIG['output_file'])

if __name__ == "__main__":
    main()