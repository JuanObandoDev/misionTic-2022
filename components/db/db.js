const { connect, client } = require("./conn.js");
const { ObjectId } = require("mongodb");
const db = client.db("AppWebGestionDocumental");

const getAllDocs = async () => {
  try {
    await connect();
    const docs = await db.collection("Documento").find().toArray();
    return docs;
  } catch (e) {
    throw new Error("Error getting docs");
  }
};

const getDocById = async (id) => {
  try {
    await connect();
    const doc = await db
      .collection("Documento")
      .findOne({ _id: new ObjectId(id) });
    return doc;
  } catch (error) {
    throw new Error("Error getting doc");
  }
};

const createDoc = async (doc) => {
  try {
    await connect();
    const result = await db.collection("Documento").insertOne(doc);
    return result;
  } catch (error) {
    throw new Error("Error creating doc");
  }
};

const updateDoc = async (id, doc) => {
  try {
    await connect();
    const result = await db
      .collection("Documento")
      .updateOne({ _id: new ObjectId(id) }, { $set: doc });
    return result;
  } catch (error) {
    throw new Error("Error updating doc");
  }
};

const deleteDoc = async (id) => {
  try {
    await connect();
    const result = await db
      .collection("Documento")
      .deleteOne({ _id: new ObjectId(id) });
    return result;
  } catch (error) {
    throw new Error("Error deleting doc");
  }
};

const getAllCategories = async () => {
  try {
    await connect();
    const categories = await db.collection("Categoria").find().toArray();
    return categories;
  } catch (e) {
    throw new Error("Error getting categories");
  }
};

const getCategoryById = async (id) => {
  try {
    await connect();
    const category = await db
      .collection("Categoria")
      .findOne({ _id: new ObjectId(id) });
    return category;
  } catch (error) {
    throw new Error("Error getting category");
  }
};

const createCategory = async (category) => {
  try {
    await connect();
    const result = await db.collection("Categoria").insertOne(category);
    return result;
  } catch (error) {
    throw new Error("Error creating category");
  }
};

const updateCategory = async (id, category) => {
  try {
    await connect();
    const result = await db
      .collection("Categoria")
      .updateOne({ _id: new ObjectId(id) }, { $set: category });
    return result;
  } catch (error) {
    throw new Error("Error updating category");
  }
};

const deleteCategory = async (id) => {
  try {
    await connect();
    const result = await db
      .collection("Categoria")
      .deleteOne({ _id: new ObjectId(id) });
    return result;
  } catch (error) {
    throw new Error("Error deleting category");
  }
};

const getAllInventories = async () => {
  try {
    await connect();
    const inventories = await db.collection("Inventario").find().toArray();
    return inventories;
  } catch (e) {
    throw new Error("Error getting inventories");
  }
};

const getInventoryById = async (id) => {
  try {
    await connect();
    const inventory = await db
      .collection("Inventario")
      .findOne({ _id: new ObjectId(id) });
    return inventory;
  } catch (error) {
    throw new Error("Error getting inventory");
  }
};

const createInventory = async (inventory) => {
  try {
    await connect();
    const result = await db.collection("Inventario").insertOne(inventory);
    return result;
  } catch (error) {
    throw new Error("Error creating inventory");
  }
};

const updateInventory = async (id, inventory) => {
  try {
    await connect();
    const result = await db
      .collection("Inventario")
      .updateOne({ _id: new ObjectId(id) }, { $set: inventory });
    return result;
  } catch (error) {
    throw new Error("Error updating inventory");
  }
};

const deleteInventory = async (id) => {
  try {
    await connect();
    const result = await db
      .collection("Inventario")
      .deleteOne({ _id: new ObjectId(id) });
    return result;
  } catch (error) {
    throw new Error("Error deleting inventory");
  }
};

module.exports = {
  getAllDocs,
  getDocById,
  createDoc,
  updateDoc,
  deleteDoc,
  getAllCategories,
  getCategoryById,
  createCategory,
  updateCategory,
  deleteCategory,
  getAllInventories,
  getInventoryById,
  createInventory,
  updateInventory,
  deleteInventory,
};
