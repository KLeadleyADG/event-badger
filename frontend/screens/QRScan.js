import React, { useState, useEffect, useCallback } from "react";
import { Text, View, StyleSheet, Alert } from "react-native";
import { CameraView, Camera } from "expo-camera";
import { useRoute } from "@react-navigation/native";
import { GlobalStyles } from "../constants/styles";
import { addSubEvent } from "../api/fetch";
import ModalMessage from "../components/ui/ModalMessage";
import Button from '../components/ui/Button';

export default function QRScan() {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false);
  const [qrData, setQrData] = useState({});
  const [modalVisible, setModalVisible] = useState(false);
  const [modalMessage, setModalMessage] = useState("");

  const route = useRoute();
  const subEventParticipant = route.params.subEvent;

  useEffect(() => {
    const getCameraPermissions = async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === "granted");
    };

    getCameraPermissions();
  }, []);

  const handleBarCodeScanned = useCallback(({ type, data }) => {
    console.log("Scanned");
    setScanned(true);
    const splitData = data.split("-");
    const qrDataObject = {
      eId: splitData[0],
      cId: splitData[1],
      pId: splitData[2],
      first: splitData[3],
      last: splitData[4],
      role: splitData[5],
      status: splitData[6],
      contributionStatus: splitData[7],
      subEvents: splitData[8]
    };
    setQrData(qrDataObject);
    console.log(qrDataObject);
    checkAccessGranted(subEventParticipant, qrDataObject);
  }, [subEventParticipant]);

  const checkAccessGranted = useCallback(async (subEventParticipant, qrDataObject) => {
    if (qrDataObject.subEvents.includes(subEventParticipant.label)) {
      const incompleteStatusCodes = [2, 3, 4, 8];
      if (incompleteStatusCodes.includes(qrDataObject.contributionStatus)) {
        Alert.alert(
          'Incomplete Payment',
          'The participant has not fully paid for the event.',
          [
            {
              text: 'Cancel',
              onPress: () => setScanned(false),
              style: 'cancel',
            },
            {
              text: 'Okay',
              onPress: async () => {
                const entityRecord = {
                  entity_id: qrDataObject.cId,
                  Event_Id: qrDataObject.eId,
                  Event_Name_2: subEventParticipant.event_title,
                  Price_Field: subEventParticipant.label,
                  Date: subEventParticipant.date,
                };
                try {
                  const result = await addSubEvent(entityRecord);
                  setModalMessage(result.error ? 
                    `Participant ${qrDataObject.first} ${qrDataObject.last} has already been recorded` : 
                    `Thank you for attending ${subEventParticipant.label}, ${qrDataObject.first} ${qrDataObject.last}`);
                } catch {
                  setModalMessage("An error occurred while recording the participant.");
                }
                setModalVisible(true);
              }
            }
          ],
          { cancelable: false }
        );
        return;
      }

      const entityRecord = {
        entity_id: qrDataObject.cId,
        Event_Id: qrDataObject.eId,
        Event_Name_2: subEventParticipant.event_title,
        Price_Field: subEventParticipant.label,
        Date: subEventParticipant.date,
      };
      try {
        const result = await addSubEvent(entityRecord);
        setModalMessage(result.error ? 
          `Participant ${qrDataObject.first} ${qrDataObject.last} has already been recorded` : 
          `Thank you for attending ${subEventParticipant.label}, ${qrDataObject.first} ${qrDataObject.last}`);
      } catch {
        setModalMessage("An error occurred while recording the participant.");
      }
    } else {
      setModalMessage(`${qrDataObject.first} ${qrDataObject.last} has not registered for ${subEventParticipant.label}.`);
    }
    setModalVisible(true);
  }, [subEventParticipant]);

  const closeModal = () => setModalVisible(false);

  if (hasPermission === null) {
    return <Text>Requesting for camera permission</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <CameraView
        barcodeScannerSettings={{
          barcodeTypes: ["qr","pdf417"],
        }}
        onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
        style={StyleSheet.absoluteFillObject}
      />
      <View style={styles.overlay}>
        <Text style={styles.subEventText}>Scanning for: {subEventParticipant.event_title} - {subEventParticipant.label}</Text>
      </View>
      {scanned && (
        <View style={styles.bottomOverlay}>
          <Button onPress={() => {
            setScanned(false);
            setQrData({}); // Reset QR code data
          }}>
            Scan Again
          </Button>
        </View>
      )}

      <ModalMessage
        visible={modalVisible}
        message={modalMessage}
        onClose={closeModal}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
  },
  overlay: {
    position: 'absolute',
    top: 10,
    left: 0,
    right: 0,
    alignItems: 'center',
    zIndex: 1,
  },
  subEventText: {
    fontSize: 18,
    color: 'white',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    padding: 10,
    borderRadius: 5,
  },
  bottomOverlay: {
    position: 'absolute',
    bottom: 20,
    left: 0,
    right: 0,
    alignItems: 'center',
    zIndex: 1,
    padding: 20,
    fontSize: 38,
  },
});
