import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, KeyboardAvoidingView, Platform, ActivityIndicator, Image } from 'react-native';
import * as Font from 'expo-font';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../assets/colors';
import useRegisterLogic from './Logics/useRegisterLogic';

export default function RegisterComponent() {
  const {
    username,
    setUsername,
    password,
    setPassword,
    showPassword,
    setShowPassword,
    usernameValidated,
    passwordValidated,
    isLoading,
    handleLogin,
    handleConnect,
  } = useRegisterLogic();
  const [fontLoaded, setFontLoaded] = useState(false);

  useEffect(() => {
    async function loadFont() {
      await Font.loadAsync({
        'custom-font': require('../assets/fonts/LeagueSpartan-Bold.otf'),
        'custom-font-quicksand': require('../assets/fonts/Quicksand_Light.otf')
      });
      setFontLoaded(true);
    }

    loadFont();
  }, []);

  if (!fontLoaded) return null;

  if (isLoading) {
    return (
      <View style={styles.loaderContainer}>
        <ActivityIndicator size="large" color="#C49D83" />
      </View>
    );
  }

  return (
    <KeyboardAvoidingView
        style={styles.container}
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        keyboardVerticalOffset={Platform.OS === "ios" ? -220 : 20}
    >
      <View style={styles.container}>
        <Image
          source={require('../assets/icons/logo.png')}
          style={{ width: 168, height: 168, marginTop: -100, marginBottom: 30 }}
        />
        <View>
          <Text style={styles.appName}>AreaCraft</Text>
          <Text style={styles.slogan}>Create an account</Text>
        </View>
        <View style={styles.inputContainer}>
          <Ionicons name="person" size={24} color="#62B1BA" style={{ paddingRight: 10 }} />
          <TextInput
            style={styles.input}
            placeholder="Create Username"
            placeholderTextColor="#909090"
            value={username}
            onChangeText={setUsername}
          />
        </View>
        <View>
          {!usernameValidated && <Text testID="usernameError" style={styles.errorMessage}>Le champ est obligatoire</Text>}
        </View>
        <View style={styles.inputContainer}>
          <Ionicons name="lock-closed" size={24} color="#62B1BA" style={{ paddingRight: 10 }} />
          <TextInput
            style={[styles.input, { paddingRight: 40 }]}
            placeholder="Create Password"
            placeholderTextColor="#909090"
            value={password}
            onChangeText={setPassword}
            secureTextEntry={!showPassword}
          />
          <TouchableOpacity onPress={() => setShowPassword(!showPassword)} style={styles.eyeIcon}>
            <Ionicons name={showPassword ? 'eye-off' : 'eye'} size={24} color="black" />
          </TouchableOpacity>
        </View>
        <View>
          {!passwordValidated && <Text testID="passwordError" style={styles.errorMessage}>Ce champ est obligatoire</Text>}
        </View>
        <TouchableOpacity style={styles.customButton} onPress={handleConnect}>
          <Text style={styles.buttonText}>Create</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20
  },
  appName: {
    fontSize: 32,
    marginBottom: 7,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font'
  },
  slogan: {
    fontSize: 18,
    marginBottom: 18,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font-quicksand'
  },
  loaderContainer: {
    flex: 1,
    backgroundColor: COLORS.mediumLight,
    alignItems: 'center',
    justifyContent: 'center'
  },
  input: {
    width: '95%',
    padding: 10,
    marginVertical: 10,
    backgroundColor: COLORS.white,
    borderRadius: 5,
    borderColor: COLORS.red,
    borderWidth: 0,
    color: '#000',
    fontFamily: 'custom-font'
  },
  button: {
    marginTop: 10,
    backgroundColor: COLORS.primary,
    borderRadius: 5,
    overflow: 'hidden',
    fontFamily: 'custom-font'
  },
  errorMessage: {
    color: 'red',
    alignSelf: 'flex-start',
    marginLeft: 10
  },
  passwordContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '95%',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '95%',
    position: 'relative'
  },
  eyeIcon: {
    position: 'absolute',
    right: 10,
    top: '50%',
    transform: [{ translateY: -12 }]
  },
  customButton: {
    backgroundColor: COLORS.bluetech,
    borderRadius: 5,
    paddingVertical: 12,
    paddingHorizontal: 40,
    marginVertical: 10,
    alignItems: 'center',
    justifyContent: 'center'
  },
  buttonText: {
    color: "#F2F2F2",
    fontSize: 18,
    fontFamily: 'custom-font'
  }
});