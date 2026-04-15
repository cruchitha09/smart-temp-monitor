const express = require("express");
const cors = require("cors");

const predictionRoutes = require("./routes/prediction");

const app = express();

app.use(cors());
app.use(express.json());

// Routes
app.use("/api", predictionRoutes);

app.listen(5000, () => {
  console.log("Server running on port 5000");
});