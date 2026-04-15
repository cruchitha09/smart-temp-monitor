const { spawn } = require("child_process");

function getPrediction(data) {
  return new Promise((resolve, reject) => {

    const py = spawn("python", [
      "../ml-model/predict.py",
      JSON.stringify(data)
    ]);

    let result = "";

    py.stdout.on("data", (data) => {
      result += data.toString();
    });

    py.stderr.on("data", (err) => {
      reject(err.toString());
    });

    py.on("close", () => {
  const cleaned = result.trim();

  const num = parseFloat(cleaned);

  if (isNaN(num)) {
    return reject("Invalid ML output: " + cleaned);
  }

  resolve(num);
});

  });
}

module.exports = { getPrediction };