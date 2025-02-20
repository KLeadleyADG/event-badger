const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      dbName: 'EventBadger'
    });

    console.log(`MongoDB connected... at ${process.env.MONGO_URI}`);
  } catch (err) {
    console.error(`Error connecting to MongoDB at ${process.env.MONGO_URI} : ${err.message}`);
    process.exit(1);
  }
};

module.exports = connectDB;
