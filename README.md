# This project is used for task management.

# Endpoints:

# 1. To Register a user.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/users/register/
       request payload : username   <string>
                         password   <varchar>
                         first_name <string>
                         last_name  <string>
                         email      <email format>

# 2. To Login.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/users/login/
       request payload : username   <string>
                         password   <varchar>

# 3. To Logout.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/users/logout/
       request header: Authorization : Token <token>

# 4. To create task.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/tasks/
       request payload : title   <string>
                         description   <string>
                         due_date <YYYY-MM-DD>
                         status  <string> (use only these strings (case sensitive) : Todo, Inprogress, Done)

# 5. To get all tasks list
       Method: GET
       url: http://surajkumar1998.pythonanywhere.com/tasks

# 6. To get a specific task.
       Method: GET
       url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id> (you an get task_id from task list (above) API)

# 7. To update a task.
       Method: PUT
       url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/
       request payload : title   <string>
                         description   <string>
                         due_date <YYYY-MM-DD>

# 8. To delete a task.
       Method: DELETE
       url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/

# 9. To add memeber to a task.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/add_member/
       request payload : user_id  <int>

# 10. To get all members associated to a task
        Method: GET
        url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/members

# 11. To remove a member from a task.
       Method: POST
       url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/remove_member/
       request payload : user_id  <int>

# 12. To update status of task.
        Method: PUT
        url: http://surajkumar1998.pythonanywhere.com/tasks/<task_id>/update_status/
        request payload : status  <string> (use only these strings: Todo, Inprogress, Done)

    


   


   
