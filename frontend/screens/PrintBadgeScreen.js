import React, { useState, useEffect, useCallback, useRef } from 'react';
import { useRoute } from "@react-navigation/native";
import { View, Text, Alert, StyleSheet, ActivityIndicator, Platform } from 'react-native';
import { Dropdown } from 'react-native-element-dropdown';
import EmailVerificationModal from '../components/ui/EmailVerification';
import PinEntryModal from '../components/ui/PinEntryModal';
import Button from '../components/ui/Button';
import Badge from '../components/ui/Badge';
import { getApiConfig } from '../constants/api';
import { GlobalStyles } from '../constants/styles';
import { updateParticipant, fetchParticipants, fetchContacts, fetchApi3, fetchApi4 } from '../api/fetch';
import { printBadge } from '../api/printApi';
import { useUser } from '../context/UserContext';
import { getLogoBase64 } from '../assets/logos/logos';
import useBackHandlerAndStatusBar from '../hooks/useBackHandlerAndStatusBar';

function PrintBadgeScreen({ navigation }) {
  const { user } = useUser();
  const route = useRoute();
  const eventId = route.params.event.id;
  const api = getApiConfig();

  const [participants, setParticipants] = useState([]);
  const [modalIsVisible, setModalVisible] = useState(false);
  const [badgeIsVisible, setBadgeIsVisible] = useState(false);
  const [emailVerified, setEmailVerified] = useState(false);  
  const [selectedParticipant, setSelectedParticipant] = useState(null);
  const [participant, setParticipant] = useState({});
  const [pinPromptVisible, setPinPromptVisible] = useState(false);
  const [message, setMessage] = useState('');
  const [onSubmitPin, setOnSubmitPin] = useState(() => () => {});
  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const qrCodeRef = useRef(null);

  useBackHandlerAndStatusBar();

  useEffect(() => {
    async function getParticipants() {
      try {
        console.log("Fetching participants for event:", eventId);
        const participants = await fetchParticipants(eventId);
        const contacts = await fetchContacts();
        
        const filteredContacts = await Promise.all(
          contacts.map(async (c) => {
            const participant = participants.find((p) => p.contact_id === c.id);
            if (participant) {
              const { id, sort_name, first_name, last_name, email } = c;
              let feeLevels = participant.participant_fee_level;

              if (typeof feeLevels === 'string') {
                try {
                  feeLevels = JSON.parse(feeLevels);
                } catch (e) {
                  feeLevels = [];
                }
              }

              const trimmedFeeLevels = Array.isArray(feeLevels)
                ? feeLevels.map(item => item.split('-')[0].trim())
                : [];
              const contributionStatus = await getContributionData(participant.id);

              return {
                eId: eventId,
                id,
                sort_name,
                first_name,
                last_name,
                email,
                status: participant.participant_status,
                role: participant.participant_role,
                participant_id: participant.id,
                subEvents: trimmedFeeLevels,
                contributionStatus
              };
            }
            return null;
          })
        );

        const validContacts = filteredContacts.filter(contact => contact !== null);
        console.log(validContacts);
        setParticipants(validContacts);
      } catch (e) {
        console.log("Error fetching participants:", e);
      }
    }
    getParticipants();
  }, [eventId]);

  async function getContributionData(pId) {
    try {
      const partPayment = await fetchApi3("ParticipantPayment");
      const contributions = await fetchApi4("Contribution");
      const filteredPayments = partPayment.filter(payment => payment.participant_id === pId);
      if (filteredPayments.length === 0) {
        console.log("No payments found for the given participant ID.");
        return;
      }
      const contributionId = filteredPayments[0].contribution_id;
      const filteredContributions = contributions.filter(contribution => contribution.id == contributionId);
      return filteredContributions[0].contribution_status_id;
    } catch (error) {
      console.log("Error fetching data:", error);
    }
  }

  const resetState = () => {
    setModalVisible(false);
    setBadgeIsVisible(false);
    setEmailVerified(false);
    setParticipant({}); 
    setSelectedParticipant(null);
    setLoading(false);
    setSuccessMessage('');
  };

  const cancelOnPress = () => {
    setMessage('');
    setOnSubmitPin(() => validatePinAndNavigate);
    setPinPromptVisible(true);
  };

  const validatePinAndNavigate = async (pin) => {
    console.log("Validate Pin: " + pin);
    console.log (api.apiUrl);
    try {
      const response = await fetch(`${api.apiUrl}/api/users/getPin`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: user.email }),
      });

      const data = await response.json();
      if (response.ok && data.pin === (pin)) {
        setPinPromptVisible(false);
        resetState();
        navigation.navigate('SelectModeScreen');
      } else {
        Alert.alert('Invalid PIN', 'The PIN you entered is incorrect.');
      }
    } catch (err) {
      console.log('Error validating PIN:', err);
      Alert.alert('Error', 'An error occurred while validating the PIN.');
    }
  };

  const printOnPress = async () => {
    console.log("printOnPress");
    console.log(participant.contributionStatus);
    setLoading(true);
    // Quick if check for people who are not registered for a subevent. 
    const incompleteStatusCodes = [2, 3, 4, 8];
    if (incompleteStatusCodes.includes(participant.contributionStatus)) {
      setMessage('Incomplete Payment. Please See Association Manager for admittance.');
      setOnSubmitPin(() => async (pin) => {
        try {
          const response = await fetch(`${api.apiUrl}/api/users/getPin`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: user.email }),
          });
  
          const data = await response.json();
          if (response.ok && data.pin === pin) {
            await markAttended(participant);
            if (participant) {
              console.log("Attempt print()");
              await print();
              setSuccessMessage('Print job successful!');
              setBadgeIsVisible(false);
              setTimeout(resetState, 2000); // Show success message for 2 seconds before resetting state
              setLoading(false);
            } else {
              console.log('QR Code generation failed');
              setLoading(false);
            }
          } else {
            Alert.alert('Invalid PIN', 'The PIN you entered is incorrect.');
            setLoading(false);
          }
        } catch (err) {
          console.log('Error validating PIN:', err);
          Alert.alert('Error', 'An error occurred while validating the PIN.');
          setLoading(false);
        }
      });
      setPinPromptVisible(true);
      setLoading(false);
      return;
    }
  
    await markAttended(participant);
    // Back to normal situation where person is a valid attendee 
    if (participant) {
      console.log("Attempt print()");
      await print();
      setSuccessMessage('Print job successful!');
      setTimeout(resetState, 2000); // Show success message for 2 seconds before resetting state
      setLoading(false);
    } else {
      console.log('QR Code generation failed');
      setLoading(false);
    }
  };

  const markAttended = async (participant) => {
    try {
      await updateParticipant(participant.participant_id);
    } catch (e) {
      console.log("Error marking participant as attended:", e);
    }
  };

  const print = async () => {
    console.log("Print");
    console.log(participant);
    try {
      const logoBase64 = await getLogoBase64(api.logo);

      const badgeData = {
        participant,
        logoBase64,
      };
      await printBadge(badgeData);
    } catch (error) {
      console.log('Print error:', error);
    }
    setPinPromptVisible(false);
  };

  const endEmailVerification = () => {
    setModalVisible(false);
    setEmailVerified(true);
    setBadgeIsVisible(true);
  };

  const renderItem = useCallback((item) => (
    <View style={styles.item}>
      <Text style={styles.textItem}>{item.sort_name}</Text>
    </View>
  ), []);

  // Extract email domains from participants
  const emailDomains = participants
    .map(participant => participant.email.split('@')[1])
    .filter((value, index, self) => self.indexOf(value) === index); // Remove duplicates

  return (
    <View style={GlobalStyles.container}>
      <View style={[GlobalStyles.contentContainer, Platform.OS === 'ios' && GlobalStyles.centerContent]}>
        <EmailVerificationModal
          visible={modalIsVisible}
          email={participant.email}
          closeModal={endEmailVerification}
          resetState={resetState}
          domains={emailDomains}
        />
        <Text style={GlobalStyles.headerText}>Select Participant</Text>
        <View style={GlobalStyles.inputContainer}>
          <Dropdown
            style={styles.dropdown}
            placeholderStyle={styles.placeholderStyle}
            selectedTextStyle={styles.selectedTextStyle}
            inputSearchStyle={styles.inputSearchStyle}
            iconStyle={styles.iconStyle}
            data={participants}
            search
            maxHeight={300}
            labelField="sort_name"
            valueField="id"
            value={selectedParticipant}
            searchPlaceholder="Search..."
            onChange={item => {
              setParticipant(item);
              setSelectedParticipant(item.id);
            }}
            renderItem={renderItem}
          />
        </View>
        {selectedParticipant && !emailVerified && (
          <Button onPress={() => setModalVisible(true)} disabled={loading}>
            {loading ? (
              <ActivityIndicator size="small" color={GlobalStyles.colors.white} />
            ) : (
              "Submit"
            )}
          </Button>
        )}
        {badgeIsVisible && (
          <>
            <Badge
              ref={qrCodeRef}
              id={participant.id}
              eId={participant.eId}
              participant_id={participant.participant_id}
              subEvents={participant.subEvents}
              first_name={participant.first_name}
              last_name={participant.last_name}
              role={participant.role}
              status={participant.status}
              contributionStatus={participant.contributionStatus}
            />
            {(loading && <View style={styles.loading}>
              <Text style={GlobalStyles.infoText}>Printing...</Text>
              <ActivityIndicator style={styles.loading} size="large" color={GlobalStyles.colors.white}/>
            </View>)}
            {!loading &&(<Button onPress={printOnPress} disabled={loading}>Print</Button>)}
          </>
        )}
        {successMessage && (
          <Text style={styles.successMessage}>{successMessage}</Text>
        )}
      </View>
      {!loading && (
        <View style={GlobalStyles.bottomContainer}>
          <Button onPress={badgeIsVisible ? resetState : cancelOnPress} disabled={loading}>
            {badgeIsVisible ? 'Clear' : 'Cancel'}
          </Button>
        </View>
      )}
      <PinEntryModal
        visible={pinPromptVisible}
        message={message}
        onSubmit={onSubmitPin}
        onCancel={() => setPinPromptVisible(false)}
      />
    </View>
  );
}

export default PrintBadgeScreen;

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
  successMessage: {
    fontSize: 16,
    color: GlobalStyles.colors.secondary,
    marginTop: 10,
    textAlign: 'center',
  },
  loading: {
    marginTop:"30px"
  }
});
