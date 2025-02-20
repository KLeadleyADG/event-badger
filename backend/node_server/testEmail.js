const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'colokurt9@gmail.com',
    pass: 'tvdo gnph apit buar', // App password
  },
});

const mailOptions = {
  from: 'colokurt9@gmail.com',
  to: 'colokurt9@gmail.com', // Change to your test email
  subject: 'Test Email',
  text: 'This is a test email.',
};

transporter.sendMail(mailOptions, (err, info) => {
  if (err) {
    console.error('Error sending email:', err);
  } else {
    console.log('Email sent:', info.response);
  }
});
