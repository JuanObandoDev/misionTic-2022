import { updateDoc } from "../../../../database/db";

const updateDocHandler = async (req, res) => {
  if (req.method === "PUT") {
    try {
      const { doc_id } = req.query;
      const { doc } = req.body;
      await updateDoc(doc_id, doc);
      res.status(200).json({ success: true });
    } catch (e) {
      res.status(500).json({ success: false });
    }
  } else {
    res.status(405).json({ success: false });
  }
};

export default updateDocHandler;
