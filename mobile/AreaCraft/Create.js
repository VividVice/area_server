import React, { useState, Component, useEffect } from 'react';
import { View, ScrollView, Text, StyleSheet, TextInput } from 'react-native';
import COLORS from '../assets/colors';
import { TouchableOpacity } from 'react-native-gesture-handler';
import { Picker } from '@react-native-picker/picker';
import { useNavigation, useRoute } from '@react-navigation/native';
import axios from 'axios';
import ServerUrl from './Logics/BaseUrl';

export default function CreateComponent() {
  const [selectedApp1, setSelectedApp1] = useState('');
  const [selectedApp2, setSelectedApp2] = useState('');
  const [isConnectedToApp1, setIsConnectedToApp1] = useState(false);
  const [isConnectedToApp2, setIsConnectedToApp2] = useState(false);
  const [selectedItemApp1, setSelectedItemApp1] = useState('');
  const [selectedItemApp2, setSelectedItemApp2] = useState('');
  const [Option1app1, setOption1app1] = useState(null);
  const [Option2app1, setOption2app1] = useState(null);
  const [Option3app1, setOption3app1] = useState(null);
  const [Option1app2, setOption1app2] = useState(null);
  const [Option2app2, setOption2app2] = useState(null);
  const [Option3app2, setOption3app2] = useState(null);
  const [Option4app2, setOption4app2] = useState(null);
  const [userNameCallR, setUserNameCallR] = useState('');
  const [passwordNameCallR, setPasswordNameCallR] = useState('');
  const route = useRoute();
  const token = route.params.token
  const navigation = useNavigation();

  const toCamelCase = (str) => {
    return str
      .split(' ')
      .map((word, index) =>
        index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
      )
      .join('');
  };

  function handleConnectApp1() {
    console.log(`connect to ${selectedApp1}`);
    if (selectedApp1 === 'Trello') {
      navigation.navigate('TrelloSub', { token: token, return_destination: "Create" });
    }
    if (selectedApp1 === 'Callr') {
      return;
    }
    // if (selectedApp1 === 'Spotify') {
      //   navigation.navigate('SpotifySub', { token: token, return_destination: "Create" });
      // }
    setIsConnectedToApp1(true);
  }

  function handleConnectApp2() {
    console.log(`connect to ${selectedApp2}`);
    if (selectedApp2 === 'Trello') {
      navigation.navigate('TrelloSub', { token: token, return_destination: "Create" });
    }
    if (selectedApp2 === 'Callr') {
      return;
    }
    if (selectedApp2 === 'GitHub') {
      navigation.navigate('GitHubSub', { token: token, return_destination: "Create" });
    }
    // if (selectedApp2 === 'Spotify') {
    //   navigation.navigate('SpotifySub', { token: token, return_destination: "Create" });
    // }
    setIsConnectedToApp2(true);
  }

  async function handleConnectCallR() {
    if (selectedApp1 === 'Callr') {
      console.log(`connect to ${selectedApp1}`);
      if (!userNameCallR || !passwordNameCallR) {
        alert('Please enter your username and password');
        return;
      }
      console.log(userNameCallR, passwordNameCallR)
      try {
        const response = await axios.post(
          `${ServerUrl()}/subscribe`,
          {
            service: 'callr',
            service_args: {
              return_url: 'http://localhost:8081',
              username: userNameCallR,
              password: passwordNameCallR,
            },
          },
          {
            timeout: 10000,
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.data.auth_url) {
          console.log(response.data.auth_url);
          setIsConnectedToApp1(true);
        } else {
          console.log(response);
          alert('Callr connection failed');
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          if (error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            if (error.response.status === 400) {
              alert('Callr connection failed');
              return;
            }
          } else {
            console.log('Error', error.message);
          }
        } else {
          console.log('Error', error);
        }
        alert('Callr connection failed');
        console.error(error);
      }
    }

    if (selectedApp2 === 'Callr') {
      console.log(`connect to ${selectedApp2}`);
      if (!userNameCallR || !passwordNameCallR) {
        alert('Please enter your username and password');
        return;
      }
      console.log(userNameCallR, passwordNameCallR)
      try {
        const response = await axios.post(
          `${ServerUrl()}/subscribe`,
          {
            service: 'callr',
            service_args: {
              return_url: 'http://localhost:8081',
              username: userNameCallR,
              password: passwordNameCallR,
            },
          },
          {
            timeout: 10000,
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.data.auth_url) {
          console.log(response.data.auth_url);
          setIsConnectedToApp2(true);
        } else {
          console.log(response);
          alert('Callr connection failed');
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          if (error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            if (error.response.status === 400) {
              alert('Callr connection failed');
              return;
            }
          } else {
            console.log('Error', error.message);
          }
        } else {
          console.log('Error', error);
        }
        console.log(response);
        alert('Callr connection failed');
        console.error(error);
      }
    }
  }

  async function handleTryIt() {
    body = {
      action_service: toCamelCase(selectedApp1),
      action_name: toCamelCase(selectedItemApp1),
      reaction_service: toCamelCase(selectedApp2),
      reaction_name: toCamelCase(selectedItemApp2),
    };

    body.action_params = {};
    if (selectedApp1 === 'Time') {
      if (selectedItemApp1 === 'Create timer') {
        body.action_params = {
          hour: Option1app1,
          minute: Option2app1,
        };
      }
    }

    body.reaction_params = {};
    if (selectedApp2 === 'Trello') {
      if (selectedItemApp2 === 'Create Card') {
        body.reaction_params = {
          board_name: Option1app2,
          list_name: Option2app2,
          card_name: Option3app2,
        };
      }
      if (selectedItemApp2 === 'Create Board') {
        body.reaction_params = {
          name: Option1app2,
        };
      }
      if (selectedItemApp2 === 'Create List') {
        body.reaction_params = {
          name: Option1app2,
          board_name: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Delete Board') {
        body.reaction_params = {
          name: Option1app2,
        };
      }
      if (selectedItemApp2 === 'Delete List') {
        body.reaction_params = {
          id: Option1app2,
        };
      }
      if (selectedItemApp2 === 'Delete Card') {
        body.reaction_params = {
          id: Option1app2,
        };
      }
      if (selectedItemApp2 === 'Create Member') {
        body.reaction_params = {
          name: Option1app2,
          email: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Delete Member') {
        body.reaction_params = {
          board_name: Option1app2,
          email: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Update Board') {
        body.reaction_params = {
          name: Option1app2,
          new_name: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Update List') {
        body.reaction_params = {
          board_name: Option1app2,
          list_name: Option2app2,
          new_name: Option3app2,
        };
      }
      if (selectedItemApp2 === 'Update Card') {
        body.reaction_params = {
          board_name: Option1app2,
          card_name: Option2app2,
          new_name: Option3app2,
        };
      }
    }

    if (selectedApp2 === 'Callr') {
      if (selectedItemApp2 === 'Make call') {
        body.reaction_params = {
          target: Option1app2,
          msg: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Send sms') {
        body.reaction_params = {
          target: Option1app2,
          msg: Option2app2,
          sender: Option3app2,
        };
      }
      if (selectedItemApp2 === 'Create media') {
        body.reaction_params = {
          name: Option1app2,
        };
      }
      if (selectedItemApp2 === 'Update media tts') {
        body.reaction_params = {
          id: Option1app2,
          msg: Option2app2,
        };
      }
    }

    if (selectedApp2 === 'ChatGPT') {
      if (selectedItemApp2 === 'Post message sentiments') {
        body.reaction_params = {
          target: Option1app2,
          message_content: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Post message categories') {
        body.reaction_params = {
          target: Option1app2,
          message_content: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Post message summarize') {
        body.reaction_params = {
          target: Option1app2,
          message_content: Option2app2,
        };
      }
      if (selectedItemApp2 === 'Post message mail') {
        body.reaction_params = {
          target: Option1app2,
          message_content: Option2app2,
        };
      }
    }

    console.log(body);
    try {
      const response = await fetch(`${ServerUrl()}/create_AREA`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(body)
      });
      const data = await response.json();
      console.log(data);
      alert("Created Area " + selectedApp1 +  " with " + selectedApp2 + " when " + selectedItemApp1 + " do " + selectedItemApp2);
    } catch (error) {
      console.error('Error:', error);
    }
  }

  return (
    <ScrollView style={styles.background}>
      <Text style={styles.appName}>Create AreaCraft</Text>
      <Text style={styles.stepStyle}>Step 1</Text>
      <Text style={styles.slogan}>Connect this app...</Text>
      <View style={styles.dropdown}>
        <Picker
          selectedValue={selectedApp1}
          onValueChange={(itemValue) => setSelectedApp1(itemValue)}
          style={styles.picker}
        >
          <Picker.Item label="Select app" value="" />
          <Picker.Item label="Trello" value="Trello" />
          <Picker.Item label="Spotify" value="Spotify" />
          <Picker.Item label="Callr" value="Callr" />
          <Picker.Item label="Time" value="Time" />
          <Picker.Item label="Meteo" value="Meteo" />
        </Picker>
      </View>
      <Text style={styles.slogan}>...With this one:</Text>
      <View style={styles.dropdown}>
        <Picker
          selectedValue={selectedApp2}
          onValueChange={(itemValue) => setSelectedApp2(itemValue)}
          style={styles.picker}
        >
          <Picker.Item label="Select app" value="" />
          <Picker.Item label="Trello" value="Trello" />
          <Picker.Item label="Spotify" value="Spotify" />
          <Picker.Item label="ChatGPT" value="ChatGPT" />
          <Picker.Item label="Callr" value="Callr" />
          <Picker.Item label="GitHub" value="GitHub" />
          <Picker.Item label="Time" value="Time" />
        </Picker>
      </View>

      {selectedApp1 && selectedApp2 && (
        <>
          <Text style={styles.stepStyle}>Step 2</Text>
          {selectedApp1 === selectedApp2 && !isConnectedToApp1 && !isConnectedToApp2 && (
            <TouchableOpacity onPress={() => {
              handleConnectApp1();
              handleConnectApp2();
            }} style={styles.connect}>
              <Text style={styles.buttonText}>Connect to {selectedApp1}</Text>
            </TouchableOpacity>
          )}

          {!isConnectedToApp1 && selectedApp1 !== 'Callr' && selectedApp1 !== selectedApp2 && (
            <TouchableOpacity onPress={handleConnectApp1} style={styles.connect}>
              <Text style={styles.buttonText}>Connect to {selectedApp1}</Text>
            </TouchableOpacity>
          )}

          {!isConnectedToApp2 && selectedApp2 !== 'Callr' && selectedApp1 !== selectedApp2 && (
            <TouchableOpacity onPress={handleConnectApp2} style={styles.connect}>
              <Text style={styles.buttonText}>Connect to {selectedApp2}</Text>
            </TouchableOpacity>
          )}
          {selectedApp2 === 'Callr' && !isConnectedToApp2 && (
            <>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="username"
                  placeholderTextColor="#909090"
                  value={userNameCallR}
                  onChangeText={setUserNameCallR}
                />
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="password"
                  placeholderTextColor="#909090"
                  value={passwordNameCallR}
                  onChangeText={setPasswordNameCallR}
                />
              </View>
              <TouchableOpacity onPress={handleConnectCallR} style={styles.connect}>
                <Text style={styles.buttonText}>Connect to {selectedApp2}</Text>
              </TouchableOpacity>
            </>
          )}
          {selectedApp1 === 'Callr' && !isConnectedToApp1 && (
            <>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="username"
                  placeholderTextColor="#909090"
                  value={userNameCallR}
                  onChangeText={setUserNameCallR}
                />
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="password"
                  placeholderTextColor="#909090"
                  value={passwordNameCallR}
                  onChangeText={setPasswordNameCallR}
                />
              </View>
              <TouchableOpacity onPress={handleConnectCallR} style={styles.connect}>
                <Text style={styles.buttonText}>Connect to {selectedApp1}</Text>
              </TouchableOpacity>
            </>
          )}
          {isConnectedToApp1 && isConnectedToApp2 && (
            <>
              <Text style={styles.slogan}>When this happens...</Text>
              <View style={styles.dropdown}>
                {selectedApp1 === 'Trello' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp1} onValueChange={(itemValue) => setSelectedItemApp1(itemValue)}
                    >
                      <Picker.Item label="Create Card" value="Create Card" />
                      <Picker.Item label="Create Board" value="Create Board" />
                      <Picker.Item label="Create List" value="Create List" />
                      <Picker.Item label="Create Member" value="Create Member" />
                      <Picker.Item label="Update Card" value="Update Card" />
                      <Picker.Item label="Update List" value="Update List" />
                      <Picker.Item label="Update Board" value="Update Board" />
                      <Picker.Item label="Delete Card" value="Delete Card" />
                      <Picker.Item label="Delete List" value="Delete List" />
                      <Picker.Item label="Delete Board" value="Delete Board" />
                      <Picker.Item label="Delete Member" value="Delete Member" />
                    </Picker>
                  </>
                )}
                {selectedApp1 === 'Spotify' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp1} onValueChange={(itemValue) => setSelectedItemApp1(itemValue)}
                    >
                      <Picker.Item label="New Playlist" value="New Playlist" />
                      <Picker.Item label="New Saved Track" value="New Saved Track" />
                      <Picker.Item label="New Track Added To Playlist" value="New Track Added To Playlist" />
                    </Picker>
                  </>
                )}
                {selectedApp1 === 'Time' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp1} onValueChange={(itemValue) => setSelectedItemApp1(itemValue)}
                    >
                      <Picker.Item label="Create timer" value="Create timer" />
                    </Picker>
                  </>
                )}
                {selectedApp1 === 'Meteo' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp1} onValueChange={(itemValue) => setSelectedItemApp1(itemValue)}
                    >
                      <Picker.Item label="meteo change" value="meteo change" />
                      <Picker.Item label="temperature" value="temperature" />
                    </Picker>
                  </>
                )}
                {selectedApp1 === 'Callr' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp1} onValueChange={(itemValue) => setSelectedItemApp1(itemValue)}
                    >
                      <Picker.Item label="Call outbound hangup" value="Call outbound hangup" />
                      <Picker.Item label="Call inbound start" value="Call inbound start" />
                      <Picker.Item label="Call outbound start" value="Call outbound start" />
                      <Picker.Item label="Media recording" value="Media recording" />
                      <Picker.Item label="Call inbound hangup" value="Call inbound hangup" />
                      <Picker.Item label="Billing credit" value="Billing credit" />
                      <Picker.Item label="Send sms" value="Send sms" />
                      <Picker.Item label="Did assigned" value="Did assigned" />
                      <Picker.Item label="Did unassigned" value="Did unassigned" />
                    </Picker>
                  </>
                )}
              </View>
              <Text style={styles.slogan}>...then do this:</Text>
              <View style={styles.dropdown}>
                {selectedApp2 === 'Trello' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Create Board" value="Create Board" />
                      <Picker.Item label="Create List" value="Create List" />
                      <Picker.Item label="Create Card" value="Create Card" />
                      <Picker.Item label="Create Member" value="Create Member" />
                      <Picker.Item label="Delete Board" value="Delete Board" />
                      <Picker.Item label="Delete List" value="Delete List" />
                      <Picker.Item label="Delete Card" value="Delete Card" />
                      <Picker.Item label="Delete Member" value="Delete Member" />
                      <Picker.Item label="Update Board" value="Update Board" />
                      <Picker.Item label="Update List" value="Update List" />
                      <Picker.Item label="Update Card" value="Update Card" />
                    </Picker>
                  </>
                )}
                {selectedApp2 === 'Spotify' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Create Playlist" value="Create Playlist" />
                      <Picker.Item label="Find Track" value="Find Track" />
                      <Picker.Item label="Save Track" value="Save Track" />
                    </Picker>
                  </>
                )}
                {selectedApp2 === 'ChatGPT' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Post message sentiments" value="Post message sentiments" />
                      <Picker.Item label="Post message categories" value="Post message categories" />
                      <Picker.Item label="Post message summarize" value="Post message summarize" />
                      <Picker.Item label="Post message mail" value="Post message mail" />
                    </Picker>
                  </>
                )}
                {selectedApp2 === 'GitHub' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Add repository" value="Add repository" />
                      <Picker.Item label="Remove repository" value="Remove repository" />
                    </Picker>
                  </>
                )}
                {selectedApp2 === 'Callr' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Make call" value="Make call" />
                      <Picker.Item label="Send sms" value="Send sms" />
                      <Picker.Item label="Create media" value="Create media" />
                      <Picker.Item label="Update media tts" value="Update media tts" />
                      <Picker.Item label="Get list of medias" value="Get list of medias" />
                      <Picker.Item label="Get quota status" value="Get quota status" />
                    </Picker>
                  </>
                )}
                {selectedApp2 === 'Time' && (
                  <>
                    <Picker
                      style={styles.picker} selectedValue={selectedItemApp2} onValueChange={(itemValue) => setSelectedItemApp2(itemValue)}
                    >
                      <Picker.Item label="Global clock" value="Global clock" />
                    </Picker>
                  </>
                )}
              </View>
              <Text style={styles.stepStyle}>Step 3</Text>
              <Text style={styles.slogan}>option app 1:</Text>
              <View style={styles.inputContainer}>
                {selectedItemApp1 && selectedItemApp2 && (
                  <>
                    {selectedItemApp1 === 'Create timer' && (
                    <View style={styles.inputTextCallr}>
                      <TextInput
                        style={styles.input}
                        placeholder="Time in hour"
                        placeholderTextColor="#909090"
                        value={Option1app1}
                        onChangeText={setOption1app1}
                      />
                      <TextInput
                        style={styles.input}
                        placeholder="Time in minutes"
                        placeholderTextColor="#909090"
                        value={Option2app1}
                        onChangeText={setOption2app1}
                      />
                    </View>
                    )}
                    {selectedItemApp1 === 'meteo change' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="City"
                          placeholderTextColor="#909090"
                          value={Option1app1}
                          onChangeText={setOption1app1}
                        />
                      </>
                    )}
                    {selectedItemApp1 === 'temperature' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="City"
                          placeholderTextColor="#909090"
                          value={Option1app1}
                          onChangeText={setOption1app1}
                        />
                      </>
                    )}
                  </>
                )}
              </View>
              <Text style={styles.slogan}>option app 2:</Text>
              <View style={styles.inputContainer}>
                {selectedItemApp1 && selectedItemApp2 && (
                  <>
                    {selectedItemApp2 === 'Create Board' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Board name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Create List' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="List name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="Board name"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Create Card' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Name of the board"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="Name of the list"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="message"
                          placeholderTextColor="#909090"
                          value={Option3app2}
                          onChangeText={setOption3app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Create Member' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Member id"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="Board name"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Delete Board' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Board name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Delete List' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="List id"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Delete Card' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Card id"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Delete Member' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="name of the board"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="email of the member"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Update Board' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="id"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="name"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Update List' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="board name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="list name"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="new name of the list"
                          placeholderTextColor="#909090"
                          value={Option3app2}
                          onChangeText={setOption3app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Update Card' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="board name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="card name"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="new card name"
                          placeholderTextColor="#909090"
                          value={Option3app2}
                          onChangeText={setOption3app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Create Playlist' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Playlist name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Find Track' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Track name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Save Track' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Track name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Post message sentiments' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Post message categories' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Post message summarize' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Post message mail' && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === 'Add repository' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Repo name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === 'Remove repository' && (
                      <>
                        <TextInput
                          style={styles.input}
                          placeholder="Repo name"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                        />
                      </>
                    )}
                    {selectedItemApp2 === "Send sms" && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="Sms Message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                        <TextInput
                          style={styles.input}
                          placeholder="Sms Sender (optional)"
                          placeholderTextColor="#909090"
                          value={Option3app2}
                          onChangeText={setOption3app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === "Make call" && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Target phone number (ex: +33612345678)"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="Sms Message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                    {selectedItemApp2 === "Create media" && (
                      <TextInput
                        style={styles.input}
                        placeholder="Name of the media"
                        placeholderTextColor="#909090"
                        value={Option1app2}
                        onChangeText={setOption1app2}
                      />
                    )}
                    {selectedItemApp2 === "Update media tts" && (
                      <View style={styles.inputTextCallr}>
                        <TextInput
                          style={styles.input}
                          placeholder="Id of the media"
                          placeholderTextColor="#909090"
                          value={Option1app2}
                          onChangeText={setOption1app2}
                          />
                        <TextInput
                          style={styles.input}
                          placeholder="Sms Message"
                          placeholderTextColor="#909090"
                          value={Option2app2}
                          onChangeText={setOption2app2}
                        />
                      </View>
                    )}
                  </>
                )}
              </View>
            </>
          )}
        </>
      )}
      <View style={styles.summaryContainer}>
        <Text style={styles.summaryText}>
          {selectedApp1 || "None"} with {selectedApp2 || "None"} when {selectedItemApp1 || "None"} do {selectedItemApp2 || "None"}
        </Text>
      </View>

      <TouchableOpacity style={styles.button} onPress={handleTryIt}>
        <Text style={styles.buttonText}>Try it</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  background: {
    backgroundColor: COLORS.background,
  },
  container: {
    flex: 1,
    backgroundColor: COLORS.mediumLight,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
    paddingBottom: 50,
  },
  appName: {
    marginTop: 10,
    fontSize: 32,
    marginBottom: 10,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font',
  },
  stepStyle: {
    marginTop: 20,
    fontSize: 32,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font',
  },
  label: {
    fontSize: 18,
    alignSelf: 'flex-start',
    marginVertical: 17,
    marginLeft: 12,
    backgroundColor: COLORS.bluetech,
    fontFamily: 'custom-font',
    color: COLORS.white,
  },
  slogan: {
    fontSize: 18,
    marginTop: 20,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font-quicksand'
  },
  dropdown: {
    flexDirection: 'row',
    alignItems: 'center',
    marginHorizontal: 20,
    marginVertical: 10,
    backgroundColor: COLORS.bluetech,
    borderRadius: 5,
    borderColor: COLORS.bluetech,
    borderWidth: 1,
    paddingHorizontal: 10,
  },
  picker: {
    flex: 1,
    height: 50,
    backgroundColor: COLORS.bluetech,
    color: COLORS.white,
  },
  button: {
    backgroundColor: COLORS.bluetech,
    borderRadius: 5,
    padding: 10,
    marginHorizontal: 20,
    marginVertical: 50,
  },
  connect: {
    backgroundColor: COLORS.bluetech,
    borderRadius: 5,
    padding: 10,
    marginHorizontal: 20,
    marginVertical: 20,
  },
  buttonText: {
    color: COLORS.white,
    fontSize: 18,
    textAlign: 'center',
    fontFamily: 'custom-font',
  },
  summaryContainer: {
    marginTop: 20,
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  summaryText: {
    color: COLORS.white,
    fontSize: 16,
    fontFamily: 'custom-font',
    textAlign: 'center',
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
  inputContainer: {
    flexDirection: 'row',
    marginHorizontal: 15,
    paddingHorizontal: 10,
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '95%',
    position: 'relative'
  },
  inputTextCallr: {
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '95%',
    position: 'relative'
  },
});