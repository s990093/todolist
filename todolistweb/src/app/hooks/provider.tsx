"use client";
import React, { createContext, useState } from "react";
import { TaskStatus } from "../interface/api";

interface ContextType {
  state: {
    userID: boolean;
    user: any;
    loading: boolean;
    authenticated: boolean;
    isRegistered: boolean;
    taskStatus: TaskStatus;
  };
  setIsRegistered: (value: boolean) => void;
}

let Context = createContext<ContextType>({
  state: {
    userID: false,
    user: undefined,
    loading: true,
    authenticated: false,
    isRegistered: false,
    taskStatus: {
      tasks_registered: false,
      tasks_empty: false,
      tasks: [],
    },
  },
  setIsRegistered: () => {},
});

function Provider(props: {
  children: React.ReactNode;
  taskStatus: TaskStatus;
}) {
  const { taskStatus } = props;
  const initialState = {
    userID: false,
    user: undefined,
    loading: true,
    authenticated: false,
    isRegistered: true,
    taskStatus: taskStatus,
  };

  const [state, updateState] = useState(initialState);

  const setIsRegistered = (value: boolean) => {
    updateState({ ...state, isRegistered: value });
  };

  return (
    <Context.Provider
      value={{
        state: state,
        setIsRegistered: setIsRegistered,
      }}
    >
      {props.children}
    </Context.Provider>
  );
}

const Consumer = Context.Consumer;
export { Provider, Consumer, Context };
