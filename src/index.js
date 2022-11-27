const express = require("express");
const morgan = require("morgan");
app = express();

// Settings
app.set("port", process.env.PORT || 8000);
app.set("json spaces", 2);

// Midelware
app.use(morgan("dev"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Routes
app.use(require("./routes/index"));
app.use(require("./routes/document"));
app.use(require("./routes/category"));
app.use(require("./routes/inventory"));

// Starting the server
app.listen(app.get("port"), () => {
  console.log("Server is running on port 8000");
});
