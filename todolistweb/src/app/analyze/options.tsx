"use client";

export function get_lazy_options(subject: string) {
  return {
    responsive: true,
    interaction: {
      mode: "index" as const,
      intersect: false,
    },
    stacked: false,
    plugins: {
      title: {
        display: true,
        text: subject,
      },
    },
    scales: {
      y: {
        type: "linear" as const,
        display: true,
        position: "left" as const,
      },
      y1: {
        type: "linear" as const,
        display: true,
        position: "right" as const,
        grid: {
          drawOnChartArea: false,
        },
      },
    },
  };
}
export const options = {
  responsive: true,
  interaction: {
    mode: "index" as const,
    intersect: false,
  },
  stacked: false,
  plugins: {
    title: {
      display: true,
      text: "AchievementChart",
    },
  },
  scales: {
    y: {
      type: "linear" as const,
      display: true,
      position: "left" as const,
    },
    y1: {
      type: "linear" as const,
      display: true,
      position: "right" as const,
      grid: {
        drawOnChartArea: false,
      },
    },
  },
};

const generateRandomColor = (opy: number, init: number = 100) => {
  const randomColor = () => Math.floor(Math.random() * 155) + init;
  return `rgba(${randomColor()},${randomColor()},${randomColor()},${opy})`;
};

export const generateChartLabel = (subject: string, data: Object) => {
  // TODO: DO not change !
  return {
    label: subject,
    data: data,
    backgroundColor: generateRandomColor(0.8),
    fill: true,
    tension: 0.3,
  };
};
