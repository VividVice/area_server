import React from 'react';
import SpotifySubscribe from './Logics/Subscribe_spotify';
import { useRoute } from '@react-navigation/native';

export default function WebVieww() {
  const route = useRoute();
  const token = route.params.token;
  const return_destination = route.params.return_destination;

  console.log(token);
  console.log(return_destination);
  return (
    <SpotifySubscribe tokenSession={token} return_destination={return_destination} />
  )
}