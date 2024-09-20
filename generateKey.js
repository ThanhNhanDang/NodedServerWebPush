const express = require("express");
const bodyParser = require("body-parser");
const webpush = require("web-push");

const app = express();
app.use(bodyParser.json());

const vapidKeys = {
  publicKey:
    "BP9B8yGHuvhJQM8RPCTBP0lEVHgdG1KAjJOKrLqFkKBe6NjeM3o5LWDykKCK7Y9KBK-iQD_QKY9WWwsnxyEMAtU",
  privateKey: "MPQ5syPiI_5gwJdIBpoWT7EKOEzLTYnCSePBWV7Xi4w",
};

webpush.setVapidDetails(
  "mailto:example@yourdomain.org",
  vapidKeys.publicKey,
  vapidKeys.privateKey
);

// Endpoint để gửi thông báo (cho mục đích thử nghiệm)
app.post("/send-notification", (req, res) => {
  const subscription = req.body.subscription;
  const payload = JSON.stringify({
    title: req.body.title || "Test Notification",
    body: req.body.body || "This is a test notification",
  });

  webpush
    .sendNotification(subscription, payload)
    .then(() => {
      res.status(200).json({ message: "Notification sent successfully." });
    })
    .catch((error) => {
      console.error("Error sending notification:", error);
      res.status(500).json({ error: "Failed to send notification." });
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
