export const GlobalStyles = {
  colors: {
    primary: "#344450",
    secondary: "#6fa2d0",
    secondaryDark: "#4f82b0",
    accent: "#BFCFDA",
    white: "#ffffff",
    offWhite: "#F8F9FA"  // Added off-white color
  },
  container: {
    flex: 1,
    backgroundColor: '#344450',
  },
  contentContainer: {
    justifyContent: 'center',
    flex: 0,
    paddingHorizontal: 16,
    marginVertical: 20,
  },
  inputContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  bottomContainer: {
    justifyContent: 'center',
    alignItems: 'center', // Center the button horizontally
    width: '100%',
    position: 'absolute',
    bottom: 20, // Add some spacing from the bottom
    left: 0,
    right: 0,
    padding: 16,
    backgroundColor: '#344450',
  },
  textInput: {
    borderWidth: 1,
    borderColor: '#BFCFDA',
    backgroundColor: '#BFCFDA',
    color: '#090F14',
    borderRadius: 6,
    width: '100%',
    padding: 16,
    margin: 20,
    fontSize: 16,
  },
  errorMessage: {
    fontSize: 18,
    color: '#F8F9FA',  // Updated to off-white color
    backgroundColor: '#FF6347',
    width: '100%',
    textAlign: 'center',
    padding: 16,
  },
  successMessage: {
    color: '#ffffff',
    textAlign: 'center',
    fontSize: 18,
    backgroundColor: '#1e90ff',
    width: '100%',
    padding: 16,
  },
  headerText: {
    color: '#FFFFFF',
    fontSize: 28,
    textAlign: 'center',
    marginBottom: 20,
    marginTop: 20,
  },
  infoText: {
    color: '#FFFFFF',
    fontSize: 22,
    textAlign: 'center',
    marginBottom: 20,
    marginTop: 20,
  },
  contentText: {
    color: '#FFFFFF',
    fontSize: 18,
    textAlign: 'left',
    marginBottom: 20,
  },
  passwordContainer: {
    alignItems: 'center',
    marginTop: 5,
  },
  passwordText: {
    color: '#1e90ff',
    textAlign: 'center',
    fontSize: 16,
  },
  messageContainer: {
    marginVertical: 10,
  },
  // ios specific
  centerContent: {
    alignSelf: 'center',
    width: '80%',
    position: 'absolute',
    top: '25%',
  },
  // end ios specific
};
