<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Bullet Journal</h1>
        <br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
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
            <tr>
              <td><i class="bi bi-circle"></i></td>
              <td>bar</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">Mark Complete</button>
                  <button type="button" class="btn btn-secondary btn-sm">Migrate</button>
                </div>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Edit</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>