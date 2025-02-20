// frontend/api/fetch.js
import { getApiConfig, setApiConfig } from '../constants/api';
import axios from 'axios';
import { API_IP_ADDRESS } from '@env';


export async function fetchApi3(entity) {
  const api = getApiConfig();
  try {
    const endPoint = `${api.baseRoute}?entity=${entity}&json={"sequential":1}&api_key=${api.apiKey}&key=${api.key}&action=get`;
    const response = await fetch(endPoint);
    const data = await response.json();
    return data.values;
  } catch (error) {
    console.error(error);
  }
}


export async function fetchEvents() {
  console.log("Fetching Events");
  const api = getApiConfig();
  const endPoint = `${api.baseRoute}?entity=Event&json={"sequential":1}&api_key=${api.apiKey}&key=${api.key}&action=get`;

  console.log("Endpoint: " + endPoint);

  try {
    const response = await axios.get(endPoint);
    //console.log("Response: ", response.data.values);
    return response.data.values;
  } catch (error) {
    console.log("Error with fetchEvents()");
    console.error("Error details: ", error.toJSON ? error.toJSON() : error);
    if (error.response) {
      console.error('Data:', error.response.data);
      console.error('Status:', error.response.status);
      console.error('Headers:', error.response.headers);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('Request:', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Message:', error.message);
    }
    throw error; // Ensure the error is propagated
  }
}

export async function fetchParticipants(eId) {
  console.log("Fetch Participants");
  const api = getApiConfig();
  try {
    const endPoint = `${api.baseRoute}?entity=Participant&action=get&json={"sequential":1,"event_id":${eId}}&api_key=${api.apiKey}&key=${api.key}`;
    const response = await fetch(endPoint);
    const data = await response.json();
    return data.values;
  } catch (error) {
    console.error(error);
  }
}

export async function fetchContacts() {
  const api = getApiConfig();
  try {
    const endPoint = `${api.baseRoute}?entity=Contact&action=get&json={"sequential":1}&api_key=${api.apiKey}&key=${api.key}`;
    const response = await fetch(endPoint);
    const data = await response.json();
    return data.values;
  } catch (error) {
    console.error(error);
  }
}

export async function fetchApi4(entity) {
  const api = getApiConfig();
  const endPoint = api.api4EndPoint + entity + "/GET";
  try {
    const response = await fetch(endPoint, {
      method: "POST",
      headers: {
        "Content-Type" : "application/x-www-form-urlencoded",
        "X-Civi-Auth" : "Bearer " + api.apiKey
      },
    });
    const data = await response.json();
    return data.values;
  } catch (error) {
    console.error(error);
  }
}

// Update Participant to "Attended"
export async function updateParticipant(id) {
  const api = getApiConfig();
  console.log("Update Participant");
  const participantId = id;
  const endPoint = `${api.api4EndPoint}Participant/update`;
  
  const params = {
    values: { status_id: 2 },
    where: [[ 'id', '=', participantId ]]
  };

  const payload = new URLSearchParams();
  payload.append('params', JSON.stringify(params));

  console.log("Payload:", payload.toString());

  try {
    const response = await fetch(endPoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Civi-Auth": `Bearer ${api.apiKey}`
      },
      body: payload.toString()
    });

    if (!response.ok) {
      const errorResponse = await response.json();
      throw new Error(errorResponse.error_message || 'Unknown error');
    }

    const result = await response.json();
    console.log(result);
    return result;
  } catch (error) {
    console.error('Error updating participant:', error.message);
    return { error: error.message };
  }
}

export async function addSubEvent(data) {
  const api = getApiConfig();
  console.log("Add Subevent");

  const isDuplicate = await checkDuplicate(data);
  if (isDuplicate) {
    console.log("Duplicate entry detected, not adding subevent.");
    return { error: 'Duplicate entry detected' };
  }

  const endPoint = `${api.api4EndPoint}Custom_Sub_Events/create`;

  const params = {
    values: {
      entity_id: data.entity_id,
      Event_ID: data.Event_Id, // Ensure the field names match the API expectations
      Event_Name: data.Event_Name_2, // Ensure the field names match the API expectations
      Price_Field: data.Price_Field,
      Date: data.Date,
    },
  };

  const payload = new URLSearchParams();
  payload.append('params', JSON.stringify(params));

  console.log("Payload:", payload.toString());

  try {
    const response = await fetch(endPoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Civi-Auth": `Bearer ${api.apiKey}`,
      },
      body: payload.toString(),
    });

    if (!response.ok) {
      const errorResponse = await response.json();
      throw new Error(errorResponse.error_message || 'Unknown error');
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Error adding subevent:', error.message);
    return { error: error.message };
  }
}

export async function checkDuplicate(data) {
  const api = getApiConfig();
  const endPoint = `${api.api4EndPoint}Custom_Sub_Events/get`;

  const params = {
    where: [
      ['entity_id', '=', data.entity_id],
      ['Event_ID', '=', data.Event_Id],
      ['Price_Field', '=', data.Price_Field]
    ]
  };

  const payload = new URLSearchParams();
  payload.append('params', JSON.stringify(params));

  try {
    const response = await fetch(endPoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Civi-Auth": `Bearer ${api.apiKey}`
      },
      body: payload.toString()
    });

    const result = await response.json();
    return result.values.length > 0;
  } catch (error) {
    console.error('Error checking duplicate:', error.message);
    return false;
  }
}

export const fetchApiConfig = async (userToken) => {
  const api = getApiConfig();
  try {
    console.log('Fetching API config with token:', userToken);  // Log the token being used
      const response = await axios.get(`${api.apiUrl}/api/config`, {
      headers: {
        Authorization: `Bearer ${userToken}`,
      },
    });
    console.log(response.data);
    setApiConfig(response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching API config:', error);
    throw error;
  }
};

export const fetchApiUrl = async () => {
  console.log("fetchApiUrl");

  try {
    const ip = API_IP_ADDRESS; // Read the IP address from the environment variable
    const apiUrl = `http://${ip}:5000`;
    console.log(apiUrl);
    setApiConfig({ apiUrl });
    return apiUrl;
  } catch (error) {
    console.error('Error fetching API URL:', error);
    throw error;
  }
};