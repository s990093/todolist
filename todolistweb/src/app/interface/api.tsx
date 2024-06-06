import { TaskType } from "./task";

// 定義回傳的物件結構
export interface TaskStatus {
  tasks_registered: boolean;
  tasks_empty: boolean;
  tasks: TaskType[];
}
