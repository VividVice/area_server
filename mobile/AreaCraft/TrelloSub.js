import React from 'react';
import TrelloSubscribe from './Logics/Subcrpibe_trello';
import { useRoute } from '@react-navigation/native';

export default function WebVieww() {
  const route = useRoute();
  const token = route.params.token;
  const return_destination = route.params.return_destination;

  console.log(token);
  console.log(return_destination);
  return (
    <TrelloSubscribe tokenSession={token} return_destination={return_destination} />
  )
}