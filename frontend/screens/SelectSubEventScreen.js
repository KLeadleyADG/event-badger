import React, { useState, useEffect, useCallback } from 'react';
import { Text, View, StyleSheet, ActivityIndicator, Platform } from 'react-native';
import { useRoute } from "@react-navigation/native";
import { Dropdown } from 'react-native-element-dropdown';
import Button from '../components/ui/Button';
import { GlobalStyles } from '../constants/styles';
import { fetchApi4 } from '../api/fetch';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function SelectSubEventScreen({ navigation }) {
  useBackHandlerAndStatusBar();
  const [subEvent, setSubEvent] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [subEvents, setSubEvents] = useState([]);
  
  const route = useRoute();
  const event = route.params?.event;

  const backOnPress = useCallback(() => {
    navigation.navigate('SelectModeScreen');
  }, [navigation]);

  const selectSubEvent = useCallback(() => {
    navigation.navigate('QRScan', { subEvent });
  }, [navigation, subEvent]);

  useEffect(() => {
    const getEventPriceFieldValues = async () => {
      if (event) {
        try {
          const priceSetEntities = await fetchApi4("PriceSetEntity");
          const priceSetId = priceSetEntities.find(item => String(item.entity_id) === String(event.id))?.price_set_id;
          if (priceSetId) {
            const allPriceFields = await fetchApi4("PriceField");
            const priceFields = allPriceFields.filter(item => item.price_set_id === priceSetId).map(item => item.id);
            const allPriceFieldVals = await fetchApi4("PriceFieldValue");
            const priceFieldVals = allPriceFieldVals
              .filter(item => priceFields.includes(item.price_field_id))
              .map(item => ({
                event: event.id,
                event_title: event.title,
                id: item.id,
                label: item.label,
                date: event.start_date,
              }));
              setSubEvents(priceFieldVals);
          } else {
            console.log("No matching price set ID found for event.");
          }
        } catch (e) {
          console.log(e);
        }
        setIsLoading(false);
      }
    };
    getEventPriceFieldValues();
  }, [event]);

  const renderItem = useCallback((item) => (
    <View style={styles.item}>
      <Text style={styles.textItem}>{item.label}</Text>
    </View>
  ), []);

  if (isLoading) {
    return (
      <View style={GlobalStyles.container}>
        <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
          <ActivityIndicator size="large" color={GlobalStyles.colors.secondary} />
          <Text style={GlobalStyles.headerText}>Loading Sub Events...</Text>
        </View>
        <View style={GlobalStyles.bottomContainer}>
          <Button onPress={backOnPress}>Back</Button>
        </View>
      </View>
    );
  }

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <Text style={GlobalStyles.headerText}>Select Sub Event</Text>
        <View style={GlobalStyles.inputContainer}>
          <Dropdown
            style={styles.dropdown}
            placeholderStyle={styles.placeholderStyle}
            selectedTextStyle={styles.selectedTextStyle}
            inputSearchStyle={styles.inputSearchStyle}
            iconStyle={styles.iconStyle}
            data={subEvents}
            search
            maxHeight={300}
            labelField="label"
            valueField="id"
            searchPlaceholder="Search..."
            onChange={item => setSubEvent(item)}
            renderItem={renderItem}
          />
        </View>
        <Button onPress={selectSubEvent}>Submit</Button>
      </View>
      <View style={GlobalStyles.bottomContainer}>
        <Button onPress={backOnPress}>Back</Button>
      </View>
    </View>
  );
}

export default SelectSubEventScreen;

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
