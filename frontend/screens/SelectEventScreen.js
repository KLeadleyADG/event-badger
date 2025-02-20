import React, { useState, useEffect, useCallback } from 'react';
import { Text, View, StyleSheet, Platform } from 'react-native';
import { useRoute } from "@react-navigation/native";
import { Dropdown } from 'react-native-element-dropdown';
import Button from '../components/ui/Button';
import { GlobalStyles } from '../constants/styles';
import { fetchEvents } from '../api/fetch';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function SelectEventScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const route = useRoute();
  const mode = route.params.mode;

  const [event, setEvent] = useState(null);
  const [events, setEvents] = useState([]);

  const backOnPress = useCallback(() => {
    navigation.navigate('SelectModeScreen');
  }, [navigation]);

  const selectEvent = useCallback(() => {
    if (event) {
      if (mode === "Badge") {
        navigation.navigate('PrintBadgeScreen', { event });
      } else if (mode === "QR") {
        navigation.navigate('SelectSubEventScreen', { event });
      }
    }
  }, [navigation, event, mode]);

  useEffect(() => {
    const getEvents = async () => {
      try {
        const events = await fetchEvents();
        setEvents(events);
      } catch (e) {
        console.log("Error Fetching Events");
        console.log(e);
      }
    };
    getEvents();
  }, []);

  const renderItem = useCallback((item) => (
    <View style={styles.item}>
      <Text style={styles.textItem}>{item.event_title}</Text>
    </View>
  ), []);

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <Text style={GlobalStyles.headerText}>Select Event</Text>
        <View style={GlobalStyles.inputContainer}>
          <Dropdown
            style={styles.dropdown}
            placeholderStyle={styles.placeholderStyle}
            selectedTextStyle={styles.selectedTextStyle}
            inputSearchStyle={styles.inputSearchStyle}
            iconStyle={styles.iconStyle}
            data={events}
            search
            maxHeight={300}
            labelField="event_title"
            valueField="id"
            searchPlaceholder="Search..."
            onChange={item => {
              setEvent(item);
            }}
            renderItem={renderItem}
          />
        </View>
        <Button onPress={selectEvent}>Submit</Button>
      </View>
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
      </View>
    </View>
  );
}

export default SelectEventScreen;

const styles = StyleSheet.create({
  dropdown: {
    height: 50,
    borderWidth: 0.5,
    borderRadius: 8,
    paddingHorizontal: 8,
    width: 350,
    backgroundColor: GlobalStyles.colors.white,
  },
  icon: {
    marginRight: 5,
  },
  placeholderStyle: {
    fontSize: 16,
  },
  selectedTextStyle: {
    fontSize: 16,
  },
  iconStyle: {
    width: 30,
    height: 30,
  },
  inputSearchStyle: {
    height: 40,
    fontSize: 16,
  },
  item: {
    backgroundColor: GlobalStyles.colors.white,
  },
  textItem: {
    padding: 6,
    marginBottom: 4,
  },
});
