const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const userRoutes = require('./routes/userRoutes');
const configRoutes = require('./routes/configRoutes');
const printerRoutes = require('./routes/printerRoutes');
const cors = require('cors');

// Load environment variables from .env file
dotenv.config({path: '../../.env' });
console.log(`MONGO_URI: ${process.env.MONGO_URI}`);
console.log(`PORT: ${process.env.PORT}`);
// Connect to MongoDB
connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api/users', userRoutes);
app.use('/api', configRoutes);
app.use('/api/printers', printerRoutes);

const PORT = process.env.PORT || 5000;

app.get('/stop', (req, res) => {
  res.send('Stopping server...');
  process.exit();
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
});
