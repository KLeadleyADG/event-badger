import React, { forwardRef, useEffect, useState } from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import QRCode from 'react-native-qrcode-svg';
import { getApiConfig } from '../../constants/api';
import { getLogoBase64 } from '../../assets/logos/logos';

const Badge = forwardRef((props, ref) => {
  const api = getApiConfig();
  const [logoBase64, setLogoBase64] = useState(null);

  useEffect(() => {
    async function loadLogo() {
      try {
        console.log('Loading logo...');
        const base64 = await getLogoBase64(api.logo);
        console.log('Logo loaded successfully');
        setLogoBase64(base64);
      } catch (error) {
        console.log('Error loading logo:', error);
      }
    }
    loadLogo();
  }, [api.logo]);

  useEffect(() => {
    if (ref?.current) {
      props.onQrCodeRendered && props.onQrCodeRendered();
    } else {
      console.log('QRCode ref is not set yet');
    }
  }, [ref]);

  // Log QR code value for debugging
  const qrCodeValue = `${props.id}-${props.eId}-${props.participant_id}-${props.subEvents}-${props.first_name}-${props.last_name}-${props.role}-${props.status}-${props.contributionStatus}`;

  return (
    <View
      style={styles.badge}
      ref={ref}
    >
      <Text style={styles.text}>
        {props.first_name} {props.last_name}
      </Text>
      <View style={styles.qrCode}>
        <QRCode
          value={qrCodeValue}
          size={100}
          color="black"
          backgroundColor="white"
          onError={(e) => console.log('QR Code generation error:', e)}
        />
      </View>
      {logoBase64 && (
        <Image
          style={styles.image}
          source={{ uri: logoBase64 }}
          onError={(e) => console.log('Error loading logo image:', e)}
        />
      )}
    </View>
  );
});

export default Badge;

const styles = StyleSheet.create({
  badge: {
    marginTop: 24,
    alignSelf: 'center',
    height: 243,
    width: 153,
    backgroundColor: '#fff',
    borderRadius: 8,
    padding: 16,
    justifyContent: 'space-between',
  },
  text: {
    fontSize: 14,
    alignSelf: 'center',
  },
  qrCode: {
    alignSelf: 'center',
    marginVertical: 16,
  },
  image: {
    width: '100%',
    height: 50,
    resizeMode: 'contain',
  },
});
