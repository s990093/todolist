"use client";
import React from "react";
import { Line, Bar, Pie } from "react-chartjs-2";
import { ChartOptions } from "chart.js/auto";
import { CategoryScale } from "chart.js";
import Chart from "chart.js/auto";
import { autocompleteClasses } from "@mui/material";

Chart.register(CategoryScale);

export default function AnalyzePage() {
  // 成就圖表資料
  const achievementData = {
    labels: ["週一", "週二", "週三", "週四", "週五"],
    datasets: [
      {
        label: "成就",
        data: [5, 7, 3, 9, 6],
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 1,
      },
    ],
  };

  // 里程碑圖表資料
  const milestoneData = {
    labels: ["1月", "2月", "3月", "4月", "5月", "6月"],
    datasets: [
      {
        label: "里程碑",
        data: [10, 20, 15, 25, 30, 28],
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  };

  // 進度追蹤圖表資料
  const progressData = {
    labels: ["週一", "週二", "週三", "週四", "週五"],
    datasets: [
      {
        label: "進度",
        data: [20, 30, 25, 35, 40],
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
    ],
  };

  // 負載平衡圖表資料
  const workloadData = {
    labels: ["週一", "週二", "週三", "週四", "週五"],
    datasets: [
      {
        label: "負載",
        data: [8, 7, 6, 5, 9],
        backgroundColor: "rgba(153, 102, 255, 0.2)",
        borderColor: "rgba(153, 102, 255, 1)",
        borderWidth: 1,
      },
    ],
  };

  return (
    <main className="fixed inset-0 overflow-y-auto flex flex-col items-center justify-start p-20 ml-64">
      <div className="mb-8">
        <h2 className="mb-4">成就圖表</h2>
        <Line data={achievementData} />
      </div>
      <div className="mb-8">
        <h2 className="mb-4">里程碑圖表</h2>
        <Bar data={milestoneData} />
      </div>
      <div className="mb-8">
        <h2 className="mb-4">進度追蹤圖表</h2>
        <Line data={progressData} />
      </div>
      <div className="mb-8">
        <h2 className="mb-4">負載平衡圖表</h2>
        <Bar data={workloadData} />
      </div>
    </main>
  );
}
