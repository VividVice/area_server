import React, { useState } from "react";
import COLORS from "../assets/colors";
import {
  View,
  Text,
  Image,
  TouchableOpacity,
  StyleSheet,
  Switch,
} from "react-native";
import { useNavigation } from "@react-navigation/native";
import ServerUrl from "./Logics/BaseUrl";
import TrelloSubscribe from "./Logics/Subcrpibe_trello";
import axios from "axios";


export default function AreaCard({ image1, image2, description, token }) {
  const [isEnabled, setIsEnabled] = useState(false);
  const [isgood, setIsGood] = useState(false);
  const toggleSwitch = () => setIsEnabled((previousState) => !previousState);
  const navigation = useNavigation();

  if (isgood) {
    navigation.navigate("Create", { token: token });
  }

  return (
    <View style={styles.cardContainer}>
      <View style={styles.imagesContainer}>
        <Image source={image1} style={styles.image} />
        <Image source={image2} style={styles.image} />
      </View>
      <Text style={styles.description}>{description}</Text>
      <TouchableOpacity style={styles.customButton} onPress={setIsGood}>
        <Text style={styles.buttonText}>Try it</Text>
      </TouchableOpacity>
      <Switch
        trackColor={{ false: COLORS.dark, true: COLORS.neutral }}
        thumbColor={isEnabled ? COLORS.primary : COLORS.dark}
        onValueChange={toggleSwitch}
        value={isEnabled}
        style={styles.switch}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  cardContainer: {
    flexDirection: "row",
    alignItems: "center",
    padding: 5,
    margin: 13,
    backgroundColor: COLORS.bluetech,
    borderRadius: 8,
    elevation: 3,
  },
  imagesContainer: {
    flexDirection: "row",
  },
  image: {
    width: 30,
    height: 30,
    margin: 5,
  },
  description: {
    flex: 1,
    marginLeft: 5,
    color: COLORS.dark,
    fontSize: 15,
    fontFamily: "custom-font",
  },
  button: {
    padding: 2,
    backgroundColor: "blue",
    borderRadius: 5,
  },
  buttonText: {
    color: "white",
  },
  switch: {
    transform: [{ scaleX: 0.8 }, { scaleY: 0.8 }],
    marginRight: 10,
  },
  customButton: {
    backgroundColor: COLORS.bluetechlight,
    borderRadius: 4,
    width: 50,
    height: 30,
    marginLeft: 2,
    alignItems: "center",
    justifyContent: "center",
  },
});
