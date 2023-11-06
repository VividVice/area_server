import { useRoute, useNavigation } from "@react-navigation/native";
import { useState, useEffect } from "react";
import { StyleSheet } from "react-native";
import { WebView } from "react-native-webview";
import axios from "axios";
import {ServerUrl} from "../ServerUrl";
import { View, Text } from "react-native";

// Ways to set up a service as POST request to /subscribe. expect a redirect url or an error response
// Trello
//     {
//         "service": "trello",
//         "service_args": {
//             "return_url": the url where you want to load in the front end after auth,
//             }
//     }
//     After make a get request to /trello/?access_token={the_access_token given by trello}
//     make sure you always send the header Authorization: Bearer {JWT token} with EVERY request

function getParameterByName(name, url) {
  name = name.replace(/[\[\]]/g, '\\$&');
  var regex = new RegExp('[?&#]' + name + '(=([^&#]*)|&|#|$)'),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function TrelloSubscribe({ tokenSession, return_destination }) {
  const [Isauth, setIsauth] = useState(false);
  const navigation = useNavigation();
  const [redirect_url, setRedirectUrl] = useState(null);

  useEffect(() => {
    axios
      .post(
        `${ServerUrl()}/subscribe`,
        {
          service: "trello",
          service_args: {
            return_url: "http://localhost:8081",
          },
        },
        {
          timeout: 10000,
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${tokenSession}`,
          },
        }
      )
      .then((response) => {
        setRedirectUrl(response.data.auth_url);
      })
      .catch((error) => {
        alert("Already subscribe to Trello", error);
      });
  }, []);

    useEffect(() => {
      if (Isauth) {
        navigation.navigate(return_destination, { token: tokenSession });
      }
    }, [Isauth, navigation, return_destination]);
  const sendToken = (url) => {
    // get the token form url params
    console.log("urlToken:", url);
    const token = getParameterByName("token", url);
    console.log("tokenTrello:", token);
    const response = axios.get(`${ServerUrl()}/trello/?access_token=${token}`, {
      timeout: 10000,
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${tokenSession}`,
      },
    });
    console.log(response);
  };

  const onShouldStartLoadWithRequest = (event) => {
    const { url, navigationType } = event;

    if (navigationType === "click") {
      // This is a new page load
      console.log("Navigating to new page:", url);
      setIsauth(false);
      return true;
    } else {
      // check if the redirect url is in the url
      if (url.includes("http://localhost:8081")) {
        console.log("Redirect url found in url:", url);
        sendToken(url);
        setIsauth(true);
        console.log("url:", url);
        return false;
      }
      return true;
    }
  };
  if (!redirect_url) {
    return (
      <View style={styles.fullScreenContainer}>
        <Text>Loading...</Text>
      </View>
    );
  } else if (!Isauth) {
    return (
      <WebView
        source={{ uri: redirect_url }}
        onShouldStartLoadWithRequest={onShouldStartLoadWithRequest}
      />
    );
  } else {
    return null;
  }
}

const styles = StyleSheet.create({
  fullScreenContainer: {
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(0, 0, 0, 0.5)", // Background color with transparency
    justifyContent: "center",
    alignItems: "center",
    zIndex: 999, // Set the z-index to make it appear above other content
  },
  fullScreenText: {
    color: "white",
    fontSize: 20,
  },
});

export default TrelloSubscribe;
