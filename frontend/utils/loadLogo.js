// frontend/utils/loadLogo.js
import logos from '../assets/logos/logos';

export const loadLogo = (logoName) => {
  return logos[logoName] || logos['defaultLogo.png'];
};