import os
import json
import requests
from config import FOURSQUARE_API_KEY, FOURSQUARE_API_VERSION

CATEGORY_IDS = {
    "restaurant": "13065",
    "kafe": "13032",
    "tarihi_yer": "16020",
    "meydan": "16032",
    "müze": "10027"
}

PHOTO_CACHE_FILE = "photo_cache.json"

def load_photo_cache():
    if os.path.exists(PHOTO_CACHE_FILE):
        try:
            with open(PHOTO_CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_photo_cache(cache_data):
    with open(PHOTO_CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=2)


CACHE_FILE = "foursquare_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache_data):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=2)

class FoursquareAPI:
    def __init__(self):
        self.api_key = FOURSQUARE_API_KEY
        self.api_version = FOURSQUARE_API_VERSION
        self.base_url = "https://api.foursquare.com/v3"

    def search_places(self, query, near, category="restaurant", limit=10):
        """
        Belirli bir konumda mekan araması yapar — önce cache kontrol edilir
        """
        cache_key = f"{query.lower()}_{near.lower()}_{category}"
        cache_data = load_cache()

        # Cache'te varsa direkt döndür
        if cache_key in cache_data:
            print(f"[CACHE] {cache_key} bulundu, API'ye gidilmiyor.")
            return cache_data[cache_key]

        # API isteği oluşturuluyor
        headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

        category_id = CATEGORY_IDS.get(category, "13065")

        params = {
            "query": query,
            "near": near,
            "limit": limit,
            "categories": category_id
        }

        try:
            print(f"[API] {self.base_url}/places/search çağrılıyor...")
            response = requests.get(
                f"{self.base_url}/places/search",
                headers=headers,
                params=params
            )

            if response.status_code != 200:
                print(f"[API HATA] {response.text}")
                return None

            data = response.json()

            # Sonucu cache'e yaz
            cache_data[cache_key] = data
            save_cache(cache_data)

            return data

        except Exception as e:
            print(f"[API HATA] {e}")
            return None

    def get_place_details(self, fsq_id):
        """
        Belirli bir mekanın detaylarını getirir
        """
        headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

        try:
            print(f"[API] Mekan detayı isteniyor: {fsq_id}")
            response = requests.get(
                f"{self.base_url}/places/{fsq_id}",
                headers=headers
            )

            if response.status_code != 200:
                print(f"[API DETAY HATA] {response.text}")
                return None

            return response.json()

        except Exception as e:
            print(f"[DETAY API HATASI] {e}")
            return None


    def get_place_photos(self, fsq_id, limit=1):
        """
        Belirli bir mekan için fotoğraf(lar) getirir — önce cache kontrol edilir
        """
        cache_data = load_photo_cache()

         # Cache kontrolü
        if fsq_id in cache_data:
           print(f"[CACHE] Fotoğraf (fsq_id={fsq_id}) cache'den alındı.")
           return cache_data[fsq_id]

        headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

        try:
            url = f"{self.base_url}/places/{fsq_id}/photos"
            params = {"limit": limit}

            print(f"[API] Fotoğraf isteniyor: {url}")
            response = requests.get(url, headers=headers, params=params)

            if response.status_code != 200:
                print(f"[API FOTOĞRAF HATASI] {response.text}")
                return []

            data = response.json()

            # Fotoğraf URL'leri oluşturuluyor
            photo_urls = []
            for photo in data:
                prefix = photo.get("prefix", "")
                suffix = photo.get("suffix", "")
                size = "original"  # istersen "300x200" gibi sabitleyebilirsin
                url = f"{prefix}{size}{suffix}"
                photo_urls.append(url)

            # Cache'e yaz
            cache_data[fsq_id] = photo_urls
            save_photo_cache(cache_data)

            return photo_urls

        except Exception as e:
            print(f"[FOTOĞRAF API HATASI] {e}")
            return []
    

if __name__ == "__main__":
    api = FoursquareAPI()

    # Test amaçlı: belirli bir mekanın fotoğrafını getir
    fsq_id = "4f5218fee4b03365338f678a"
    photos = api.get_place_photos(fsq_id)

    if photos:
        print("📸 Fotoğraf bulundu:")
        for url in photos:
            print(url)
    else:
        print("❌ Fotoğraf bulunamadı veya hata oluştu.")

