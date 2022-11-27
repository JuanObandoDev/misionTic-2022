const {
  getAllCategories,
  getCategoryById,
  createCategory,
  updateCategory,
  deleteCategory,
} = require("../../components/db/db");
const { Router } = require("express");
const router = Router();

router.get("/category", async (req, res) => {
  const data = await getAllCategories();
  res.setHeader("Content-Type", "application/json");
  res.status(200).json(data);
});

router.get("/category/:id", async (req, res) => {
  const data = await getCategoryById(req.params.id);
  if (data !== null) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json(data);
  } else {
    res.status(404).json({ message: "Category not found" });
  }
});

router.post("/category/new", async (req, res) => {
  await createCategory(req.body);
  res.setHeader("Content-Type", "application/json");
  res.status(200).json({ message: "Category created" });
});

router.put("/category/:id", async (req, res) => {
  const data = await updateCategory(req.params.id, req.body);
  if (data.matchedCount === 1) {
    if (data.modifiedCount === 1) {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "Category found and updated" });
    } else {
      res.setHeader("Content-Type", "application/json");
      res.status(200).json({ message: "Category found but not updated" });
    }
  } else {
    res.status(404).json({ message: "Category not found" });
  }
});

router.delete("/category/:id", async (req, res) => {
  const data = await deleteCategory(req.params.id);
  if (data.deletedCount === 1) {
    res.setHeader("Content-Type", "application/json");
    res.status(200).json({ message: "Deleted category" });
  } else {
    res.status(404).json({ message: "Category not found" });
  }
});

module.exports = router;
