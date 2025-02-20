import React, { useState, useEffect } from 'react';
import { View, Modal, Text, Platform } from 'react-native';
import { GlobalStyles } from '../../constants/styles';
import Button from './Button';
import ErrorMessage from './ErrorMessage';
import useKeyboardVisibility from '../../hooks/useKeyboardVisibility';
import EmailInput from './EmailInput';

function EmailVerification({ visible, email, closeModal, resetState, domains }) {
  const [enteredEmail, setEnteredEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);
  const isKeyboardVisible = useKeyboardVisibility();

  useEffect(() => {
    if (visible) {
      setEnteredEmail('');
      setMessage('');
      setIsError(false);
    }
  }, [visible]);

  const emailInputHandler = (enteredText) => {
    setEnteredEmail(enteredText);
  };

  const verifyOnPress = () => {
    if (enteredEmail) {
      if (email && email.toString().toUpperCase() === enteredEmail.toString().toUpperCase()) {
        setIsError(false);
        setEnteredEmail('');
        closeModal();
      } else {
        setMessage('Entered Email does not match');
        setIsError(true);
        setTimeout(() => {
          setMessage('');
        }, 3000);
      }
    }
  };

  const onBackPress = () => {
    setEnteredEmail('');
    setIsError(false);
    resetState();
  };

  return (
    <Modal visible={visible} animationType='slide'>
      <View style={GlobalStyles.container}>
        <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
          <View style={GlobalStyles.inputContainer}>
            <Text style={GlobalStyles.headerText}>Please Verify Email</Text>
            <EmailInput
              style={GlobalStyles.textInput}
              placeholder="Verify Email"
              value={enteredEmail}
              onChangeText={emailInputHandler}
              domains={domains}
            />
            {!isKeyboardVisible && (<Button onPress={verifyOnPress}>Verify</Button>)}
          </View>
        </View>
        {!isKeyboardVisible && (
          <View style={GlobalStyles.bottomContainer}>
            <Button onPress={onBackPress}>Cancel</Button>
            <ErrorMessage message={message} isError={isError} onDismiss={() => setMessage('')} />
          </View>
        )}
      </View>
    </Modal>
  );
}

export default EmailVerification;
