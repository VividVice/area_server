import React, { useState } from 'react';
import GithubOauth from './Logics/GithubOauth';

export default function Gotogith() {
  const [token, setToken] = useState("");

  return (
    <GithubOauth SetTokenSession={setToken} />
  )
}