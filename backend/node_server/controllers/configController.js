// backend/controllers/configController.js
exports.getConfig = async (req, res) => {
  try {
    console.log('User in getConfig:', req.user);

    const organization = req.organization;
    if (!organization) {
      console.log('Organization not found in getConfig');
      return res.status(404).json({ message: 'Organization not found' });
    }

    res.json({
      apiUrl: organization.apiUrl,
      baseRoute: organization.civicrmBaseRoute,
      apiKey: organization.apiKey,
      key: organization.key,
      api4EndPoint: organization.api4Route,
      logo: organization.logo,
      jwtSecret: organization.jwtSecret  // Include JWT secret in the response
    });
  } catch (error) {
    console.error('Error in getConfig:', error);
    res.status(500).json({ message: 'Server error', error });
  }
};

