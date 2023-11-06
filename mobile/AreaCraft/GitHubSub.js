import React from 'react';
import GitHubSubscribe from './Logics/Subscribe_github';
import { useRoute } from '@react-navigation/native';

export default function SubGitHub() {
  const route = useRoute();
  const token = route.params.token;
  const return_destination = route.params.return_destination;

  console.log(token);
  console.log(return_destination);
  return (
    <GitHubSubscribe tokenSession={token} return_destination={return_destination} />
  )
}