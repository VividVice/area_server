import { useState } from "react";
import { useNavigation } from "@react-navigation/native";
import axios from "axios";
import { ServerUrl } from "./BaseUrl";

const TIMEOUT_DURATION = 10000;

const useLoginLogic = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [usernameValidated, setUsernameValidated] = useState(true);
  const [passwordValidated, setPasswordValidated] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const navigation = useNavigation();

  const handleLogin = async () => {
    setIsLoading(true);
    let isValid = true;

    if (!username.trim()) {
      setUsernameValidated(false);
      isValid = false;
    } else {
      setUsernameValidated(true);
    }

    if (!password.trim()) {
      setPasswordValidated(false);
      isValid = false;
    } else {
      setPasswordValidated(true);
    }

    if (!isValid) {
      setIsLoading(false);
      return;
    }
    console.log("Base url:", ServerUrl());
    try {
      const response = await axios.post(
        `${ServerUrl()}/login`,
        {
          username: username,
          password: password,
        },
        {
          timeout: 10000,
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.status === 200) {
        console.log("Login successful!", response.data);
        navigation.navigate("Dashboard", { token: response.data.token });
      } else {
        console.log("Login failed with status:", response.status);
      }
    } catch (error) {
      console.log("Error:", error);
    }
    setIsLoading(false);
  };

  const handleRegister = () => {
    navigation.navigate("Register");
  };

  return {
    username,
    setUsername,
    password,
    setPassword,
    showPassword,
    setShowPassword,
    usernameValidated,
    setUsernameValidated,
    passwordValidated,
    setPasswordValidated,
    isLoading,
    handleLogin,
    handleRegister,
  };
};

export default useLoginLogic;
