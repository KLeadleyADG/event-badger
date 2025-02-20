const bcrypt = require('bcrypt');
const crypto = require('crypto');
const nodemailer = require('nodemailer');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const Organization = require('../models/Organization');

// Login User
exports.loginUser = async (req, res) => {
  try {
    const { email, password } = req.body;
    console.log('Login attempt with email:', email);

    // Check if user exists
    const user = await User.findOne({ email: { $regex: new RegExp('^' + email + '$', 'i') } });
    if (!user) {
      return res.status(400).json({ message: 'Invalid credentials.' });
    }

    // Check if password is correct
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      console.log('Password does not match');
      return res.status(400).json({ message: 'Invalid credentials.' });
    }

    // Check if user is activated
    if (!user.activated) {
      console.log('User not activated');
      return res.status(400).json({ message: 'Account not activated.' });
    }

    // Extract domain from email and find the organization
    const domain = email.split('@')[1];
    const organization = await Organization.findOne({ domain });
    if (!organization) {
      return res.status(400).json({ message: 'Organization not found.' });
    }

    // Create and send token using the organization's JWT secret
    const token = jwt.sign({ userId: user._id }, organization.jwtSecret, { expiresIn: '1h' });

    res.status(200).json({ token });
  } catch (err) {
    console.error('Error logging in user:', err);
    res.status(500).json({ message: 'Server error.', error: err });
  }
};

// Register User
exports.registerUser = async (req, res) => {
  try {
    console.log("registerUser");
    console.log(req.body);
    const { email, password } = req.body;

    // Convert email to lowercase
    const emailLowerCase = email.toLowerCase();

    // Check if user already exists
    let user = await User.findOne({ email: { $regex: new RegExp('^' + emailLowerCase + '$', 'i') } });
    if (user) {
      return res.status(400).json({ message: 'User already exists.' });
    }

    // Extract domain from email
    const emailDomain = emailLowerCase.split('@')[1];

    // Check if the domain is authorized
    let organization = await Organization.findOne({ domain: emailDomain });
    if (!organization) {
      return res.status(400).json({ message: 'Email domain is not authorized.' });
    }

    // Hash the password
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    // Create verification token
    const verificationToken = crypto.randomBytes(20).toString('hex');

    // Create user
    user = new User({
      email: emailLowerCase,
      password: hashedPassword,
      organization: organization._id,
      verificationToken,
    });

    await user.save();

    // Add user to organization's user list
    organization.users.push(user._id);
    await organization.save();

    // Send verification email
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'colokurt9@gmail.com',
        pass: 'tvdo gnph apit buar', // App password
      },
    });

    const mailOptions = {
      from: 'colokurt9@gmail.com',
      to: user.email,
      subject: 'Account Verification',
      text: `Please verify your account by clicking the following link: \nhttp://${req.headers.host}/api/users/verify/${verificationToken}`,
    };

    transporter.sendMail(mailOptions, (err, info) => {
      if (err) {
        console.error('Error sending email:', err);
        return res.status(500).json({ message: 'Error sending verification email.', error: err });
      }
      res.status(200).json({ message: 'Verification email sent.' });
    });

  } catch (err) {
    console.error('Error registering user:', err);
    res.status(500).json({ message: 'Server error.', error: err });
  }
};

// Verify User
exports.verifyUser = async (req, res) => {
  console.log(req.params);
  try {
    const user = await User.findOne({ verificationToken: req.params.token });

    if (!user) {
      return res.status(400).json({ message: 'Invalid or expired token.' });
    }

    user.activated = true;
    delete user.verificationToken; 
    await user.save();

    res.status(200).json({ message: 'Account verified successfully.' });
  } catch (err) {
    console.error('Error verifying user:', err);
    res.status(500).json({ message: 'Server error.', error: err });
  }
};

// Request Password Reset
exports.requestPasswordReset = async (req, res) => {
  try {
    const { email } = req.body;
    const user = await User.findOne({ email: { $regex: new RegExp('^' + email + '$', 'i') } });

    if (!user) {
      return res.status(400).json({ message: 'User with this email does not exist.' });
    }

    // Generate reset code
    const resetCode = Math.floor(100000 + Math.random() * 900000).toString(); // 6 digit code
    user.resetPasswordToken = resetCode;
    user.resetPasswordExpires = Date.now() + 3600000; // 1 hour

    await user.save();

    // Send reset email
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'colokurt9@gmail.com',
        pass: 'tvdo gnph apit buar', // App password
      },
    });

    const mailOptions = {
      from: 'colokurt9@gmail.com',
      to: user.email,
      subject: 'Password Reset',
      html: `
        <p>You are receiving this because you (or someone else) have requested to reset your password for your account.</p>
        <p>Your reset code is: <strong>${resetCode}</strong></p>
        <p>If you did not request this, please ignore this email and your password will remain unchanged.</p>
      `,
    };

    transporter.sendMail(mailOptions, (err, info) => {
      if (err) {
        console.error('Error sending email:', err);
        return res.status(500).json({ message: 'Error sending password reset email.', error: err });
      }
      res.status(200).json({ message: 'Password reset email sent.' });
    });
  } catch (err) {
    console.error('Error requesting password reset:', err);
    res.status(500).json({ message: 'Server error.', error: err });
  }
};

// Reset Password using Reset Code
exports.resetPassword = async (req, res) => {
  try {
    const { resetCode, password } = req.body;
    const user = await User.findOne({
      resetPasswordToken: resetCode,
      resetPasswordExpires: { $gt: Date.now() },
    });

    if (!user) {
      return res.status(400).json({ message: 'Password reset code is invalid or has expired.' });
    }

    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    user.password = hashedPassword;
    user.resetPasswordToken = undefined; // Remove the token
    user.resetPasswordExpires = undefined; // Remove the token expiration

    await user.save();

    res.status(200).json({ message: 'Password has been reset successfully.' });
  } catch (err) {
    console.error('Error resetting password:', err);
    res.status(500).json({ message: 'Server error.', error: err });
  }
};

// Set Pin
exports.setPin = async (req, res) => {
  console.log("Set Pin API");
  const { email, pin } = req.body;
  try {
    const user = await User.findOne({ email: email.toLowerCase() });
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    user.pin = pin;
    await user.save();
    res.status(200).json({ message: 'PIN set successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
// Get Pin
exports.getPin = async (req, res) => {
  const { email } = req.body;
  try {
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    res.status(200).json({ pin: user.pin });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
// Test Connection
exports.testConnection = async (req, res) => {
  try {
    const email = 'leadleyk@adgcommunications.com';
    console.log(`Querying user with email: ${email}`);
    
    const user = await User.findOne({ email });
    if (user) {
      console.log('User found:', user);
      res.json({ message: 'Connection successful!', user });
    } else {
      console.log('User not found');
      res.status(404).json({ message: 'User not found' });
    }
  } catch (err) {
    console.error(`Error querying user: ${err.message}`);
    res.status(500).json({ message: `Error: ${err.message}` });
  }
};
