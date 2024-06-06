"use client";

import React from "react";
import { classifyTask } from "../interface";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faTasks,
  faChartLine,
  faBook,
  faTasksAlt,
  IconDefinition,
} from "@fortawesome/free-solid-svg-icons";

// MilestoneCard 組件
const MilestoneCard: React.FC<{
  title: string;
  count: number | string;
  icon: IconDefinition;
}> = ({ title, count, icon }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-4">
      <h2 className="text-xl font-semibold mb-2">
        <FontAwesomeIcon icon={icon} /> {title}
      </h2>
      <p className="text-gray-700">{count.toString()}</p>
    </div>
  );
};

interface MilestoneChartProps {
  tasks: classifyTask[];
}

const MilestoneChart: React.FC<MilestoneChartProps> = ({ tasks }) => {
  const completedTasks = tasks.filter((task) => task.completed);

  const completedCount = completedTasks.length;

  // 計算已經持續多久
  const firstTaskDate =
    tasks.length > 0 ? new Date(tasks[0].dueDate) : new Date();
  const lastTaskDate =
    tasks.length > 0 ? new Date(tasks[tasks.length - 1].dueDate) : new Date();
  const daysDifference = Math.ceil(
    (lastTaskDate.getTime() - firstTaskDate.getTime()) / (1000 * 60 * 60 * 24)
  );

  // 計算平均每天的任務數量
  const averageTasksPerDay = tasks.length / daysDifference;

  // 計算最多次任務數量
  const maxTasksPerDay = tasks.reduce((acc, task) => {
    const dateKey = task.dueDate.toDateString();
    acc[dateKey] = (acc[dateKey] || 0) + 1;
    return acc;
  }, {} as { [key: string]: number });
  const maxTasks = Math.max(...Object.values(maxTasksPerDay));

  // 計算最常使用的科目
  const subjectFrequency = tasks.reduce((acc, task) => {
    const subject = task.category;
    acc[subject] = (acc[subject] || 0) + 1;
    return acc;
  }, {} as { [key: string]: number });
  const mostUsedSubject = Object.keys(subjectFrequency).reduce((a, b) =>
    subjectFrequency[a] > subjectFrequency[b] ? a : b
  );

  return (
    <div className="max-w-md mx-auto flex flex-col items-center justify-start">
      <div className="p-4 text-2xl font-bold text-gray-800">
        <FontAwesomeIcon icon={faChartLine} /> Analyze
      </div>

      <div className="flex flex-wrap justify-center">
        <div className="mb-5 grid gap-4 grid-cols-2">
          <MilestoneCard
            title="Completed Tasks"
            count={completedCount}
            icon={faTasksAlt}
          />
          <MilestoneCard
            title="Average Tasks per Day"
            count={Number(averageTasksPerDay.toFixed(2))}
            icon={faTasks}
          />
          <MilestoneCard
            title="Max Tasks in a Day"
            count={maxTasks}
            icon={faTasks}
          />
          <MilestoneCard
            title="Most Used Subject"
            icon={faBook}
            count={mostUsedSubject}
          />
        </div>
      </div>
    </div>
  );
};
export default MilestoneChart;
