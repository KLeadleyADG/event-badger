import React, { useState } from 'react';
import { View, Text, TextInput, TouchableWithoutFeedback, Keyboard, Platform } from 'react-native';
import { GlobalStyles } from '../constants/styles';
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage';
import { getApiConfig } from '../constants/api';
import useKeyboardVisibility from '../hooks/useKeyboardVisibility'; 
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

const RegisterScreen = ({ navigation }) => {
  useBackHandlerAndStatusBar();
  const api = getApiConfig();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const isKeyboardVisible = useKeyboardVisibility();

  const register = async () => {
    try {
      const response = await fetch(`${api.apiUrl}/api/users/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage('Registration successful! Please check your email to verify your account.');
        setIsError(false);
        setTimeout(() => {
          navigation.navigate('AdminLoginScreen');
        }, 1000); // Navigate after 1 second
      } else {
        setMessage(data.message || 'Error registering user.');
        setIsError(true);
      }
    } catch (err) {
      console.error('Network request failed:', err);
      setMessage('Error registering user. Please check your network connection and try again.');
      setIsError(true);
    }
  };

  const cancelOnPress = () => {
    navigation.navigate('AdminLoginScreen');
  };

  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
      <View style={GlobalStyles.container}>
        <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
          <Text style={GlobalStyles.headerText}>Register</Text>
          <View style={GlobalStyles.inputContainer}>
            <TextInput
              style={GlobalStyles.textInput}
              placeholder="Email"
              value={email}
              onChangeText={setEmail}
            />
            <TextInput
              style={GlobalStyles.textInput}
              placeholder="Password"
              secureTextEntry
              value={password}
              onChangeText={setPassword}
            />
             {!isKeyboardVisible && (<Button onPress={register}>Register</Button>)}
          </View>
        </View>
        {!isKeyboardVisible && (
          <View style={GlobalStyles.bottomContainer}>
            <Button onPress={cancelOnPress}>Cancel</Button>
            <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
          </View> 
        )} 
      </View>
    </TouchableWithoutFeedback>
  );
};

export default RegisterScreen;

