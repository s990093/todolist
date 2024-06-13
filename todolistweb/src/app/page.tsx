"use client";

import Image from "next/image";
import React, { useContext, useEffect, useState } from "react";
import { TaskType } from "./interface";
import Task from "./components/task";
import { Context } from "./hooks/provider";
import { useRouter } from "next/navigation";

import { AddTask, sortOriginalTasks, sortTasksByTime } from "./helper/sort";
import TodoForm from "./todoForm";
import LongTermGoalsTable from "./longTermGoal";
import { createTask, getTasks } from "./api/config";
import { GetServerSideProps } from "next";

// 每一次請求都會拿到資料

// Main Home component with a list of tasks
// eslint-disable-next-line @next/next/no-async-client-component
export default function Home() {
  const { state } = useContext(Context);
  const router = useRouter();
  const [tasks, setTasks] = useState<TaskType[]>(
    sortOriginalTasks(state.taskStatus.tasks)
  );

  if (!state.isRegistered) {
    if (typeof window !== "undefined") {
      router.push("/register");
    }
    return null; // 或者返回一個空的組件或 loading 指示器
  }

  // Function to add a new task
  const addTask = (text: string, priority: "low" | "medium" | "high") => {
    if (text.trim() !== "") {
      const newTaskObj = AddTask(text, priority);
      createTask(newTaskObj);

      // setTasks([...tasks, newTaskObj]); // Add to the existing tasks
      const updatedTasks = sortTasksByTime([...tasks, newTaskObj]);
      // Sets
      setTasks(updatedTasks);
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
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      {/* title */}
      <h1 className="text-3xl font-bold mb-6">To-Do List</h1>
      <div className="w-full max-w-md">
        {/* BG */}
        {/* form */}
        <div className="flex mb-4">
          <TodoForm onAddTask={addTask} />
        </div>
        {/* body */}
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
      {/* <div>
        <LongTermGoalsTable />
      </div> */}
    </main>
  );
}
