import React, { useState } from "react";
import COLORS from "../assets/colors";
import {
  View,
  Text,
  Image,
  StyleSheet,
  Switch,
} from "react-native";

export default function AreaCard({ image1, image2, description, token }) {
  const [isEnabled, setIsEnabled] = useState(true);

  const toggleSwitch = () => setIsEnabled((previousState) => !previousState);

  return (
    <View style={styles.cardContainer}>
      <View style={styles.imagesContainer}>
        <Image source={image1} style={styles.image} />
        <Image source={image2} style={styles.image} />
      </View>
      <Text style={styles.description}>{description}</Text>
      <Switch
        trackColor={{ false: COLORS.dark, true: COLORS.neutral }}
        thumbColor={isEnabled ? COLORS.primary : COLORS.dark}
        ios_backgroundColor={COLORS.dark}
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
