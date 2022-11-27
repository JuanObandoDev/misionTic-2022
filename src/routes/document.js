const {
  getAllDocs,
  getDocById,
  createDoc,
  updateDoc,
  deleteDoc,
} = require("../../components/db/db");
const { Router } = require("express");
const router = Router();

router.get("/document", async (req, res) => {
  const data = await getAllDocs();
  res.setHeader("Content-Type", "application/json");
  res.status(200).json(data);
});

router.get("/document/:id", async (req, res) => {
  const data = await getDocById(req.params.id);
  if (data !== null) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json(data);
  } else {
    res.status(404).json({ message: "Document not found" });
  }
});

router.post("/document/new", async (req, res) => {
  await createDoc(req.body);
  res.setHeader("Content-Type", "application/json");
  res.status(200).json({ message: "Document created" });
});

router.put("/document/:id", async (req, res) => {
  const data = await updateDoc(req.params.id, req.body);
  if (data.matchedCount === 1) {
    if (data.modifiedCount === 1) {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "document found and updated" });
    } else {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "document found but not updated" });
    }
  } else {
    res.status(404).json({ message: "Document not found" });
  }
});

router.delete("/document/:id", async (req, res) => {
  const data = await deleteDoc(req.params.id);
  if (data.deletedCount === 1) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json({ message: "Deleted document" });
  } else {
    res.status(404).json({ message: "Document not found" });
  }
});

module.exports = router;
