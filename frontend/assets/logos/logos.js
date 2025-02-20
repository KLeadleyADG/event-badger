import { Asset } from 'expo-asset';
import * as FileSystem from 'expo-file-system';

const logos = {
  'adg-tag-rgb.png': require('./adg-tag-rgb.png'),
  'defaultLogo.png': require('./adg-tag-rgb.png'),
  'ncbj.png': require('./ncbj.png'),
};

export const getLogoBase64 = async (logoName) => {
  try {
    const logo = logos[logoName] || logos['defaultLogo.png'];
    
    // Load and resolve the asset URI
    const asset = Asset.fromModule(logo);
    await asset.downloadAsync(); // Ensure the asset is downloaded

    // Read the file as base64
    const fileBase64 = await FileSystem.readAsStringAsync(asset.localUri, {
      encoding: FileSystem.EncodingType.Base64,
    });
    console.log(`Successfully read file as base64: ${logoName}`);
    return `data:image/png;base64,${fileBase64}`;
  } catch (error) {
    console.error(`Error in getLogoBase64 for ${logoName}:`, error);
    throw error;
  }
};

export default logos;

