module.exports = {
  dependencies: {
    'react-native-fs': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-full-screen': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-html-to-pdf': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-safe-area-context': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-screens': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-wifi-reborn': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
    'react-native-zeroconf': {
      platforms: {
        android: null, // disable autolinking for this dependency on Android
      },
    },
  },
  project: {
    ios: {},
    android: {
      watchModeCommandParams: [
        '--mode',
        'generalDebug',
      ],
    },
  },
};