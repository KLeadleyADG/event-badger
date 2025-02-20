// /frontend/App.js
import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { UserProvider } from './context/UserContext';

import AdminLoginScreen from './screens/AdminLoginScreen';
import SelectModeScreen from './screens/SelectModeScreen';
import SelectEventScreen from './screens/SelectEventScreen';
import SelectSubEventScreen from './screens/SelectSubEventScreen';
import PrintBadgeScreen from './screens/PrintBadgeScreen';
import QRScan from './screens/QRScan';
import RegisterScreen from './screens/RegistrationScreen';
import RequestPasswordResetScreen from './screens/RequestPasswordResetScreen';
import ResetPasswordWithCodeScreen from './screens/ResetPasswordWithCodeScreen';
import SetPinScreen from './screens/SetPinScreen';
import SelectPrinterScreen from './screens/SelectPrinterScreen';
import { API_IP_ADDRESS } from '@env';
const Stack = createNativeStackNavigator();

export default function App() {
  console.log("Loaded API_IP_ADDRESS:", API_IP_ADDRESS);
  return (
    <UserProvider>
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName="AdminLoginScreen"
          screenOptions={{
            gestureEnabled: false, // Disable swipe back gestures globally
          }}
        >
          <Stack.Screen
            name="AdminLoginScreen"
            component={AdminLoginScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="SelectModeScreen"
            component={SelectModeScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="SelectEventScreen"
            component={SelectEventScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="SelectSubEventScreen"
            component={SelectSubEventScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="QRScan"
            component={QRScan}
            options={{ headerTitle: "ADG Event Badger"}}
          />
          <Stack.Screen
            name="PrintBadgeScreen"
            component={PrintBadgeScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="RegisterScreen"
            component={RegisterScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="RequestPasswordResetScreen"
            component={RequestPasswordResetScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="ResetPasswordWithCodeScreen"
            component={ResetPasswordWithCodeScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="SetPinScreen"
            component={SetPinScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="SelectPrinterScreen"
            component={SelectPrinterScreen}
            options={{ headerShown: false }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </UserProvider>
  );
}


