"use client";
import React from "react";
import { Line, Bar, Pie } from "react-chartjs-2";
import { ChartOptions } from "chart.js/auto";
import { CategoryScale } from "chart.js";
import Chart from "chart.js/auto";
import { autocompleteClasses } from "@mui/material";
import CurrencyChart from "./achievement_chart";
import { generateFakeclassifyTask, generateTaskData } from "../../../test/data";
import AchievementChart from "./achievement_chart";
import TakecompletionChart from "./takecompletion";
import MilestoneChart from "./milestoneChart";
import GoalTracker from "./goalTracker";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartBar } from "@fortawesome/free-solid-svg-icons";

Chart.register(CategoryScale);

function getData() {
  return generateFakeclassifyTask(1000);
}

export default function AnalyzePage() {
  const data = getData();

  return (
    <main className="fixed inset-0 overflow-y-auto flex flex-col items-center justify-start ml-32 p-4">
      <div className="p-4 text-2xl font-bold text-gray-800">
        <FontAwesomeIcon icon={faChartBar} /> Analyze
      </div>
      <div className="w-full max-w-4xl p-4 bg-white shadow-md rounded-lg mb-6">
        <AchievementChart tasks={data} />
      </div>
      <div className="w-full max-w-4xl p-4 bg-white shadow-md rounded-lg mb-6">
        <MilestoneChart tasks={data} />
      </div>

      <div className="w-full  max-w-4xl p-4 bg-white shadow-md rounded-lg">
        <TakecompletionChart tasks={data} />
      </div>
      <div className="w-full max-w-4xl p-4 bg-white shadow-md rounded-lg m-5">
        <GoalTracker
          totalTasks={data.length}
          completedTasks={data.filter((item) => item.completed).length}
        />
      </div>
    </main>
  );
}
