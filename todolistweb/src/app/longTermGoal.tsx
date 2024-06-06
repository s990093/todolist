"use client";
import { LongTermGoal } from "./interface";

const longTermGoals: LongTermGoal[] = [
  {
    id: 1,
    title: "成為軟體工程師",
    description: "學習程式設計語言和相關技術，並取得相關證照。",
    targetDate: new Date(2025, 12, 31),
    progress: 50,
  },
  {
    id: 2,
    title: "創辦自己的公司",
    description: "發想一個商業點子，並將其付諸實踐。",
    targetDate: new Date(2028, 12, 31),
    progress: 20,
  },
  {
    id: 3,
    title: "環遊世界",
    description: "參觀世界各地的著名景點，體驗不同的文化。",
    targetDate: new Date(2030, 12, 31),
    progress: 10,
  },
];

const LongTermGoalsTable = () => {
  return (
    <div className="container mx-auto">
      <table className="w-full table-auto border-collapse">
        <thead>
          <tr>
            <th className="text-left px-4 py-3 border-t border-b border-gray-200">
              標題
            </th>
            <th className="text-left px-4 py-3 border-t border-b border-gray-200">
              描述
            </th>
            <th className="text-left px-4 py-3 border-t border-b border-gray-200">
              目標日期
            </th>
            <th className="text-left px-4 py-3 border-t border-b border-gray-200">
              進度
            </th>
          </tr>
        </thead>
        <tbody>
          {longTermGoals.map((goal) => (
            <tr key={goal.id}>
              <td className="text-left px-4 py-3 border-b border-gray-200">
                {goal.title}
              </td>
              <td className="text-left px-4 py-3 border-b border-gray-200">
                {goal.description}
              </td>
              <td className="text-left px-4 py-3 border-b border-gray-200">
                {goal.targetDate.toLocaleDateString()}
              </td>
              <td className="text-left px-4 py-3 border-b border-gray-200">
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className={`w-${goal.progress}% bg-blue-500 rounded-full`}
                  ></div>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LongTermGoalsTable;
