"use client";

import React, { useState } from "react";
import { TaskProps } from "../interface";

// Task component for displaying individual tasks
const Task: React.FC<TaskProps> = ({ task, onRemove, onToggleComplete }) => {
  return (
    <div className="flex justify-between items-center p-2 mb-2 bg-gray-100 rounded-lg shadow-sm">
      <div className="flex items-center">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggleComplete(task.id)}
          className="mr-2"
        />
        <span className={task.completed ? "line-through" : ""}>
          {task.text}
        </span>
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

export default Task;
