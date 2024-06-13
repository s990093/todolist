"use client";
import React, { useState } from "react";

const MemoPage = () => {
  const [memos, setMemos] = useState([
    "倒垃圾",
    "暑假考駕照",
    "換摩托車",
    "暑假出國比賽",
  ]);
  const [newMemo, setNewMemo] = useState("");

  const handleAddMemo = () => {
    if (newMemo.trim() !== "") {
      setMemos([...memos, newMemo]);
      setNewMemo("");
    }
  };

  const handleDeleteMemo = (index: number) => {
    const updatedMemos = [...memos];
    updatedMemos.splice(index, 1);
    setMemos(updatedMemos);
  };

  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-8">備忘錄</h1>

      <div className="mb-4">
        <input
          type="text"
          className="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-blue-500"
          placeholder="新增備忘錄"
          value={newMemo}
          onChange={(e) => setNewMemo(e.target.value)}
        />
        <button
          className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
          onClick={handleAddMemo}
        >
          新增
        </button>
      </div>

      <div>
        {memos.map((memo, index) => (
          <div
            key={index}
            className="bg-white rounded-md shadow-md p-4 mb-4 flex justify-between items-center"
          >
            <p className="text-gray-800">{memo}</p>
            <button
              className="text-red-500 hover:text-red-700 focus:outline-none"
              onClick={() => handleDeleteMemo(index)}
            >
              刪除
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MemoPage;
