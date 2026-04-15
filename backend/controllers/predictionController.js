const { getPrediction } = require("../services/mlService");

exports.predictTemperature = async (req, res) => {
  try {

    // Dummy data (will replace later with DB)
    const temps = [28.7, 29.0, 29.3];

    const prediction = await getPrediction(temps);

    res.json({
      predictedTemperature: prediction
    });

  } catch (err) {
    res.status(500).json({ error: err });
  }
};