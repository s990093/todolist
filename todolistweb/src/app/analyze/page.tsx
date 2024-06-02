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

Chart.register(CategoryScale);

function getData() {
  return generateFakeclassifyTask(500);
}

export default function AnalyzePage() {
  const data = getData();

  return (
    <main className="fixed inset-0 overflow-y-auto flex flex-col items-center justify-start ml-32 p-10">
      <div className="flex flex-col p-2 space-y-4">
        <AchievementChart tasks={data} />
        <TakecompletionChart tasks={data} />
      </div>
    </main>
  );
}
