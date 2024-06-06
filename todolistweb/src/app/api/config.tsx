import axios, { AxiosError, AxiosResponse } from "axios";
import { TaskStatus } from "../interface/api";
import { TaskType } from "../interface";

const BASE_URL = "http://localhost:8000/api/app/";
// 通用的 Axios 請求函數
async function sendRequest<T>(
  method: "GET" | "POST",
  url: string,
  data?: any
): Promise<T> {
  try {
    const response: AxiosResponse<T> = await axios({
      method,
      url,
      data,
    });
    return response.data;
  } catch (error: unknown) {
    const axiosError = error as AxiosError;
    throw new Error(`Request failed: ${axiosError.message}`);
  }
}

// 定義一個函數來發送 GET 請求，並返回結果
export async function getTaskStatus(): Promise<TaskStatus> {
  return await sendRequest<TaskStatus>("GET", `${BASE_URL}task-status/`);
}

// 定義一個函數來發送 POST 請求，並返回結果
export async function createTask(taskData: TaskType): Promise<TaskType> {
  return await sendRequest<TaskType>("POST", `${BASE_URL}tasks/`, taskData);
}

export async function getTasks(): Promise<TaskType[]> {
  return await sendRequest<TaskType[]>("GET", `${BASE_URL}tasks/`);
}
