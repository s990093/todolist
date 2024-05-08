export interface Evaluate {
  title: string;
  rating: number;
}
export interface Course {
  id: number;
  info: {
    course: string;
    teacher: string;
    type: string;
  };

  quality: Evaluate;
  sweetness: Evaluate; // 甜度評分
  coolness: Evaluate; // 涼度評分
  homework: Evaluate; // 作業評分

  recommendation: number; // 推薦等級，以五顆心表示
  totalStudents: number; // 統計人數
  timestamp: Date; // 可以使用 Date 類型，或者字串表示時間戳記
  comments: string;
}
