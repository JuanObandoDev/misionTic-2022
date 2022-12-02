import { MongoClient } from "mongodb";
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

export { connect, client };
