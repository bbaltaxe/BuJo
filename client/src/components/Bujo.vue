<template>

  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Bullet Journal</h1> 
         <v-icon icon="home" />
        <br><br>
        <table class="table-borderless table-hover">
          <tbody>
            <tr v-for="(task,index) in tasks" :key="index">
              <td>
                <i
                  :class="task.done ? 'bi bi-circle-fill' : 'bi bi-circle'"
                  @click="task.done = !task.done;" 
                ></i>&emsp;  
              </td>
              <td>{{ task.task }}</td>
            </tr> 
            <tr>
              <td colspan="2">        
                <!-- INPUT A NEW TASK -->
                <v-text-field density="compact" label="add item" @keydown.enter="handleAdd" v-model="newTask"></v-text-field>
              </td>
            </tr>
          </tbody>
        </table>

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
      newTask: '',
      // statusIcon: 'bi-circle',
      // status_icons: ['bi-circle', 'bi-circle-right', 'bi-arrowright-circle', 'bi-exclamation-circle', 'bi-x-circle'
      // ],
    };
  },
  methods: {
    addTask(payload){ 
      const path = 'http://127.0.0.1:5000/tasks'
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
        })
        .catch((error) => {

          console.log(error);
          this.getTasks();
        });
    },
    getTasks() {
      const path = 'http://127.0.0.1:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAdd(){
      const payload = {
        task: this.newTask,
      };
      // reinit
      this.newTask = ''; 
      this.addTask(payload);
    }
  },
  created() {
    this.getTasks();
  },
};
</script>