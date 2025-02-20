// frontend/constants/api
let apiConfig = {};

export const setApiConfig = (config) => {
  apiConfig = { ...apiConfig, ...config };
};

export const getApiConfig = () => {
  return apiConfig;
};