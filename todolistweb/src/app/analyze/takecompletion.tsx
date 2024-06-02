"use client";
import React from "react";
import { classifyTask } from "../interface";

interface AchievementChartProps {
  tasks: classifyTask[];
}

const TakecompletionChart: React.FC<AchievementChartProps> = ({ tasks }) => {
  return (
    <div>
      {tasks.map((task, index) => (
        <div key={index}>
          <p>Category: {task.category}</p>
          <p>Description: {task.description}</p>
          <p>Due Date: {task.dueDate.toDateString()}</p>
          <p>Completed: {task.completed ? "Yes" : "No"}</p>
        </div>
      ))}
    </div>
  );
};

export default TakecompletionChart;
