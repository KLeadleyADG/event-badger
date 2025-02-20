import React, { useState, useCallback } from 'react';
import { View, TextInput, Text, StyleSheet, TouchableOpacity, Platform } from 'react-native';
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage'; // Ensure this matches the actual directory casing
import { GlobalStyles } from '../constants/styles';
import { getApiConfig } from '../constants/api';
import useResetStateOnFocus from '../hooks/useResetStateOnFocus';
import useKeyboardVisibility from '../hooks/useKeyboardVisibility';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function RequestPasswordResetScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const api = getApiConfig();
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const isKeyboardVisible = useKeyboardVisibility();

  const backOnPress = useCallback(() => {
    navigation.navigate('AdminLoginScreen');
  }, [navigation]);

  const resetState = () => {
    setEmail('');
    setMessage('');
    setIsError(false);
  };

  useResetStateOnFocus(resetState);

  const requestReset = async () => {
    try {
      const response = await fetch(`${api.apiUrl}/api/users/requestPasswordReset`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage('Password reset email sent. Please check your email for the reset code.');
        setIsError(false);
      } else {
        setMessage(data.message || 'Password reset request failed.');
        setIsError(true);
      }
    } catch (err) {
      console.error('Error requesting password reset:', err);
      setMessage('Error requesting password reset.');
      setIsError(true);
    }
  };

  const goToResetPasswordScreen = () => {
    navigation.navigate('ResetPasswordWithCodeScreen');
  };

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <Text style={GlobalStyles.headerText}>Get Reset Code</Text>
        <View style={GlobalStyles.inputContainer}>
          <TextInput
            style={GlobalStyles.textInput}
            placeholder="Email"
            autoCapitalize="none"
            keyboardType="email-address"
            value={email}
            onChangeText={setEmail}
          />
        </View>
        {!isKeyboardVisible &&(
          <View>
            <Button onPress={requestReset}>Send Code</Button>
            <TouchableOpacity onPress={goToResetPasswordScreen} style={GlobalStyles.passwordContainer}>
              <Text style={GlobalStyles.passwordText}>Have a reset code? Reset your password</Text>
            </TouchableOpacity>
          </View>
        )}
      </View>
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
        <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
      </View>
    </View>
  );
}

export default RequestPasswordResetScreen;