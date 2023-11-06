import { useState, useEffect } from 'react';
import axios from 'axios';
import base64 from 'base-64';
import Constants from 'expo-constants';
import { useNavigation, useRoute } from '@react-navigation/native';

const PAGE_SIZE = 100;
const imageCache = new Map();

const useDashboardLogic = (token) => {
  const [cardData, setCardData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [displayedCount, setDisplayedCount] = useState(PAGE_SIZE);
  const [searchQuery, setSearchQuery] = useState('');
  const navigation = useNavigation();

  const filteredData = cardData.filter(
    data =>
      data.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      data.surname.toLowerCase().includes(searchQuery.toLowerCase()) ||
      data.email.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleScroll = ({ nativeEvent }) => {
    if (nativeEvent.contentOffset.y + nativeEvent.layoutMeasurement.height >= nativeEvent.contentSize.height) {
      setDisplayedCount(prevCount => Math.min(prevCount + PAGE_SIZE, cardData.length));
    }
  };

  const NavigateCreate = () => {
    navigation.navigate('Create', { token: token });
  };

  return {
    filteredData,
    isLoading,
    errorMessage,
    displayedCount,
    searchQuery,
    setSearchQuery,
    handleScroll,
    NavigateCreate,
  };
};

export default useDashboardLogic;
