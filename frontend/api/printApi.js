import axios from 'axios';
import { getApiConfig } from '../constants/api';

export const printBadge = async (badgeData) => {
  console.log("Print Api - Badge Data:");
  console.log(badgeData);
  const apiConfig = getApiConfig();
  console.log(apiConfig);
  if (!apiConfig.printer || !apiConfig.printer.name || !apiConfig.printer.ip) {
    throw new Error('Printer details are required');
  }

  const dataToSend = {
    ...badgeData,
    printer: {
      ip: apiConfig.printer.ip,
      name: apiConfig.printer.name,
    },
  };
  try {
    const trimmedUrl = apiConfig.apiUrl.split(':5000')[0];
    console.log(trimmedUrl);
    const response = await axios.post(`${trimmedUrl}:5001/print-badge`, dataToSend, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error printing badge:', error.response ? error.response.data : error.message);
    throw error;
  }
};
