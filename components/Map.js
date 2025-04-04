import React from 'react';
import MapView, { Marker } from 'react-native-maps';

const Map = ({ region, places }) => {
  return (
    <MapView style={{ flex: 1 }} region={region}>
      {places.map((place, index) => (
        <Marker
          key={index}
          coordinate={{
            latitude: place.geocodes.main.latitude,
            longitude: place.geocodes.main.longitude,
          }}
          title={place.name}
          description={place.location.address}
        />
      ))}
    </MapView>
  );
};

export default Map;
