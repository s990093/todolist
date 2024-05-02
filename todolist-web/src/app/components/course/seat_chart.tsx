"use client";
import React, { useState } from "react";

interface SeatChartProps {} // Define props interface for future flexibility

const SeatChart = () => {
  return (
    <div className="container mx-auto">
      <table className="table table-fixed">
        <thead>
          <tr>
            <th className="bg-blue-500 text-white px-4">Time</th>
            <th className="bg-blue-500 text-white px-4">Monday</th>
            <th className="bg-blue-500 text-white px-4">Tuesday</th>
            <th className="bg-blue-500 text-white px-4">Wednesday</th>
            <th className="bg-blue-500 text-white px-4">Thursday</th>
            <th className="bg-blue-500 text-white px-4">Friday</th>
          </tr>
        </thead>
        <tbody>
          {/* Rows for each time slot */}
          <tr>
            <td className="text-gray-800 px-4">08:00 - 09:00</td>
            <td className="px-4">Math</td>
            <td className="px-4">History</td>
            <td className="px-4">English</td>
            <td className="px-4">Science</td>
            <td className="px-4"></td>
          </tr>
          {/* More rows... */}
        </tbody>
      </table>
    </div>
  );
};

export default SeatChart;
