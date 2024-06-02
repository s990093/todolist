"use client";
import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronDown } from "@fortawesome/free-solid-svg-icons";

interface TodoFormProps {
  onAddTask: (text: string, priority: "low" | "medium" | "high") => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ onAddTask }) => {
  const [newTask, setNewTask] = useState("");
  const [priority, setPriority] = useState<
    "low" | "medium" | "high" | "normal"
  >("normal");
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const addTask = () => {
    if (newTask.trim() === "") return;
    const actualPriority = priority === "normal" ? "low" : priority;

    onAddTask(newTask, actualPriority);
    setNewTask("");
    setIsDropdownOpen(false);
    setPriority("normal");
  };

  // const closeSelection = () => {
  //   setIsDropdownOpen()
  // };

  return (
    <div className="w-full max-w-md">
      <div className="flex mb-4 m-3">
        <div className="flex w-full relative">
          {isDropdownOpen && (
            <select
              className="absolute right-0 mt-2 w-32 rounded-lg border border-gray-300 bg-white shadow-md appearance-none focus:outline-none"
              value={priority}
              onChange={(e) => {
                setPriority(
                  e.target.value as "low" | "medium" | "high" | "normal"
                );
                setIsDropdownOpen(false);
              }}
            >
              <option value="normal">Normal</option>
              <option value="high">High</option>
              <option value="urgent">Urgent</option>
            </select>
          )}
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="New Task..."
            className="w-full p-2 border border-gray-300 rounded-lg focus:outline-none"
          />
        </div>
        <button
          className="bg-blue-500 text-white px-2 py-2 rounded-lg hover:bg-blue-600 ml-2 flex items-center"
          onClick={addTask}
        >
          Add
          <div className="ml-1 flex items-center ml-[8px]">
            <FontAwesomeIcon
              icon={faChevronDown}
              className="text-gray-400 cursor-pointer"
              onClick={() => setIsDropdownOpen(!isDropdownOpen)}
            />
          </div>
        </button>
      </div>
    </div>
  );
};

export default TodoForm;
