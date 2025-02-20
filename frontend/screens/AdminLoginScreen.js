import React, { useState, useEffect } from 'react';
import {
  View,
  TextInput,
  Text,
  TouchableWithoutFeedback,
  Keyboard,
  TouchableOpacity,
  ActivityIndicator,
  Platform,
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage';
import { GlobalStyles } from '../constants/styles';
import { fetchApiUrl, fetchApiConfig } from '../api/fetch';
import { useUser } from '../context/UserContext';
import { getApiConfig } from '../constants/api';
import useKeyboardVisibility from '../hooks/useKeyboardVisibility';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function AdminLoginScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const { setUser } = useUser();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const [loading, setLoading] = useState(true);
  const isKeyboardVisible = useKeyboardVisibility();

  useEffect(() => {
    const initializeApiUrl = async () => {
      console.log("Get API URL");
      try {
        await fetchApiUrl();
      } catch (error) {
        console.log(error);
        setMessage('Error initializing API URL');
        setIsError(true);
      } finally {
        setLoading(false);
      }
    };
    initializeApiUrl();
  }, []);

  const logInOnPress = async () => {
    try {
      const apiConfig = getApiConfig();
      console.log(apiConfig);
      console.log('Sending login request with email:', email);
      console.log(`Endpoint: ${apiConfig.apiUrl}/api/users/login`);
      const response = await fetch(`${apiConfig.apiUrl}/api/users/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        const data = await response.json();
        console.log('Response from server:', data);

        if (response.ok) {
          console.log('Log In successful');
          await fetchApiConfig(data.token);  
          setUser({ email, token: data.token }); // Set user context with email and token
          setMessage('Log In and configuration successful!');
          setIsError(false);

          setTimeout(() => {
            navigation.navigate('SelectModeScreen'); // Or another protected screen
          }, 2000); // Navigate after 1 second
        } else {
          setMessage(data.message || 'Login failed');
          setIsError(true);
        }
      } else {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        setMessage('Login failed: ' + errorText);
        setIsError(true);
      }
    } catch (err) {
      console.error('Error logging in:', err);
      setMessage('Error logging in');
      setIsError(true);
    }
  };

  const registerOnPress = () => {
    console.log('Register');
    navigation.navigate('RegisterScreen');
  };

  const forgotPasswordOnPress = () => {
    console.log('Forgot Password');
    navigation.navigate('RequestPasswordResetScreen');
  };

  if (loading) {
    return (
      <View style={GlobalStyles.container}>
        <ActivityIndicator size="large" color={GlobalStyles.colors.primary} />
      </View>
    );
  }

  return (
    <KeyboardAwareScrollView
      contentContainerStyle={GlobalStyles.container}
      resetScrollToCoords={{ x: 0, y: 0 }}
      scrollEnabled
      enableAutomaticScroll
      extraScrollHeight={20}
    >
      <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
        <View style={GlobalStyles.container}>
          <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
            <Text style={GlobalStyles.headerText}>Log In</Text>
            <View style={GlobalStyles.inputContainer}>
              <TextInput
                style={GlobalStyles.textInput}
                placeholder="Email"
                autoCapitalize="none"
                keyboardType="email-address"
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
              {!isKeyboardVisible &&(
                <View>
                  <TouchableOpacity onPress={forgotPasswordOnPress} style={GlobalStyles.passwordContainer}>
                    <Text style={GlobalStyles.passwordText}>Forgot Password?</Text>
                  </TouchableOpacity>
                  <Button onPress={logInOnPress}>Log In</Button>
                </View>)}
            </View>
          </View>
          {!isKeyboardVisible && (
            <View style={GlobalStyles.bottomContainer}>
              <Button onPress={registerOnPress}>Create Account</Button>
              <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
            </View>
          )}
        </View>
      </TouchableWithoutFeedback>
    </KeyboardAwareScrollView>
  );
}

export default AdminLoginScreen;

