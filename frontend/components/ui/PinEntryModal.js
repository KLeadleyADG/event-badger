import React, { useState, useRef, useEffect } from 'react';
import { View, TextInput, StyleSheet, Modal, Text } from 'react-native';
import Button from './Button';
import { GlobalStyles } from '../../constants/styles';

const PinEntryModal = ({ visible, message, onSubmit, onCancel }) => {
  const [pin, setPin] = useState(['', '', '', '']);
  const inputRefs = [useRef(null), useRef(null), useRef(null), useRef(null)];

  useEffect(() => {
    if (visible) {
      setPin(['', '', '', '']);
    }
  }, [visible]);

  const cancelOnPress = () => {
    setPin(['', '', '', '']);
    onCancel();
  };

  const handleChange = (value, index) => {
    const newPin = [...pin];
    newPin[index] = value;
    setPin(newPin);
    if (value && index < 3) {
      inputRefs[index + 1].current.focus();
    }
  };

  const handleKeyPress = (e, index) => {
    if (e.nativeEvent.key === 'Backspace' && index > 0 && pin[index] === '') {
      inputRefs[index - 1].current.focus();
    }
  };

  const handleSubmit = () => {
    onSubmit(pin.join(''));
  };

  return (
    <Modal visible={visible} transparent={true} animationType="slide">
      <View style={styles.modalBackground}>
        <View style={styles.modalContainer}>
          <Text>Enter Pin</Text>
          <View style={styles.pinContainer}>
            {pin.map((digit, index) => (
              <TextInput
                key={index}
                ref={inputRefs[index]}
                style={styles.pinInput}
                value={digit}
                onChangeText={(value) => handleChange(value, index)}
                onKeyPress={(e) => handleKeyPress(e, index)}
                keyboardType="numeric"
                maxLength={1}
                secureTextEntry
              />
            ))}
          </View>
          <Button onPress={handleSubmit}>Submit</Button>
          <Button onPress={cancelOnPress}>Cancel</Button>
          {message ? <Text style={GlobalStyles.errorMessage}>{message}</Text> : null}
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalBackground: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
  },
  modalContainer: {
    width: 300,
    padding: 20,
    backgroundColor: 'white',
    borderRadius: 10,
    alignItems: 'center',
  },
  pinContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 20,
  },
  pinInput: {
    width: 50,
    height: 50,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    textAlign: 'center',
    fontSize: 24,
  },
});

export default PinEntryModal;
