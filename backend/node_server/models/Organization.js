// backend/models/Organization.js
const mongoose = require('mongoose');

const organizationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  domain: { type: String, required: true, unique: true },
  users: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }],
  // apiUrl: { type: String, required: true },
  civicrmBaseRoute: { type: String, required: true },
  apiKey: { type: String, required: true },
  key: { type: String, required: true },
  api4Route: { type: String, required: true },
  logo: {type: String},
  jwtSecret: { type: String, required: true }  // Add JWT secret field
});

module.exports = mongoose.model('Organization', organizationSchema);

