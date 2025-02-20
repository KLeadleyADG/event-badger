import React, { useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import { GlobalStyles } from '../../constants/styles';

function Button({ children, onPress, style }) {
  const [isPressed, setIsPressed] = useState(false);

  return (
    <View style={[styles.buttonContainer, style]}>
      <Pressable
        style={({ pressed }) => [
          styles.button,
          pressed || isPressed ? styles.buttonPressed : null,
        ]}
        onPressIn={() => setIsPressed(true)}
        onPressOut={() => setIsPressed(false)}
        onPress={onPress}
      >
        <Text style={styles.buttonText}>{children}</Text>
      </Pressable>
    </View>
  );
}

export default Button;

const styles = StyleSheet.create({
  buttonContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    marginTop: 16,
    flexDirection: 'row',
  },
  button: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: GlobalStyles.colors.secondary,
    borderRadius: 6,
    width: 158,
    marginHorizontal: 8,
  },
  buttonPressed: {
    backgroundColor: GlobalStyles.colors.secondaryDark, 
  },
  buttonText: {
    color: GlobalStyles.colors.white,
    padding: 16,
    fontSize: 18,
  },
});
