"use client";
import ParticlesBg from "particles-bg";
import React, { useState, useContext } from "react";
import { Context } from "../hooks/provider";
import { toHaveStyle } from "@testing-library/jest-dom/matchers";
import { useRouter } from "next/navigation";

function Register() {
  const router = useRouter();

  const { state, setIsRegistered } = useContext(Context);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  if (state.isRegistered) {
    router.push("/");
  }

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault();
    // 將填寫的設定資訊保存到檔案或發送到後端

    // 清空表單
    setUsername("");
    setEmail("");
    setPassword("");
    setIsRegistered(true);
  };
  return (
    <div>
      <ParticlesBg num={150} type="circle" bg={true} />
      {/* Form */}
      <div className="container mx-auto flex justify-center items-center h-screen">
        <div className="bg-white bg-opacity-50 p-10 rounded-lg backdrop-filter backdrop-blur-lg">
          <h2 className="text-2xl font-bold mb-4">Setting</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label htmlFor="username" className="block">
                Username:
              </label>
              <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="border border-gray-300 rounded px-3 py-2 w-full"
              />
            </div>
            <div>
              <label htmlFor="email" className="block">
                Email:
              </label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="border border-gray-300 rounded px-3 py-2 w-full"
              />
            </div>
            <div>
              <label htmlFor="password" className="block">
                Password:
              </label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="border border-gray-300 rounded px-3 py-2 w-full"
              />
            </div>
            <button
              type="submit"
              className="bg-blue-500 text-white rounded px-4 py-2 hover:bg-blue-600"
            >
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;
