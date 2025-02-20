import React, { useState, useEffect, useCallback } from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet, ActivityIndicator, Platform } from 'react-native';
import axios from 'axios';
import { GlobalStyles } from '../constants/styles';
import { setApiConfig, getApiConfig } from '../constants/api'; 
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage'; 
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function SelectPrinterScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const api = getApiConfig();
  const [printers, setPrinters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    fetchPrinters();
  }, []);

  const backOnPress = useCallback(() => {
    navigation.navigate('SelectModeScreen');
  }, [navigation]);

  const fetchPrinters = async () => {
    console.log(`Fetching Printers at: ${api.apiUrl}/api/printers`);
    try {
      setLoading(true);
      const response = await axios.get(`${api.apiUrl}/api/printers`);
      setPrinters(response.data);

      if (response.data.length === 0) {
        setTimeout(() => {
          navigation.navigate('SelectEventScreen', { mode: 'Badge', printer: null });
        }, 3000);
      } else {
        setMessage("Successfully Fetched Printers");
        setIsError(false);
      }
    } catch (error) {
      setMessage(`Failed to fetch printers: ${error.message}`);
      setIsError(true);
      setTimeout(() => {
        navigation.navigate('SelectEventScreen', { mode: 'Badge', printer: null });
      }, 3000);
    } finally {
      setLoading(false);
    }
  };

  const handlePrinterSelect = (printer) => {
    console.log(printer);
    const currentConfig = getApiConfig();
    setApiConfig({ ...currentConfig, printer });
    navigation.navigate('SelectEventScreen', { mode: 'Badge', printer });
  };

  return (
    <View style={GlobalStyles.container}>
      <Text style={GlobalStyles.headerText}>Select Printer</Text>
      {loading ? (
        <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
          <ActivityIndicator size="large" color={GlobalStyles.colors.secondary} />
          <Text style={GlobalStyles.infoText}>Loading Printers...</Text>
        </View>
      ) : (
        <>
          {printers.length === 0 ? (
            <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
              <Text style={GlobalStyles.infoText}>No printers found. Proceeding...</Text>
              <ActivityIndicator size="large" color={GlobalStyles.colors.secondary} />
            </View>
          ) : (
            <FlatList
              data={printers}
              keyExtractor={(item) => item.ip}
              renderItem={({ item }) => (
                <TouchableOpacity style={styles.printerItem} onPress={() => handlePrinterSelect(item)}>
                  <Text style={styles.printerText}>{item.name} ({item.ip}) - MAC: {item.mac}</Text>
                </TouchableOpacity>
              )}
            />
          )}
        </>
      )}
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Cancel</Button>
        <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
      </View>
    </View>
  );
}

export default SelectPrinterScreen;

const styles = StyleSheet.create({
  printerItem: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: GlobalStyles.colors.secondary,
    borderRadius: 6,
    margin: 16,
    padding: 16,
  },
  printerText: {
    color: GlobalStyles.colors.white,
    fontSize: 16,
  },
  spinner: {
    marginBottom: 10,
  },
});


