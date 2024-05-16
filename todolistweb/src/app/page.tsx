"use client";

import Image from "next/image";
import React, { useContext, useState } from "react";
import { TaskType } from "./interface";
import Task from "./components/task";
import { Context } from "./hooks/provider";
import { useRouter } from "next/navigation";
import ParticlesBg from "particles-bg";
import { generateOneTaskData, generateTaskData } from "../../test/data";

// Main Home component with a list of tasks
export default function Home() {
  const { state } = useContext(Context);
  const router = useRouter();

  const [tasks, setTasks] = useState<TaskType[]>(generateTaskData(10)); // State for managing tasks
  const [newTask, setNewTask] = useState(""); // State for the input box

  if (!state.isRegistered) {
    if (typeof window !== "undefined") {
      router.push("/register");
    }
    return null; // 或者返回一個空的組件或 loading 指示器
  }

  // Function to add a new task
  const addTask = () => {
    if (newTask.trim() !== "") {
      const newTaskObj = generateOneTaskData();
      setTasks([...tasks, newTaskObj]); // Add to the existing tasks
      setNewTask(""); // Clear the input box
    }
  };

  // Function to remove a task by its ID
  const removeTask = (taskId: number) => {
    setTasks(tasks.filter((task) => task.id !== taskId));
  };

  // Function to toggle the completed status of a task
  const toggleTaskComplete = (taskId: number) => {
    setTasks(
      tasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <main className="fixed min-h-screen flex-col items-center justify-between w-full p-20  ml-64 ">
      <h1 className="text-3xl font-bold mb-6">To-Do List</h1>

      <div className="w-full max-w-md">
        <ParticlesBg type="tadpole" bg={true} />
        <div className="flex mb-4">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="New Task..."
            className="w-full p-2 border border-gray-300 rounded-lg focus:outline-none"
          />
          <button
            onClick={addTask}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg ml-2 hover:bg-blue-600"
          >
            Add
          </button>
        </div>

        <div>
          {tasks.map((task) => (
            <Task
              key={task.id}
              task={task}
              onRemove={removeTask}
              onToggleComplete={toggleTaskComplete}
            />
          ))}
        </div>
      </div>
    </main>
  );
}
