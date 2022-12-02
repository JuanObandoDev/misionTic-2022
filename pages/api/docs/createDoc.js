import { createDoc } from "../../../database/db";

const createDocHandler = async (req, res) => {
  if (req.method === "POST") {
    try {
      const { doc } = req.body;
      await createDoc(doc);
      res.status(200).json({ success: true });
    } catch (e) {
      res.status(500).json({ success: false });
    }
  } else {
    res.status(405).json({ success: false });
  }
};

export default createDocHandler;
