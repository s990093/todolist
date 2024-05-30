"use client";

import React, { useState } from "react";
import { TaskProps } from "../interface";

// Task component for displaying individual tasks
const TaskItem: React.FC<TaskProps> = ({
  task,
  onRemove,
  onToggleComplete,
}) => {
  const [clickCount, setClickCount] = useState(0);

  const handleClick = () => {
    onToggleComplete(task.id);
  };
  return (
    <div
      className={`flex justify-between items-center p-2 mb-2 bg-gray-100 rounded-lg shadow-sm ${
        task.completed ? "line-through" : ""
      }`}
    >
      <div className="flex items-center">
        <input
          type="radio"
          checked={task.completed}
          onChange={handleClick}
          className="mr-2"
        />
        <span>{task.text}</span>
      </div>
      <button
        onClick={() => onRemove(task.id)}
        className="text-red-500 hover:text-red-700"
      >
        Remove
      </button>
    </div>
  );
};

export default TaskItem;
