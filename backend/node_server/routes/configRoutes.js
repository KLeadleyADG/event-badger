// backend/routes/configRoutes.js
const express = require('express');
const router = express.Router();
const { getConfig } = require('../controllers/configController');
const { protect } = require('../middlewares/authMiddleware'); 

router.get('/config', protect, getConfig);

module.exports = router;