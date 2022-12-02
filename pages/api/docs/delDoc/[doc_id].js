import { deleteDoc } from "../../../../database/db";

const deleteDocHandler = async (req, res) => {
  if (req.method === "DELETE") {
    try {
      const { doc_id } = req.query;
      await deleteDoc(doc_id);
      res.status(200).json({ success: true });
    } catch (e) {
      res.status(500).json({ success: false });
    }
  } else {
    res.status(405).json({ success: false });
  }
};

export default deleteDocHandler;
