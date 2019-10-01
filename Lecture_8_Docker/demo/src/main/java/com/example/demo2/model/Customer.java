package com.example.demo2.model;

import java.util.Arrays;
import java.util.Date;
import java.util.List;


public class Customer {

    private Date created = new Date();
    private String name = "Sergey";
    private List<Task> task =
            Arrays.asList(
                    new Task("Task 1"),
                    new Task("Task N"));

    public Customer(final String name) {
        this.name = name;
    }

    public Date getCreated() {
        return created;
    }

    public void setCreated(final Date created) {
        this.created = created;
    }

    public String getName() {
        return name;
    }

    public void setName(final String name) {
        this.name = name;
    }

    public List<Task> getTask() {
        return task;
    }

    public void setTask(final List<Task> task) {
        this.task = task;
    }
}
