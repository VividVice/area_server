import { useState } from "react";
import { useNavigation } from "@react-navigation/native";
import axios from "axios";
import ServerUrl from "./BaseUrl";

const useRegisterLogic = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [usernameValidated, setUsernameValidated] = useState(true);
  const [passwordValidated, setPasswordValidated] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const navigation = useNavigation();

  const handleRegister = () => {
    navigation.navigate("Login");
  };

  const handleConnect = async () => {
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
        `${ServerUrl()}/register`,
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

      if (response.status === 201) {
        console.log("Register successful!", response.data);
        navigation.navigate("Login");
      } else {
        console.log("Register failed with status:", response.status);
      }
    } catch (error) {
      console.log("Error:", error);
      if (!error.status) {
        console.log("General network error");
      }
    }
    setIsLoading(false);
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
    handleRegister,
    handleConnect,
  };
};

export default useRegisterLogic;
