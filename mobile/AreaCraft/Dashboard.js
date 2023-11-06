import React from 'react';
import { StyleSheet, View, ScrollView, ActivityIndicator, Text, TextInput, Image, TouchableOpacity } from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import COLORS from '../assets/colors';
import useDashboardLogic from './Logics/useDashboardLogic';
import AreaCard from './Areacard';

export default function DashboardComponent() {
  const route = useRoute();
  const token = route.params.token;
  const navigation = useNavigation();

  const {
    filteredData,
    isLoading,
    errorMessage,
    displayedCount,
    searchQuery,
    setSearchQuery,
    handleScroll,
    NavigateCreate,
  } = useDashboardLogic(token);


  if (errorMessage) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorMessage}>{errorMessage}</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.background} onScroll={handleScroll} scrollEventThrottle={400}>
      <Image
          source={require('../assets/icons/logo.png')}
          style={{ width: 100, height: 100, marginTop: 0, alignSelf: 'center', marginBottom: 1 }}
      />
      <Text style={styles.appName}>Dashboard</Text>
      <Text style={styles.text}>Connect your apps together</Text>
      <TouchableOpacity style={styles.customButton} onPress={(NavigateCreate)}>
        <Text style={styles.buttonText}>Add new area</Text>
      </TouchableOpacity>
      <Text style={styles.Textmiddle}>Your areas</Text>
      <Text style={styles.Textmiddle}>Recommended areas</Text>
      <AreaCard
        image1={require('../assets/icons/trello.png')}
        image2={require('../assets/icons/trello.png')}
        description="Create card when new list is created"
        token={token}
      />
      <View style={styles.container}>
        {isLoading && (
        <View style={styles.bottomLoaderContainer}>
          <ActivityIndicator size="small" color="black" />
        </View>
      )}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  background: {
    backgroundColor: COLORS.background,
  },
  appName: {
    fontSize: 32,
    marginBottom: 10,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font'
  },
  buttonText: {
    color: COLORS.dark,
    fontSize: 20,
    fontFamily: 'custom-font',
    alignSelf: 'center',
  },
  customButton: {
    backgroundColor: COLORS.bluetech,
    borderRadius: 5,
    paddingVertical: 12,
    paddingHorizontal: 10,
    marginVertical: 10,
    width: 180,
    alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center'
  },
  slogan: {
    fontSize: 18,
    marginTop: 20,
    textAlign: 'center',
    color: '#000',
    fontFamily: 'custom-font-quicksand'
  },
  Textmiddle: {
    fontSize: 18,
    marginBottom: 18,
    marginTop: 40,
    marginLeft: 45,
    textAlign: 'left',
    color: COLORS.white,
    fontFamily: 'custom-font'
  },
  text: {
    fontSize: 14,
    marginBottom: 18,
    textAlign: 'center',
    color: COLORS.white,
    fontFamily: 'custom-font-quicksand'
  },
  container: {
    flex: 1,
    alignItems: 'center',
    paddingTop: 20,
    paddingBottom: 20,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
    paddingHorizontal: 10,
  },
  loaderContainer: {
    flex: 1,
    backgroundColor: 'transparent',
    alignItems: 'center',
    justifyContent: 'center'
  },
  errorContainer: {
    flex: 1,
    backgroundColor: COLORS.mediumLight,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20
  },
  errorMessage: {
    color: 'red',
    fontSize: 18,
    textAlign: 'center'
  },
  bottomLoaderContainer: {
    position: 'absolute',
    bottom: 20,
    left: 0,
    right: 0,
    alignItems: 'center'
  },
  searchInput: {
    width: '95%',
    padding: 10,
    marginLeft: 10,
    marginTop: 20,
    backgroundColor: COLORS.neutral,
    borderRadius: 5,
    borderColor: '#BDA18A',
    borderWidth: 1,
    color: '#000',
    fontFamily: 'custom-font'
  },
});