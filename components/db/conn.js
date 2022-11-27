const { MongoClient } = require("mongodb");
const { config } = require("dotenv");
config();

const uri = process.env.MONGO_URI;
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

let isConnected = false;
const connect = async () => {
  if (!isConnected) {
    await client.connect();
    isConnected = true;
  }
};

module.exports = { connect, client };
