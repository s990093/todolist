import { classifyTask, TaskType } from "../interface";

// 排序任务时间的函数
export function sortOriginalTasks(tasks: TaskType[]): TaskType[] {
  // 将任务列表按照 completed 属性分成两组
  const completedTasks = tasks.filter((task) => task.completed);
  const uncompletedTasks = tasks.filter((task) => !task.completed);

  // 将排序后的两组任务合并成一个任务列表
  const sortedTasks = [
    ...sortTasksByTime(uncompletedTasks),
    ...sortTasksByTime(completedTasks),
  ];

  return sortedTasks;
}

export function sortTasksByTime(tasks: TaskType[]): TaskType[] {
  return tasks
    .slice()
    .sort((a, b) => new Date(b.time).getTime() - new Date(a.time).getTime());
}

export function AddTask(
  newTask: string,
  priority: "low" | "medium" | "high"
): TaskType {
  const currentTime = new Date().toISOString(); // 使用 Date 函數獲取當前時間並轉換為 ISO 格式

  return {
    id: Date.now(),
    text: newTask,
    completed: false,
    time: currentTime, // 使用當前時間
    priority: priority, // 你可以根據需要給這些屬性指定值
    type: "someType", // 你可以根據需要給這些屬性指定值
  };
}
export function sortClassifyTasks(tasks: classifyTask[]): {
  [key: string]: classifyTask[][];
} {
  // 將 tasks 按照 category 分組
  const tasksByCategory: { [key: string]: classifyTask[] } = {};
  tasks.forEach((task) => {
    if (!tasksByCategory[task.category]) {
      tasksByCategory[task.category] = [];
    }
    tasksByCategory[task.category].push(task);
  });

  // 將每個科目的任務按照日期分組
  const tasksByCategoryAndDate: { [key: string]: classifyTask[][] } = {};
  Object.entries(tasksByCategory).forEach(([category, tasks]) => {
    const tasksByDate: { [key: string]: classifyTask[] } = {};
    tasks.forEach((task) => {
      const dateKey = task.dueDate.toLocaleDateString();
      if (!tasksByDate[dateKey]) {
        tasksByDate[dateKey] = [];
      }
      tasksByDate[dateKey].push(task);
    });
    tasksByCategoryAndDate[category] = Object.values(tasksByDate);
  });

  return tasksByCategoryAndDate;
}
