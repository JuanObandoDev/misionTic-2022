import { getAllDocs } from "../../../database/db";

const getAllDocsHandler = async (req, res) => {
  const docs = await getAllDocs();
  res.setHeader("Content-Type", "application/json");
  res.status(200).json(docs);
};

export default getAllDocsHandler;
