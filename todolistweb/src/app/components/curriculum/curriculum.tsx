"use client";
import React, { useState } from "react";
// component
import { Button } from "../button";
import BaseCard from "../card/base_card";
import CurriculumCell from "./curriculum_cell";
import CourseSelection from "./course_select";

const Curriculum = () => {
  const [selectedCells, setSelectedCells] = useState<{
    [key: string]: boolean;
  }>({});
  const [selectedOption, setSelectedOption] = useState<string | null>(null); // 追踪当前选择的选项

  const handleQureyCurriculum = () => {
    console.log(selectedCells);
  };

  const handleCellSelect = (row: number, col: number, isSelected: boolean) => {
    setSelectedCells((prevState) => {
      const updatedState = { ...prevState };
      if (isSelected) {
        updatedState[`${row}-${col}`] = true;
        delete updatedState[`${row}-${col}`];
      }

      return updatedState;
    });
  };

  const handleOptionSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(event.target.value);
  };

  return (
    <BaseCard className="items-center justify-center bg-secondary bg-opacity-60">
      <div className="flex flex-col space-x-4">
        {/* title */}
        <h1 className="flex justify-center text-xl font-bold m-3">選擇課表</h1>

        {/* body */}
        <div className="flex flex-col sm:flex-row space-x-4">
          {/* left */}
          <div className="max-w-lg mx-auto">
            <CurriculumCell handleCellSelect={handleCellSelect} />
          </div>
          {/* right */}
          <CourseSelection />
        </div>
      </div>
    </BaseCard>
  );
};

export default Curriculum;
