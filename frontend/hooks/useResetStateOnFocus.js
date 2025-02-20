// frontend/hooks/useResetStateOnFocus.js
import { useEffect } from 'react';
import { useNavigation } from '@react-navigation/native';

const useResetStateOnFocus = (resetState) => {
  const navigation = useNavigation();

  useEffect(() => {
    const unsubscribe = navigation.addListener('focus', resetState);
    return unsubscribe;
  }, [navigation, resetState]);
};

export default useResetStateOnFocus;
