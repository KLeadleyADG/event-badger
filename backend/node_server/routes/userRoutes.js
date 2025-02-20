const express = require('express');
const { registerUser, verifyUser, loginUser, requestPasswordReset, resetPassword, getPin, setPin, testConnection } = require('../controllers/userController');

const router = express.Router();

// Register user
router.post('/register', registerUser);
// Verify user
router.get('/verify/:token', verifyUser);
// Log in user
router.post('/login', loginUser);
// Request password reset
router.post('/requestPasswordReset', requestPasswordReset);
// Reset password using reset code
router.post('/reset', resetPassword);
// Set Pin
router.post('/setPin', setPin);
// Get Pin
router.post('/getPin', getPin);
// Test connection
router.get('/test', testConnection);

module.exports = router;

