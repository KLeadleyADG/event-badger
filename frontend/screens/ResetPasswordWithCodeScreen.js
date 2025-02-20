import React, { useState, useCallback } from 'react';
import { View, TextInput, Text, Platform } from 'react-native';
import Button from '../components/ui/Button';
import ErrorMessage from '../components/ui/ErrorMessage'; // Ensure this matches the actual directory casing
import { GlobalStyles } from '../constants/styles';
import useResetStateOnFocus from '../hooks/useResetStateOnFocus';
import { getApiConfig } from '../constants/api';
import useKeyboardVisibility from '../hooks/useKeyboardVisibility';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function ResetPasswordWithCodeScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const api = getApiConfig();
  const [resetCode, setResetCode] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const isKeyboardVisible = useKeyboardVisibility();

  const backOnPress = useCallback(() => {
    navigation.navigate('RequestPasswordResetScreen');
  }, [navigation]);

  const resetState = () => {
    setResetCode('');
    setPassword('');
    setMessage('');
    setIsError(false);
  };

  useResetStateOnFocus(resetState);

  const resetPassword = async () => {
    try {
      const response = await fetch(`${api.apiUrl}/api/users/reset`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ resetCode, password }),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage('Password has been reset successfully.');
        setIsError(false);

        setTimeout(() => {
          navigation.navigate('AdminLoginScreen');
        }, 3000); // Redirect after 3 seconds
      } else {
        setMessage(data.message || 'Password reset failed.');
        setIsError(true);
      }
    } catch (err) {
      console.error('Error resetting password:', err);
      setMessage('Error resetting password.');
      setIsError(true);
    }
  };

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <View style={GlobalStyles.inputContainer}>
          <TextInput
            style={GlobalStyles.textInput}
            placeholder="Reset Code"
            value={resetCode}
            onChangeText={setResetCode}
          />
          <TextInput
            style={GlobalStyles.textInput}
            placeholder="New Password"
            secureTextEntry
            value={password}
            onChangeText={setPassword}
          />
        </View>
        {!isKeyboardVisible && (<Button onPress={resetPassword}>Reset Password</Button>)}
      </View>
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
        <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
      </View>
    </View>
  );
}

export default ResetPasswordWithCodeScreen;
