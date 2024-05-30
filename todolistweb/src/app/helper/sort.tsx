import { TaskType } from "../interface";

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
    .sort((a, b) => new Date(a.time).getTime() - new Date(b.time).getTime());
}

export function AddTask(
  newTask: string,
  priority: "low" | "medium" | "high"
): TaskType {
  const currentTime = new Date().toISOString(); // 使用 Date 函數獲取當前時間並轉換為 ISO 格式

  return {
    id: Date.now(), // 使用当前时间戳作为唯一ID
    text: newTask,
    completed: false,
    time: currentTime, // 使用當前時間
    desc: "", // 你可以根據需要給這些屬性指定值
    priority: priority, // 你可以根據需要給這些屬性指定值
    deadline: "", // 你可以根據需要給這些屬性指定值
    type: "someType", // 你可以根據需要給這些屬性指定值
    tags: [], // 你可以根據需要給這些屬性指定值
  };
}
