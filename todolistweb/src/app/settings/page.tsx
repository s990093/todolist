"use client";
import React, { useEffect, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCog } from "@fortawesome/free-solid-svg-icons";

// 假資料
const userData = {
  name: "賴泓瑋",
  email: "lai09150915@gmail.com",
  role: "管理員",
  publicData: true,
  darkMode: false,
};

const courseCategories = ["資訊工程", "英文", "數學", "化學", "物理"];
function SettingsPage() {
  const [loading, setLoading] = useState(false);

  // 模擬載入完成後隱藏載入動畫
  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 10); // 模擬載入時間 1 秒
  }, []);

  return (
    <div
      className={`p-8 bg-gray-100 min-h-screen ${loading ? "opacity-50" : ""}`}
    >
      {/* 載入動畫 */}
      {loading && (
        <div className="fixed top-0 left-0 w-full h-full bg-white opacity-75 flex items-center justify-center z-50">
          <div className="loader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-24 w-24"></div>
        </div>
      )}

      <h1
        className={`text-2xl font-bold mb-4 flex items-center ${
          loading ? "hidden" : ""
        }`}
      >
        <FontAwesomeIcon icon={faCog} className="mr-2" /> 設定
      </h1>

      {/* 使用者資料 */}
      <div
        className={`mb-8 bg-white rounded shadow-md p-4 ${
          loading ? "hidden" : ""
        }`}
      >
        <h2 className="text-xl font-semibold mb-2">使用者資料</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-gray-600">姓名: {userData.name}</p>
            <p className="text-gray-600">Email: {userData.email}</p>
            <p className="text-gray-600">角色: {userData.role}</p>
          </div>
          {/* 右側的公開資料和黑暗模式設定 */}
          <div>
            <p className="text-gray-600">
              公開資料: {userData.publicData ? "是" : "否"}
            </p>
            <p className="text-gray-600">
              黑暗模式: {userData.darkMode ? "開啟" : "關閉"}
            </p>
          </div>
        </div>
      </div>

      {/* 課程分類 */}
      <div
        className={`mb-8 bg-white rounded shadow-md p-4 ${
          loading ? "hidden" : ""
        }`}
      >
        <h2 className="text-xl font-semibold mb-2">課程分類</h2>
        <ul>
          {courseCategories.map((category, index) => (
            <li key={index} className="text-gray-600">
              {category}
            </li>
          ))}
        </ul>
      </div>

      {/* 頁面設定 */}
      <div
        className={`bg-white rounded shadow-md p-4 ${loading ? "hidden" : ""}`}
      >
        <h2 className="text-xl font-semibold mb-2">頁面設定</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-gray-600">公開資料</p>
            <label className="switch">
              <input
                type="checkbox"
                checked={userData.publicData}
                onChange={() => {}}
                className="toggle-checkbox"
              />
              <span className="toggle-slider"></span>
            </label>
          </div>
          <div>
            <p className="text-gray-600">黑暗模式</p>
            <label className="switch">
              <input
                type="checkbox"
                checked={userData.darkMode}
                onChange={() => {}}
                className="toggle-checkbox"
              />
              <span className="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SettingsPage;
