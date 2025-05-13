from foursquare_api import FoursquareAPI

def main():
    # API istemcisini oluştur
    api = FoursquareAPI()
    
    # İstanbul'da restoran ara
    results = api.search_places(
        query="restaurant",
        near="Istanbul, Turkey",
        limit=5
    )
    
    if results and 'results' in results:
        for place in results['results']:
            print(f"Mekan: {place.get('name')}")
            print(f"Adres: {place.get('location', {}).get('formatted_address')}")
            print(f"Kategori: {place.get('categories', [{}])[0].get('name')}")
            print("-" * 50)

if __name__ == "__main__":
    main() 