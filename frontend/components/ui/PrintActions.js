import React from 'react';
import { View } from 'react-native';
import Button from '../ui/Button';
import Badge from '../ui/Badge';

const PrintActions = ({ badgeIsVisible, participant, qrCode, qrCodeRef, printOnPress }) => {
  if (!badgeIsVisible) return null;

  return (
    <View>
      <Button onPress={printOnPress}>Print</Button>
      {qrCode && (
        <Badge
          ref={qrCodeRef}
          first_name={participant.first_name}
          last_name={participant.last_name}
          id={participant.id}
          eId={participant.eId}
          participant_id={participant.participant_id}
          subEvents={participant.subEvents}
        />
      )}
    </View>
  );
};

export default PrintActions;
