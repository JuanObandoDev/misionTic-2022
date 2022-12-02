import { getDocById } from "../../../database/db";

const getDocByIdHandler = async (req, res) => {
  if (req.method === "GET") {
    try {
      const { doc_id } = req.query;
      const doc = await getDocById(doc_id);
      res.status(200).json({ success: true, doc });
    } catch (e) {
      res.status(500).json({ success: false });
    }
  } else {
    res.status(405).json({ success: false });
  }
};

export default getDocByIdHandler;
