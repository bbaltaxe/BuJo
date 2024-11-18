<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Bullet Journal</h1>
        <br><br>
        <table class="table-borderless table-hover">
        <!-- 
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          
          </thead>
        -->
          <tbody>
            <tr v-for="(task,index) in tasks" :key="index">
              <td>
                <i
                  :class="task.done ? 'bi bi-circle-fill' : 'bi bi-circle'"
                  @click="task.done = !task.done;" 
                ></i>
              </td>
              <td>{{ task.task }}</td>
<!--               <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">Mark Complete</button>
                  <button type="button" class="btn btn-secondary btn-sm">Migrate</button>
                </div>
              </td> -->
              <!-- <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Edit</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td> -->
            </tr> 
          </tbody>
        </table>
        <br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5001/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // editTaskStatus(status){
    //   if ()
    // }
  },
  created() {
    this.getTasks();
  },
};
</script>