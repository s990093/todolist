import { classifyTask, TaskType } from "@/app/interface";
import { faker } from "@faker-js/faker/locale/es";

// 生成虛擬任務資料的函式
export const generateTaskData = (count: number): TaskType[] => {
  const tasks: TaskType[] = [];
  for (let i = 0; i < count; i++) {
    const task: TaskType = {
      id: faker.number.int({ min: 0, max: 999 }),
      text: faker.lorem.words(2),
      completed: faker.datatype.boolean(),
      time: faker.date.future().toISOString(),
      desc: faker.lorem.lines(2),
      priority: faker.helpers.arrayElement(["low", "medium", "high"]),
      deadline: faker.date.future().toISOString(),
      tags: [faker.lorem.word(), faker.lorem.word(), faker.lorem.word()],
      type: "math",
    };
    tasks.push(task);
  }
  return tasks;
};

export const generateOneTaskData = (): TaskType => {
  return {
    id: faker.number.int({ min: 0, max: 999 }),
    text: faker.lorem.words(10),
    completed: faker.datatype.boolean(),
    time: faker.date.future().toISOString(),
    desc: faker.lorem.lines(2),
    priority: faker.helpers.arrayElement(["low", "medium", "high"]),
    deadline: faker.date.future().toISOString(),
    tags: [faker.lorem.word(), faker.lorem.word(), faker.lorem.word()],
    type: "math",
  };
};

export const generateFakeclassifyTask = (count: number): classifyTask[] => {
  const tasks: classifyTask[] = [];

  for (let i = 0; i < count; i++) {
    const task: classifyTask = {
      category: faker.helpers.arrayElement([
        "數學",
        "國文",
        "英文",
        "工程數學",
        "地理",
      ]),
      description: faker.lorem.sentence(),
      dueDate: faker.date.future(),
      completed: faker.datatype.boolean(),
    };

    tasks.push(task);
  }

  return tasks;
};
