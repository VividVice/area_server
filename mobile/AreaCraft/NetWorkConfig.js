import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';
import COLORS from '../assets/colors';
import { useNavigation } from '@react-navigation/native';
import { setServerUrl } from './Logics/BaseUrl';

export default function Network() {
  const [network, setnetwork] = useState("");
  const [isSaved, setIsSaved] = useState(false);
  const navigation = useNavigation();

  useEffect(() => {
    if (isSaved) {
      setServerUrl(network);
      navigation.navigate("Login");
    }
  } , [isSaved])

  return (
    <View style={styles.container}>
      <Text style={{ color: COLORS.white, fontSize: 20, fontFamily: "custom-font" }}>Network</Text>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="network"
          placeholderTextColor="#909090"
          value={network}
          onChangeText={setnetwork}
        />
      </View>
      <TouchableOpacity style={{ backgroundColor: COLORS.bluetech, padding: 10, borderRadius: 5, marginTop: 20 }} onPress={() => setIsSaved(true)}>
        <Text style={{ color: COLORS.white, fontSize: 20, fontFamily: "custom-font" }}>Save</Text>
      </TouchableOpacity>
    </View>
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
  inputContainer: {
    flexDirection: "row",
    marginHorizontal: 15,
    paddingHorizontal: 10,
    alignItems: "center",
    justifyContent: "space-between",
    width: "95%",
    position: "relative",
  },
  input: {
    width: "95%",
    padding: 10,
    marginVertical: 10,
    backgroundColor: COLORS.white,
    borderRadius: 5,
    borderColor: COLORS.red,
    borderWidth: 0,
    color: "#000",
    fontFamily: "custom-font",
  },
});