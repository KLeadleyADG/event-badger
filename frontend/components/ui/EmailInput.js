import React, { useState, useEffect } from 'react';
import { StyleSheet, TextInput, View, Text, TouchableOpacity } from 'react-native';
import useKeyboardVisibility from '../../hooks/useKeyboardVisibility';
import { GlobalStyles } from '../../constants/styles';

const EmailInput = ({ value, onChangeText, style, domains, ...props }) => {
  const [email, setEmail] = useState(value || '');
  const [suggestions, setSuggestions] = useState([]);
  const [inputHeight, setInputHeight] = useState(0);
  const isKeyboardVisible = useKeyboardVisibility();

  useEffect(() => {
    if (!isKeyboardVisible) {
      setSuggestions([]);
    }
  }, [isKeyboardVisible]);

  const handleChangeText = (text) => {
    setEmail(text);
    if (text.includes('@')) {
      const [localPart, domainPart] = text.split('@');
      const filteredDomains = domains.filter(domain => domain.startsWith(domainPart));
      setSuggestions(filteredDomains);
    } else {
      setSuggestions(domains);
    }
    onChangeText && onChangeText(text);
  };

  const handleSuggestionPress = (suggestion) => {
    const [localPart] = email.split('@');
    const newEmail = `${localPart}@${suggestion}`;
    setEmail(newEmail);
    setSuggestions([]);
    onChangeText && onChangeText(newEmail);
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={[styles.input, style]}
        value={email}
        onChangeText={handleChangeText}
        keyboardType="email-address"
        autoCapitalize="none"
        autoCompleteType="email"
        onLayout={(event) => {
          const { height } = event.nativeEvent.layout;
          setInputHeight(height);
        }}
        {...props}
      />
      {isKeyboardVisible && (
        <>
          <Text style={styles.italicInfo}>(When done press "return" on the keyboard)</Text>
          {suggestions.length > 0 && (
            <>
              <Text style={[GlobalStyles.infoText, styles.noMarginText]}>Domain Autofill Below:</Text>
              <View style={[styles.suggestionsContainer, { top: inputHeight }]}>
                {suggestions.map((suggestion, index) => (
                  <TouchableOpacity
                    key={index}
                    onPress={() => handleSuggestionPress(suggestion)}
                    style={styles.suggestion}
                  >
                    <Text style={styles.suggestionText}>{`${email.split('@')[0]}@${suggestion}`}</Text>
                  </TouchableOpacity>
                ))}
              </View>
            </>
          )}
        </>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'relative',
    width: '100%',
    alignItems: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#BFCFDA',
    backgroundColor: '#BFCFDA',
    color: '#090F14',
    borderRadius: 6,
    padding: 16,
    fontSize: 16,
    width: '100%',
  },
  suggestionsContainer: {
    width: '100%',
    maxHeight: 150,
    overflow: 'hidden',
    marginTop: 0,
    paddingTop: 0,
  },
  suggestion: {
    backgroundColor: GlobalStyles.colors.secondary,
    borderWidth: 1,
    borderColor: GlobalStyles.colors.secondary,
    padding: 10,
    marginBottom: 2,
    marginTop: 0,
    borderRadius: 6,
  },
  suggestionText: {
    color: '#FFFFFF',
    fontSize: 16,
  },
  italicInfo: {
    fontSize: 12,
    fontStyle: 'italic',
    color: '#FFFFFF',
    textAlign: 'center',
    marginVertical: 0,
  },
  noMarginText: {
    marginBottom: 0,
    marginTop: 0,
  },
});

export default EmailInput;
