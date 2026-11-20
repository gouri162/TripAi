# TripAI Backend

This is a simple backend for your **AI Based Travel Assistance using customisation of packages across multiple platforms** project.

## Features

- Compare travel packages across multiple platforms
- Generate AI-style recommendations based on destination, budget, duration, and interests
- Expose destination and platform master data
- Save bookings
- Create price alerts
- Support assistant chat responses for your frontend

## Project Structure

```text
tripai-backend/
  src/
    data/
    routes/
    services/
    store/
    utils/
    app.js
    server.js
```

## API Endpoints

### `GET /`
Health check endpoint.

### `GET /api/meta/platforms`
Returns supported booking platforms.

### `GET /api/meta/destinations`
Returns supported destinations and their metadata.

### `POST /api/search/packages`
Searches and compares packages.

Example request body:

```json
{
  "destination": "Goa",
  "departureCity": "Delhi",
  "duration": "5 Days / 4 Nights",
  "travelDate": "2026-05-10",
  "travellers": "2 Adults",
  "budgetPerPerson": 35000,
  "interests": ["Beach", "Nightlife", "Relaxation"],
  "category": "Holiday Package"
}
```

### `POST /api/bookings`
Creates a booking.

### `GET /api/bookings`
Returns all bookings.

### `POST /api/bookings/alerts`
Creates a price alert.

### `GET /api/bookings/alerts`
Returns all price alerts.

### `POST /api/assistant/chat`
Returns AI-style assistant guidance.

Example request body:

```json
{
  "prompt": "Tell me more about the best value package",
  "searchContext": {
    "destination": "Goa",
    "budgetPerPerson": 35000,
    "interests": ["Beach", "Nightlife"]
  }
}
```

## How To Run

1. Open terminal in [tripai-backend](C:/Users/Kriyanshu/Documents/Codex/2026-04-21-files-mentioned-by-the-user-ai-2/tripai-backend)
2. Run `npm install`
3. Copy `.env.example` to `.env`
4. Run `npm run dev`

The backend will start on `http://localhost:5000`.

## Frontend Integration

Replace the current mock `searchPackages()` logic with an API call like this:

```js
async function searchPackages() {
  const payload = {
    destination: document.getElementById('dest').value,
    departureCity: document.getElementById('from').value,
    duration: document.getElementById('dur').value,
    travelDate: document.getElementById('tdate').value,
    travellers: document.getElementById('travellers').value,
    budgetPerPerson: parseInt(document.getElementById('budgetSlider').value, 10),
    interests: [...document.querySelectorAll('.interest-chip.selected')].map((el) =>
      el.textContent.trim()
    ),
    category: document.querySelector('.stab.active').textContent.trim()
  };

  const response = await fetch('http://localhost:5000/api/search/packages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result.data);
}
```

## Note

This backend uses an in-memory store, which is ideal for a college project demo. If you want, the next step can be:

- MongoDB backend
- MySQL backend
- User login and signup
- Admin panel
- Real payment integration
- Real AI integration using OpenAI or another model# TripAI Backend

This is a simple backend for your **AI Based Travel Assistance using customisation of packages across multiple platforms** project.

## Features

- Compare travel packages across multiple platforms
- Call 2-3 provider APIs and return the cheapest normalized result
- Generate AI-style recommendations based on destination, budget, duration, and interests
- Expose destination and platform master data
- Save bookings
- Create price alerts
- Support assistant chat responses for your frontend

## Project Structure

```text
tripai-backend/
  src/
    data/
    routes/
    services/
    store/
    utils/
    app.js
    server.js
```

## API Endpoints

### `GET /`
Health check endpoint.

### `GET /api/meta/platforms`
Returns supported booking platforms.

### `GET /api/meta/destinations`
Returns supported destinations and their metadata.

### `POST /api/search/packages`
Searches and compares packages.

### `POST /api/providers/compare`
Calls 3 provider connectors in parallel and returns the cheapest package plus all normalized results.

Example request body:

```json
{
  "destination": "Goa",
  "departureCity": "Delhi",
  "travelDate": "2026-05-10",
  "duration": "5 Days / 4 Nights",
  "travellers": "2 Adults"
}
```

Example request body:

```json
{
  "destination": "Goa",
  "departureCity": "Delhi",
  "duration": "5 Days / 4 Nights",
  "travelDate": "2026-05-10",
  "travellers": "2 Adults",
  "budgetPerPerson": 35000,
  "interests": ["Beach", "Nightlife", "Relaxation"],
  "category": "Holiday Package"
}
```

### `POST /api/bookings`
Creates a booking.

### `GET /api/bookings`
Returns all bookings.

### `POST /api/bookings/alerts`
Creates a price alert.

### `GET /api/bookings/alerts`
Returns all price alerts.

### `POST /api/assistant/chat`
Returns AI-style assistant guidance.

Example request body:

```json
{
  "prompt": "Tell me more about the best value package",
  "searchContext": {
    "destination": "Goa",
    "budgetPerPerson": 35000,
    "interests": ["Beach", "Nightlife"]
  }
}
```

## How To Run

1. Open terminal in [tripai-backend](C:/Users/Kriyanshu/Documents/Codex/2026-04-21-files-mentioned-by-the-user-ai-2/tripai-backend)
2. Run `npm install`
3. Copy `.env.example` to `.env`
4. Run `npm run dev`

The backend will start on `http://localhost:5000`.

## Multi-API Setup

By default, the project uses `USE_MOCK_PROVIDERS=true`, so `/api/providers/compare` works with built-in mock data and shows how multi-provider comparison works.

To connect real APIs:

1. Set `USE_MOCK_PROVIDERS=false` in `.env`
2. Add real provider URLs and API keys
3. Update the mapper functions in [providerService.js](C:/Users/Kriyanshu/Documents/Codex/2026-04-21-files-mentioned-by-the-user-ai-2/tripai-backend/src/services/providerService.js) if the provider response shape is different

The provider adapter flow is:

```text
Frontend -> /api/providers/compare -> Provider 1
                                     -> Provider 2
                                     -> Provider 3
                                     -> Normalize -> Sort -> Cheapest result
```

## Frontend Integration

Replace the current mock `searchPackages()` logic with an API call like this:

```js
async function searchPackages() {
  const payload = {
    destination: document.getElementById('dest').value,
    departureCity: document.getElementById('from').value,
    duration: document.getElementById('dur').value,
    travelDate: document.getElementById('tdate').value,
    travellers: document.getElementById('travellers').value,
    budgetPerPerson: parseInt(document.getElementById('budgetSlider').value, 10),
    interests: [...document.querySelectorAll('.interest-chip.selected')].map((el) =>
      el.textContent.trim()
    ),
    category: document.querySelector('.stab.active').textContent.trim()
  };

  const response = await fetch('http://localhost:5000/api/search/packages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result.data);
}
```

## Note

This backend uses an in-memory store, which is ideal for a college project demo. If you want, the next step can be:

- MongoDB backend
- MySQL backend
- User login and signup
- Admin panel
- Real payment integration
- Real AI integration using OpenAI or another model