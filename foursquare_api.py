import requests
from config import FOURSQUARE_API_KEY, FOURSQUARE_API_VERSION
import json

CATEGORY_IDS = {
    "restaurant": "13065",
    "kafe": "13032",
    "tarihi_yer":"16020",
    "meydan":'16032'
}

class FoursquareAPI:
    def __init__(self):
        self.api_key = FOURSQUARE_API_KEY
        self.api_version = FOURSQUARE_API_VERSION
        self.base_url = "https://api.foursquare.com/v3"

    def search_places(self, query, near, category ="restaurant", limit=10):
        """
        Belirli bir konumda mekan araması yapar
        """
        headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

        category_id = CATEGORY_IDS.get(category, "13065")
        
        params = {
            "query": query,
            "near": near,
            "limit": limit,
            "categories": category_id  # Restoran kategorisi
        }
        
        try:
            print(f"API isteği gönderiliyor: {self.base_url}/places/search")
            print(f"Parametreler: {json.dumps(params, indent=2)}")
            print(f"Headers: {json.dumps(headers, indent=2)}")
            
            response = requests.get(
                f"{self.base_url}/places/search",
                headers=headers,
                params=params
            )
            
            print(f"API Yanıt Kodu: {response.status_code}")
            print(f"API Yanıt Başlıkları: {dict(response.headers)}")
            
            if response.status_code != 200:
                print(f"Hata Yanıtı: {response.text}")
                return None
                
            data = response.json()
            print(f"API Yanıtı: {json.dumps(data, indent=2)}")
            
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"API hatası: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Hata detayı: {e.response.text}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON çözümleme hatası: {str(e)}")
            print(f"Ham yanıt: {response.text}")
            return None
        except Exception as e:
            print(f"Beklenmeyen hata: {str(e)}")
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
            print(f"Mekan detayı isteniyor: {fsq_id}")
            response = requests.get(
                f"{self.base_url}/places/{fsq_id}",
                headers=headers
            )
            
            print(f"Detay API Yanıt Kodu: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Detay Hata Yanıtı: {response.text}")
                return None
                
            data = response.json()
            print(f"Detay API Yanıtı: {json.dumps(data, indent=2)}")
            
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"Detay API hatası: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Detay hata detayı: {e.response.text}")
            return None
        except json.JSONDecodeError as e:
            print(f"Detay JSON çözümleme hatası: {str(e)}")
            print(f"Detay ham yanıt: {response.text}")
            return None
        except Exception as e:
            print(f"Detay beklenmeyen hata: {str(e)}")
            return None 