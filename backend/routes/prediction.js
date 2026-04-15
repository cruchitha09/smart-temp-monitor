const express = require("express");
const router = express.Router();

const { predictTemperature } = require("../controllers/predictionController");

router.get("/predict", predictTemperature);

module.exports = router;