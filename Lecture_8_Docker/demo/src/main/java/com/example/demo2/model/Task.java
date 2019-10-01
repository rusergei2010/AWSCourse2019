package com.example.demo2.model;

public class Task {

    private String taskName;

    public Task(final String s) {
        taskName = s;
    }

    public String getTaskName() {
        return taskName;
    }

    public void setTaskName(final String taskName) {
        this.taskName = taskName;
    }
}
