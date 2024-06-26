export interface TaskType {
  id: number; // Unique identifier for the task
  text: string; // Description of the task
  completed: boolean; // Status of the task
  time: string; // Time associated with the task
  desc?: string; // Additional description for the task
  priority: "low" | "medium" | "high"; // Priority level of the task
  deadline?: string; // Optional deadline for the task
  type: string;
  tags?: string[]; // Optional tags associated with the task
}

export interface BaseTask {
  description: string;
  dueDate: Date;
  completed: boolean;
}

export interface classifyTask extends BaseTask {
  category: string;
}

export interface TaskCompletion extends BaseTask {
  subject: string;
}

// Define the props for the Task component
export interface TaskProps {
  task: TaskType; // A single task object
  onRemove: (id: number) => void; // Function to remove a task by ID
  onToggleComplete: (id: number) => void; // Function to toggle task completion
}

export interface LongTermGoal {
  id: number;
  title: string;
  description: string;
  targetDate: Date;
  progress: number;
}
