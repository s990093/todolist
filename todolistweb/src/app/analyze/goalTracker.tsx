import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTasks } from "@fortawesome/free-solid-svg-icons";

interface ProgressBarProps {
  completed: boolean;
  total: number;
}

const ProgressBar: React.FC<ProgressBarProps> = ({ completed, total }) => {
  const progressClass = completed
    ? "bg-blue-600 dark:bg-blue-500"
    : "bg-gray-300 dark:bg-neutral-600";
  const ariaValueNow = completed ? 20 : 0;

  return (
    <div
      className={`w-full h-2.5 flex flex-col justify-center overflow-hidden ${progressClass} text-xs text-white text-center whitespace-nowrap transition duration-500`}
      role="progressbar"
      aria-valuenow={ariaValueNow}
      aria-valuemin={0}
      aria-valuemax={100}
    />
  );
};

interface GoalTrackerProps {
  totalTasks: number;
  completedTasks: number;
}

const GoalTracker: React.FC<GoalTrackerProps> = ({
  totalTasks,
  completedTasks,
}) => {
  const maxTasks = Math.ceil(totalTasks / 10) * 10; // Ensure divisibility by 10
  const progress = Math.floor((completedTasks / maxTasks) * 100); // Calculate progress percentage

  const completedBarCount = Math.floor(progress / 10); // Each bar represents 20%

  console.log(completedBarCount);
  const remainingBarCount = maxTasks / 10 - completedBarCount;

  // Inside GoalTracker component
  return (
    <div className="p-4">
      <h2 className="text-lg font-semibold mb-2">
        <FontAwesomeIcon icon={faTasks} className="mr-2" /> Goal Progress
      </h2>
      <div className="flex items-center gap-x-1">
        {Array.from({ length: maxTasks / 10 }, (_, i) => (
          <ProgressBar key={i} completed={i < completedBarCount} total={20} />
        ))}
        <div className="w-10 text-end">
          <span className="text-sm text-gray-800 dark:text-white">
            {progress}%
          </span>
        </div>
      </div>
      <span className="text-xs text-gray-500 dark:text-gray-400">
        Tasks Completed
      </span>
    </div>
  );
};

export default GoalTracker;
