// frontend/components/ui/ErrorMessage.js
import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { GlobalStyles } from '../../constants/styles';

function ErrorMessage({ message, isError, duration = 5000, onDismiss }) {
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => {
        onDismiss();
      }, duration);

      return () => clearTimeout(timer);
    }
  }, [message, duration, onDismiss]);

  if (!message) return null;

  return (
    <View style={styles.container}>
      <Text style={isError ? GlobalStyles.errorMessage : GlobalStyles.successMessage}>
        {message}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
    marginBottom:20
  },
});

export default ErrorMessage;

