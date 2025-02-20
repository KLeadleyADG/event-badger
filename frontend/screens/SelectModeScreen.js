import React from 'react';
import { View, StyleSheet, Text, TouchableOpacity, Platform } from 'react-native';
import Button from '../components/ui/Button';
import { GlobalStyles } from '../constants/styles';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function SelectModeScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  
  function backOnPress() {
    navigation.navigate('AdminLoginScreen');
  }

  function badgePrintOnPress() {
    navigation.navigate('SelectPrinterScreen', { mode: 'Badge' });
  }

  function qrScannerOnPress() {
    navigation.navigate('SelectEventScreen', { mode: 'QR' });
  }

  function setPinOnPress() {
    navigation.navigate('SetPinScreen');
  }

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <Text style={GlobalStyles.headerText}>Select Mode</Text>
        <View style={[GlobalStyles.inputContainer, styles.inputContainer]}>
          <Button onPress={qrScannerOnPress}>QR Scanner</Button>
          <Button onPress={badgePrintOnPress}>Badge Printer</Button>
        </View>
        <TouchableOpacity onPress={setPinOnPress} style={GlobalStyles.passwordContainer}>
          <Text style={GlobalStyles.passwordText}>Set Pin</Text>
        </TouchableOpacity>
      </View>
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
      </View>
    </View>
  );
}

export default SelectModeScreen;

const styles = StyleSheet.create({
  inputContainer: {
    flexDirection: 'row'
  },
});
