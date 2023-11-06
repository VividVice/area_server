import React, { useState, useEffect } from 'react';
import GithubOauth from './Logics/GithubOauth';
import { useNavigation, useRoute } from "@react-navigation/native";

export default function Gotogith() {
  const [token, setToken] = useState(null);
  const navigation = useNavigation();

  useEffect(() => {
    if (token) {
      console.log(token);
      navigation.navigate('Dashboard', { token: token });
    }
  }, [token, navigation]);

  if (!token) {
    return <GithubOauth SetTokenSession={setToken} />;
  }

  return null;
}
