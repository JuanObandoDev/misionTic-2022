const {
  getAllInventories,
  getInventoryById,
  createInventory,
  updateInventory,
  deleteInventory,
} = require("../../components/db/db");
const { Router } = require("express");
const router = Router();

router.get("/inventory", async (req, res) => {
  const data = await getAllInventories();
  res.setHeader("Content-Type", "application/json");
  res.status(200).json(data);
});

router.get("/inventory/:id", async (req, res) => {
  const data = await getInventoryById(req.params.id);
  if (data !== null) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json(data);
  } else {
    res.status(404).json({ message: "Inventory not found" });
  }
});

router.post("/inventory/new", async (req, res) => {
  await createInventory(req.body);
  res.setHeader("Content-Type", "application/json");
  res.status(200).json({ message: "Inventory created" });
});

router.put("/inventory/:id", async (req, res) => {
  const data = await updateInventory(req.params.id, req.body);
  if (data.matchedCount === 1) {
    if (data.modifiedCount === 1) {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "Inventory found and updated" });
    } else {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "Inventory found but not updated" });
    }
  } else {
    res.status(404).json({ message: "Inventory not found" });
  }
});

router.delete("/inventory/:id", async (req, res) => {
  const data = await deleteInventory(req.params.id);
  if (data.deletedCount === 1) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json({ message: "Deleted inventory" });
  } else {
    res.status(404).json({ message: "Inventory not found" });
  }
});

module.exports = router;
