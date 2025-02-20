const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  organization: { type: mongoose.Schema.Types.ObjectId, ref: 'Organization', required: true },
  activated: { type: Boolean, default: false },
  verificationToken: { type: String, required: true },
  resetPasswordToken: { type: String },
  resetPasswordExpires: { type: Date },
  pin: { type: String, default: '0000', match: /^[0-9]{4}$/ },
}, { timestamps: true });

module.exports = mongoose.model('User', userSchema);

