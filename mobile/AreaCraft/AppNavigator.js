import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import Login from './Login';
import Dashboard from './Dashboard';
import Create from './Create';
import Register from './Register';
import COLORS from '../assets/colors';
import TrelloSub from './TrelloSub';
import GitHubSub from './GitHubSub';
import SpotifySub from './SpotifySub';
import GoToGithub from './GoToGithub';

const Stack = createStackNavigator();

function AppNavigator() {
  return (
    <Stack.Navigator
      initialRouteName="Login"
      screenOptions={{
      headerStyle: {
        backgroundColor: COLORS.neutral,
      },
      headerTitleStyle: {
        fontFamily: 'custom-font',
        fontSize: 22,
        color: COLORS.mediumLight
      },
      headerTintColor: '#F2F2F2',
      headerTitleAlign: 'center',
    }}>
      <Stack.Screen name="Login" component={Login} options={{ headerShown: false }}/>
      <Stack.Screen
        name="Dashboard"
        component={Dashboard}
        options={({ navigation, route }) => {
          const token = route.params.token;
          return {
            title: 'AreaCraft',
          }
        }}
      />

      <Stack.Screen name="Create" component={Create} options={{ title: 'AreaCraft.' }}/>
      <Stack.Screen name="Register" component={Register} options={{ title: 'Areacraft' }}/>
      <Stack.Screen name="TrelloSub" component={TrelloSub} options={{ title: 'Trello' }}/>
      <Stack.Screen name="GitHubSub" component={GitHubSub} options={{ title: 'Github' }}/>
      <Stack.Screen name="SpotifySub" component={SpotifySub} options={{ title: 'Spotify' }}/>
      <Stack.Screen name="GoToGithub" component={GoToGithub} options={{ title: 'Github' }}/>
    </Stack.Navigator>
  );
}

export default AppNavigator;
