import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChartPie,
  faCheckCircle,
  faFlag,
  faTrophy,
} from "@fortawesome/free-solid-svg-icons";

// 假資料
const friendsData = [
  {
    name: "Amy",
    description: "Amy 是一位熱愛挑戰的玩家，專注於技能發展和遊戲內的成就。",
    goals: 5,
    tasksCompleted: 32,
    milestonesCompleted: 7,
    achievements: 3,
  },
  {
    name: "Bob",
    description: "Bob 是一位樂於助人的社區成員，致力於完成多項任務和專案。",
    goals: 8,
    tasksCompleted: 45,
    milestonesCompleted: 12,
    achievements: 5,
  },
  {
    name: "Charlie",
    description:
      "Charlie 是一位創意無限的設計師，專注於創建獨特和有意義的作品。",
    goals: 3,
    tasksCompleted: 18,
    milestonesCompleted: 4,
    achievements: 1,
  },
  {
    name: "David",
    description:
      "David 是一位喜愛運動和健康生活的教練，鼓勵身心健康的積極生活。",
    goals: 6,
    tasksCompleted: 28,
    milestonesCompleted: 5,
    achievements: 2,
  },
  {
    name: "Emily",
    description:
      "Emily 是一位熱愛旅行和探險的自由靈魂，追求多元文化的交流和體驗。",
    goals: 4,
    tasksCompleted: 22,
    milestonesCompleted: 6,
    achievements: 4,
  },
];

const FriendTasksPage = () => {
  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-8">朋友任務情況</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {friendsData.map((friend, index) => (
          <div key={index} className="bg-white rounded shadow-md p-4">
            <h2 className="text-lg font-semibold mb-2">{friend.name}</h2>
            <p className="text-sm text-gray-600 mb-4">{friend.description}</p>
            <div className="grid grid-cols-2 gap-4">
              <div className="flex items-center">
                <FontAwesomeIcon
                  icon={faChartPie}
                  className="text-blue-500 mr-2"
                />
                <p className="text-gray-600">Goals: {friend.goals}</p>
              </div>
              <div className="flex items-center">
                <FontAwesomeIcon
                  icon={faCheckCircle}
                  className="text-green-500 mr-2"
                />
                <p className="text-gray-600">
                  Tasks Completed: {friend.tasksCompleted}
                </p>
              </div>
              <div className="flex items-center">
                <FontAwesomeIcon
                  icon={faFlag}
                  className="text-yellow-500 mr-2"
                />
                <p className="text-gray-600">
                  Milestones Completed: {friend.milestonesCompleted}
                </p>
              </div>
              <div className="flex items-center">
                <FontAwesomeIcon
                  icon={faTrophy}
                  className="text-purple-500 mr-2"
                />
                <p className="text-gray-600">
                  Achievements: {friend.achievements}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FriendTasksPage;
