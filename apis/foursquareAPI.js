export const fetchPlaces = async (latitude, longitude) => {
    const FOURSQUARE_API_URL = 'https://api.foursquare.com/v3/places/search';
    const API_KEY = 'fsq3pMSHXDaePJIUWYCDgThOnaOFGIqbUjiwKGehCMVBUyA=';
  
    try {
      const response = await fetch(`${FOURSQUARE_API_URL}?ll=${latitude},${longitude}&radius=1000`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${API_KEY}`,
        },
      });
      const data = await response.json();
      return data.results;
    } catch (error) {
      console.error("Error fetching places:", error);
    }
  };
  