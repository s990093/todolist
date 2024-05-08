"use client";
import React, { useState } from "react";

const CourseCell = ({
  row,
  col,
  onSelect,
}: {
  row: number;
  col: number;
  onSelect: Function;
}) => {
  const [selected, setSelected] = useState(false);
  const [isMouseDown, setIsMouseDown] = useState(false);
  const handleMouseDown = () => {
    setIsMouseDown(true);
  };

  const handleMouseUp = () => {
    setIsMouseDown(false);
  };

  const handleClick = () => {
    setSelected(!selected);
    onSelect(row, col, !selected);
  };
  const handleMouseEnter = () => {
    if (isMouseDown) {
      setSelected(!selected);
      onSelect(row, col, !selected);
    }
  };
  return (
    <div
    // onClick={handleClick}
    // onMouseDown={handleMouseDown}
    // onMouseUp={handleMouseUp}
    // onMouseEnter={handleMouseEnter}
    >
      <button onClick={handleClick}>
        <div
          className={`flex justify-center m-1 items-center border bg-blue h-5 w-10 rounded-md ${
            selected
              ? "bg-[#172554] text-white"
              : "bg-[#3b82f6] text-white hover:bg-[#6d28d9]"
          }`}
          key={`${row}-${col}`}
        ></div>
      </button>
    </div>
  );
};

const DayCell = ({ day }: { day: string }) => {
  return (
    <div className="flex items-center justify-center text-black font-bold text-sm">
      {day}
    </div>
  );
};

const CurriculumCell = ({
  handleCellSelect,
}: {
  handleCellSelect: Function;
}) => {
  const courses = 50;
  //   const weekly = 5;
  const weekly = ["", "Mon", "Tue", "Wed", "Thu", "Fri"];

  return (
    <div className="grid grid-cols-6">
      {weekly.map((day, index) => (
        <DayCell key={index} day={day} />
      ))}

      {Array.from({ length: courses }).map((_, index) => {
        const row = Math.floor(index / 5);
        const col = index % 5;

        if (col === 0) {
          return (
            <React.Fragment key={index}>
              <span className="text-black font-bold text-sm">
                第{row + 1}節
              </span>
              <CourseCell
                key={index}
                row={row}
                col={col}
                onSelect={handleCellSelect}
              />
            </React.Fragment>
          );
        } else {
          return (
            <CourseCell
              key={index}
              row={row}
              col={col}
              onSelect={handleCellSelect}
            />
          );
        }
      })}
    </div>
  );
};

export default CurriculumCell;
