"use client";
import React from "react";
import { Bar, Line } from "react-chartjs-2";
import { classifyTask, TaskType } from "../interface";
import { sortClassifyTasks } from "../helper/sort";
import filled from "@material-tailwind/react/theme/components/timeline/timelineIconColors/filled";
import { generateChartLabel, options } from "./options";

interface CurrencyChartProps {
  tasks: classifyTask[];
}

const AchievementChart: React.FC<CurrencyChartProps> = ({ tasks }) => {
  const sortedTasks = sortClassifyTasks(tasks);

  const monthlyData: { [key: string]: { [key: string]: number } } = {};
  Object.entries(sortedTasks).forEach(([subject, tasksByDay]) => {
    monthlyData[subject] = {};
    tasksByDay.forEach((tasks) => {
      tasks.forEach((task) => {
        const monthKey = `${
          task.dueDate.getMonth() + 1
        }/${task.dueDate.getFullYear()}`;
        monthlyData[subject][monthKey] =
          (monthlyData[subject][monthKey] || 0) + (task.completed ? 1 : 0);
      });
    });
  });

  // 建立 labels，這裡使用所有月份的統計數據中的鍵值
  const labels = Object.keys(monthlyData[Object.keys(monthlyData)[0]]);

  // 建立 datasets，每個科目對應一個線
  const datasets = Object.entries(monthlyData).map(([subject, data]) => {
    return generateChartLabel(subject, Object.values(data));
  });

  // 構建 chartData
  const chartData = {
    labels: labels,
    datasets: datasets,
  };

  return <Line options={options} data={chartData} />;
};

export default AchievementChart;
