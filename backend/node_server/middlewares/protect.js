// backend/middlewares/authMiddleware.js
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const Organization = require('../models/Organization');

const protect = async (req, res, next) => {
  let token;

  if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
    try {
      token = req.headers.authorization.split(' ')[1];
      console.log('Received token:', token);

      const decoded = jwt.decode(token);
      console.log('Decoded token:', decoded);

      const user = await User.findById(decoded.userId).select('-password');
      if (!user) {
        console.log('User not found');
        return res.status(401).json({ message: 'Not authorized, user not found' });
      }

      const domain = user.email.split('@')[1];
      const organization = await Organization.findOne({ domain });
      if (!organization) {
        console.log('Organization not found');
        return res.status(401).json({ message: 'Not authorized, organization not found' });
      }

      console.log('Organization found:', organization);

      jwt.verify(token, organization.jwtSecret, (err, decoded) => {
        if (err) {
          console.log('Token verification failed:', err);
          return res.status(401).json({ message: 'Not authorized, token failed' });
        }
        console.log('Token verified:', decoded);
        req.user = user;
        next();
      });
    } catch (error) {
      console.error('Token processing failed:', error);
      res.status(401).json({ message: 'Not authorized, token failed' });
    }
  } else {
    res.status(401).json({ message: 'Not authorized, no token' });
  }
};

module.exports = { protect };
