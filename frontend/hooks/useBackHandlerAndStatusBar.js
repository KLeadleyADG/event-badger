import { useEffect } from 'react';
import { BackHandler, StatusBar } from 'react-native';

const useBackHandlerAndStatusBar = () => {
  useEffect(() => {
    const backAction = () => {
      // Prevent the back button from doing anything
      return true;
    };

    const backHandler = BackHandler.addEventListener(
      "hardwareBackPress",
      backAction
    );

    StatusBar.setHidden(true); // Hide the status bar

    return () => {
      backHandler.remove();
      StatusBar.setHidden(false); // Show the status bar again
    };
  }, []);
};

export default useBackHandlerAndStatusBar;
