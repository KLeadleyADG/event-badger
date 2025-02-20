import React, { useState, useCallback } from 'react';
import { View, TextInput, Text, Platform } from 'react-native';
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage';
import { GlobalStyles } from '../constants/styles';
import { useUser } from '../context/UserContext';
import { getApiConfig } from '../constants/api';
import useKeyboardVisibility from '../hooks/useKeyboardVisibility';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';


function SetPinScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const api = getApiConfig();
  const { user } = useUser();
  const [pin, setPin] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const isKeyboardVisible = useKeyboardVisibility();

  const backOnPress = useCallback(() => {
    navigation.navigate('SelectModeScreen');
  }, [navigation]);

  const setPinOnPress = async () => {
    if (!/^[0-9]{4}$/.test(pin)) {
      setMessage('PIN must be a 4-digit number');
      setIsError(true);
      return;
    }

    try {
      const response = await fetch(`${api.apiUrl}/api/users/setPin`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: user.email.toLowerCase(), pin }), // Use user's email in lowercase
      });

      const responseText = await response.text();
      console.log('Response from server:', responseText);

      const data = JSON.parse(responseText);

      if (response.ok) {
        setMessage('PIN set successfully');
        setIsError(false);
        setTimeout(() => {
          setMessage('');
          navigation.navigate('SelectModeScreen');
        }, 3000); // Show success message for 3 seconds
      } else {
        setMessage(data.message || 'Failed to set PIN');
        setIsError(true);
      }
    } catch (err) {
      console.error('Error setting PIN:', err);
      setMessage('Error setting PIN');
      setIsError(true);
    }
  };

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <Text style={GlobalStyles.headerText}>Set Pin</Text>
        <View style={GlobalStyles.inputContainer}>
          <TextInput
            style={GlobalStyles.textInput}
            placeholder="Enter 4-digit PIN"
            secureTextEntry
            value={pin}
            onChangeText={setPin}
            keyboardType="numeric"
            maxLength={4}
          />
        </View>
        {!isKeyboardVisible &&(<Button onPress={setPinOnPress}>Set Pin</Button>)}
      </View>
      {!isKeyboardVisible && (<View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
        <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
      </View>)}
    </View>
  );
}

export default SetPinScreen;
