"use client";

import React from "react";
import { classifyTask } from "../interface";
import { sortClassifyTasks } from "../helper/sort";
import { Bar } from "react-chartjs-2";
import { generateChartLabel, get_lazy_options, options } from "./options";

interface AchievementChartProps {
  tasks: classifyTask[];
}

const TakecompletionChart: React.FC<AchievementChartProps> = ({ tasks }) => {
  const sortedTasks = sortClassifyTasks(tasks);

  const monthlyData: {
    [key: string]: { [key: string]: { count: number; completed: number } };
  } = {};

  Object.entries(sortedTasks).forEach(([subject, tasksByDay]) => {
    monthlyData[subject] = {};
    tasksByDay.forEach((tasks) => {
      tasks.forEach((task) => {
        const monthKey = `${
          task.dueDate.getMonth() + 1
        }/${task.dueDate.getFullYear()}`;
        monthlyData[subject][monthKey] = monthlyData[subject][monthKey] || {
          count: 0,
          completed: 0,
        };
        monthlyData[subject][monthKey].count++;
        if (task.completed) {
          monthlyData[subject][monthKey].completed++;
        }
      });
    });
  });

  // 建立所有月份的 labels
  const allMonths = new Set<string>();

  Object.values(monthlyData).forEach((subjectData) => {
    Object.keys(subjectData).forEach((month) => {
      allMonths.add(month);
    });
  });
  const labels = Array.from(allMonths).sort((a, b) => {
    const [aMonth, aYear] = a.split("/").map(Number);
    const [bMonth, bYear] = b.split("/").map(Number);
    return (
      new Date(aYear, aMonth - 1).getTime() -
      new Date(bYear, bMonth - 1).getTime()
    );
  });

  // 計算每個科目每個月的完成百分比
  const datasets = Object.entries(monthlyData).map(([subject, data]) => {
    const subjectData = labels.map((label) => {
      const monthData = data[label] || { count: 0, completed: 0 };
      return (monthData.completed / monthData.count) * 100 || 0; // 防止除以零
    });
    return generateChartLabel(subject, subjectData);
  });

  // 構建 chartData
  const chartData = {
    labels: labels,
    datasets: datasets,
  };

  return <Bar options={options} data={chartData} />;
};

export default TakecompletionChart;
