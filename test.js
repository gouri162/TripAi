require('dotenv').config({ path: './trip-backend/api.env' });

const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://travel-advisor.p.rapidapi.com/hotels/list',
  headers: {
    'X-RapidAPI-Key': process.env.RAPIDAPI_KEY,
    'X-RapidAPI-Host': process.env.RAPIDAPI_HOST
  },
  params: {
    location_id: '293919', // Delhi
    adults: '1',
    rooms: '1',
    nights: '2'
  }
};

axios.request(options)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });